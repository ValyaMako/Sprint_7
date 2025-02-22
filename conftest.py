import pytest
from data import *
from api_methods import ApiMethods


@pytest.fixture
def courier():
    data = valid_courier_data()
    login_pass, reg_response = ApiMethods.register_new_courier_and_return_login_password(data)

    auth_data = get_auth_data(login_pass)
    auth_response = ApiMethods.courier_auth(auth_data)
    courier_id = (auth_response.json())["id"]

    yield login_pass, reg_response, auth_response, courier_id

    ApiMethods.delete_courier(courier_id)

