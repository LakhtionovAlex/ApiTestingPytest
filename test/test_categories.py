import pytest
import allure
import random
from http import HTTPStatus

from utils.assertions import Assert
from api.categories import categories_api
from schemas.validate_schema import CATEGORY_SCHEMA
from data.models import road_csv_file_create_category, get_all_id_categories, road_csv_file_update_category


@pytest.mark.smoke
@pytest.mark.regression
@allure.feature("Categories API")
@allure.story("Get Categories List")
@allure.severity(allure.severity_level.CRITICAL)
@allure.testcase("128")
def test_categories_list():
    with allure.step("Sending request to get categories list"):
        res = categories_api.categories_list()
        print(res.json())

    with allure.step("Verifying response status code"):
        assert res.status_code == HTTPStatus.OK

    with allure.step("Verifying response headers"):
        assert res.headers['Content-Type'] == 'application/json'

    with allure.step("Logging response details"):
        allure.attach("Response Headers", str(res.headers), allure.attachment_type.TEXT)


@pytest.mark.regression
@allure.story("Create Category")
@pytest.mark.parametrize("title, parent_id, description",
                         road_csv_file_create_category('/data/create_categories_positive.csv'))
def test_create_categories_positive(authorization_admin_token, title, parent_id, description):

    res = categories_api.categories_create(authorization_admin_token, title=title, parent_id=parent_id,
                                           description=description)

    assert res.status_code == HTTPStatus.CREATED
    assert res.headers['Content-Type'] == 'application/json'
    res_body = res.json()

    assert 'id' in res_body
    res_delete = categories_api.categories_destroy(res_body['id'], authorization_admin_token)
    assert res_delete.status_code == HTTPStatus.NO_CONTENT


@pytest.mark.regression
@allure.story("Create Category")
@pytest.mark.parametrize("title, parent_id, description",
                         road_csv_file_create_category('/data/create_category_negative.csv'))
def test_create_categories_negative(authorization_admin_token, title, parent_id, description):
    res = categories_api.categories_create(authorization_admin_token, title=title, parent_id=parent_id,
                                           description=description)

    assert res.status_code == HTTPStatus.BAD_REQUEST
    print(res.json())


@pytest.mark.regression
@allure.story("Get Categories Retrieve")
@pytest.mark.parametrize("id", random.sample(get_all_id_categories(), 10))
def test_categories_retrieve(id):
    res = categories_api.categories_retrieve(id)

    assert res.status_code == HTTPStatus.OK
    assert res.headers['Content-Type'] == 'application/json'
    res_body = res.json()
    Assert.validate_schema(res_body, schema=CATEGORY_SCHEMA)


@pytest.mark.regression
@allure.story("Update Category")
@pytest.mark.parametrize("id", random.sample(get_all_id_categories(), 4))
@pytest.mark.parametrize("title, description",
                         road_csv_file_update_category('/data/update_category_positive.csv'))
def test_categories_update(id, authorization_admin_token, title, description):
    """
    Modifying a category and reverting to the original category
    """
    get_original_category = categories_api.categories_retrieve(id)
    result_original_category = get_original_category.json()

    result_update_category = categories_api.categories_update(id, authorization_admin_token,
                                                              title=title,
                                                              description=description)

    assert result_update_category.status_code == HTTPStatus.OK
    assert result_update_category.headers['Content-Type'] == 'application/json'

    revert_back_original_category = categories_api.categories_update(id, authorization_admin_token,
                                                                     title=result_original_category['title'],
                                                                     description=result_original_category['description'])

    assert revert_back_original_category.status_code == HTTPStatus.OK
    assert revert_back_original_category.headers['Content-Type'] == 'application/json'


