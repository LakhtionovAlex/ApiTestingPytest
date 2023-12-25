import pytest
import random
import allure

from http import HTTPStatus

from utils.assertions import Assert
from api.admin import kazi_admin_api
from data.models import get_all_id_tags, get_all_id_categories, get_all_id_product
from schemas.validate_schema import TAGS_LIST_SCHEMA


@pytest.mark.smoke
@allure.story("Tags")
@pytest.mark.regression
def test_kazi_admin_tags_list(authorization_admin_token):
    res = kazi_admin_api.kazi_admin_tags_list(authorization_admin_token)

    assert res.status_code == HTTPStatus.OK
    assert res.headers['Content-Type'] == "application/json"
    Assert.validate_schema(res.json(), schema=TAGS_LIST_SCHEMA)
    print(get_all_id_tags(authorization_admin_token))


@pytest.mark.regression
@allure.story("Tags")
@pytest.mark.parametrize("source", ['qgold', 'stuller', 'swissmadecorp', 'midtownwatchdeals',
                                    'masterluxury', 'bonetawholesale'])
def test_kazi_admin_tags_by_source_create(authorization_admin_token, source):
    res = kazi_admin_api.kazi_admin_tags_by_source_create(authorization_admin_token,
                                                          get_all_id_tags(authorization_admin_token), source)
    res_body = res.json()
    example_add_tags = {
        "detail": "Tags successfully added to products by source"
    }
    example_delete_tags = {
        'detail': f'Tags successfully removed for products where thesource of the item is {source}'
    }
    assert res.status_code == HTTPStatus.CREATED
    assert res_body == example_add_tags
    assert res.headers['Content-Type'] == "application/json"
    res_delete = kazi_admin_api.kazi_admin_tags_by_source_destroy(authorization_admin_token,
                                                                  get_all_id_tags(authorization_admin_token), source)

    assert res_delete.status_code == HTTPStatus.OK
    assert res_delete.json() == example_delete_tags


@pytest.mark.regression
@allure.story("Tags")
@pytest.mark.parametrize("id", random.sample(get_all_id_categories(), 5))
def test_category_tags_create(authorization_admin_token, id):
    res = kazi_admin_api.kazi_admin_category_tags_create(authorization_admin_token,
                                                         get_all_id_tags(authorization_admin_token), id)
    res_body = res.json()
    example = {
        "detail": f"Tags were successfully added for products that have a category: {id}"
    }
    assert res.status_code == HTTPStatus.CREATED
    assert res_body == example
    assert res.headers['Content-Type'] == "application/json"
    res_delete = kazi_admin_api.kazi_admin_category_tags_destroy(authorization_admin_token,
                                                                 get_all_id_tags(authorization_admin_token), id)
    assert res_delete.status_code == HTTPStatus.OK


@pytest.mark.regression
@allure.story("Category by Product")
@pytest.mark.parametrize("category", random.sample(get_all_id_categories(), 5))
def test_product_category_create(authorization_admin_token, category):
    res = kazi_admin_api.kazi_admin_product_category_create(authorization_admin_token, get_all_id_product(), category)
    res_body = res.json()
    example = {
        "detail": "Products linked to categories successfully"
    }
    assert res.status_code == HTTPStatus.CREATED
    assert res_body == example
    assert res.headers['Content-Type'] == "application/json"
    res_delete = kazi_admin_api.kazi_admin_product_category_destroy(authorization_admin_token,
                                                                    get_all_id_product(), category)

    assert res_delete.status_code == HTTPStatus.OK


@pytest.mark.regression
@allure.story("Categories by Category")
@pytest.mark.parametrize("category", random.sample(get_all_id_categories(), 5))
def test_kazi_admin_categories_by_category_create(authorization_admin_token, category):
    list_category = random.sample(get_all_id_categories(), 5)
    res = kazi_admin_api.kazi_admin_categories_by_category_create(authorization_admin_token,
                                                                  category, list_category)
    example = {
        "detail": "Categories successfully added to products by category"
    }

    assert res.status_code == HTTPStatus.CREATED
    assert res.json() == example
    assert res.headers['Content-Type'] == "application/json"

    res_delete = kazi_admin_api.kazi_admin_categories_by_category_destroy(authorization_admin_token,
                                                                          category, list_category)
    assert res_delete.status_code == HTTPStatus.NO_CONTENT
