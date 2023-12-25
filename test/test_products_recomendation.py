import pytest
import allure

from api.products_recomendation import products_recomendation_api
from http import HTTPStatus


@pytest.mark.smoke
@pytest.mark.regression
@allure.story("Products Recomendation")
@pytest.mark.parametrize("iteration", range(10))
def test_products_recomendation_retrieve(authorization_user_token, iteration):
    res = products_recomendation_api.products_recomendation_retrieve(authorization_user_token)
    assert res.status_code == HTTPStatus.OK
