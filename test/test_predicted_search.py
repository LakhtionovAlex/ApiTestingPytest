import pytest
import allure

from api.predicted_search import predicted_search
from http import HTTPStatus


@pytest.mark.smoke
@pytest.mark.regression
@allure.story("Predicted Search")
@pytest.mark.parametrize("repeat", range(20))
def test_predicted_search_retrieve(repeat):
    res = predicted_search.predicted_search_retrieve()
    assert res.status_code == HTTPStatus.OK
