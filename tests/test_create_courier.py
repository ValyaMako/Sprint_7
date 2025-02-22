import pytest
from api_methods import ApiMethods
from data import *
from conftest import courier


class TestCreateCourier:

    @allure.title('Проверяем, что запрос на создание курьера возвращает код 201 и соответствующий ответ, если отправить все обязательные поля')
    def test_create_courier_correct_code_and_response(self, courier):
        _, reg_response, _, _ = courier
        assert reg_response.status_code == 201
        assert reg_response.json() == create_courier[201]

    @allure.title('Проверяем, что курьера можно создать')
    @allure.description('В качестве подтверждения создания курьера, авторизируем его (код ответа - 200)')
    def test_create_courier_success(self, courier):
        _, _, auth_response, _ = courier
        assert auth_response.status_code == 200
        assert "id" in auth_response.json()

    @allure.title('Проверяем, что нельзя создать двух одинаковых курьеров')
    def test_create_identical_courier_error(self, courier):
        login_pass, _, _, _ = courier
        login = login_pass[0]
        password = login_pass[1]
        first_name = login_pass[2]
        register_data = get_register_data(login, password, first_name)
        _, second_reg_response = ApiMethods.register_new_courier_and_return_login_password(register_data)
        assert second_reg_response.status_code == 409
        assert second_reg_response.json() == create_courier[409]

    @allure.title('Проверяем, что запрос возвращает ошибку, если создавать пользователя с уже существующим логином')
    def test_create_courier_with_existing_login_error(self, courier):
        login_pass, _, _, _ = courier
        login = login_pass[0]
        register_data = get_register_data_with_existing_login(login)
        _, second_reg_response = ApiMethods.register_new_courier_and_return_login_password(register_data)
        assert second_reg_response.status_code == 409
        assert second_reg_response.json() == create_courier[409]

    @pytest.mark.parametrize("invalid_data", [invalid_data_without_login(), invalid_data_without_password()])
    @allure.title('Проверяем, что запрос возвращает ошибку, если нет одного из обязательных полей')
    def test_create_courier_without_field_error(self, invalid_data):
        _, reg_response = ApiMethods.register_new_courier_and_return_login_password(invalid_data)
        assert reg_response.status_code == 400
        assert reg_response.json() == create_courier[400]
