from conftest import courier
from data import *
from api_methods import ApiMethods
import pytest

class TestCourierLogin:
    @allure.title('Проверяем, что курьер может авторизоваться, передав все обязательные поля, - запрос возвращает id')
    def test_courier_login_success(self, courier):
        _, _, auth_response, _ = courier
        assert auth_response.status_code == 200
        assert "id" in auth_response.json()

    @pytest.mark.parametrize("invalid_auth_data", [get_auth_data_wrong_login, get_auth_data_wrong_password])
    @allure.title('Проверяем, что запрос возвращает ошибку, если неверно указаны логин или пароль')
    def test_courier_login_wrong_login_or_password_error(self, courier, invalid_auth_data):
        login_pass, _, _, _ = courier
        wrong_auth_data = invalid_auth_data(login_pass)
        auth_response = ApiMethods.courier_auth(wrong_auth_data)
        assert auth_response.status_code == 404
        assert auth_response.json() == auth_courier[404]

    @pytest.mark.parametrize("incomplete_data", [get_auth_data_without_login, get_auth_data_without_password])
    @allure.title('Проверяем, что запрос возвращает ошибку, если не указаны логин или пароль')
    def test_courier_login_without_login_or_password_error(self, courier, incomplete_data):
        login_pass, _, _, _ = courier
        wrong_auth_data = incomplete_data(login_pass)
        auth_response = ApiMethods.courier_auth(wrong_auth_data)
        assert auth_response.status_code == 400
        assert auth_response.json() == auth_courier[400]

    @allure.title('Проверяем, что запрос возвращает ошибку, если авторизоваться под несуществующим пользователем')
    def test_courier_login_nonexistent_user_error(self):
        auth_data = get_auth_data_for_nonexistent_user()
        auth_response = ApiMethods.courier_auth(auth_data)
        assert auth_response.status_code == 404
        assert auth_response.json() == auth_courier[404]
