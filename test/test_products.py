import pytest
import allure

from api.products import products_api
from http import HTTPStatus


@pytest.mark.smoke
@pytest.mark.regression
@allure.story("Product")
def test_product_list():
    res = products_api.products_list()

    assert res.status_code == HTTPStatus.OK
    assert res.headers['Content-Type'] == "application/json"
