import pytest
import allure
from http import HTTPStatus
from utils.assertions import Assert

from api.admin import kazi_admin_api
from schemas.validate_schema import LIST_USERS_SCHEMA


@pytest.mark.smoke
@pytest.mark.regression
@allure.story("Users")
def test_kazi_admin_list_users(authorization_admin_token):
    res = kazi_admin_api.kazi_admin_list_users(authorization_admin_token)
    res_body = res.json()

    assert res.status_code == HTTPStatus.OK
    assert res.headers['Content-Type'] == "application/json"
    Assert.validate_schema(res_body, schema=LIST_USERS_SCHEMA)
