from helpers import *
import allure

@allure.step('Получаем тело запроса для успешной регистрации курьера')
def valid_courier_data():
    login, password, first_name = generate_courier_data()
    return {
        "login": login,
        "password": password,
        "firstName": first_name
    }

@allure.step('Получаем тело запроса для успешной авторизации курьера')
def get_auth_data(data):
    login = data[0]
    password = data[1]
    return {
        "login": login,
        "password": password
    }

@allure.step('Получаем тело запроса для повторной регистрации курьера')
def get_register_data(login, password, first_name):
    return {
        "login": login,
        "password": password,
        "firstName": first_name
    }

@allure.step('Получаем тело запроса для регистрации курьера с существующим логином')
def get_register_data_with_existing_login(login):
    _, password, first_name = generate_courier_data()
    return {
        "login": login,
        "password": password,
        "firstName": first_name
    }

@allure.step('Получаем тело запроса для регистрации курьера без логина')
def invalid_data_without_login():
    login, password, first_name = generate_courier_data()
    return {
        "login": "",
        "password": password,
        "firstName": first_name
    }

allure.step('Получаем тело запроса для регистрации курьера без пароля')
def invalid_data_without_password():
    login, password, first_name = generate_courier_data()
    return {
        "login": login,
        "password": "",
        "firstName": first_name
    }

@allure.step('Получаем тело запроса для авторизации курьера с неправильным логином')
def get_auth_data_wrong_login(login_pass):
    login, _, _ = generate_courier_data()
    password = login_pass[1]
    return {
        "login": login,
        "password": password,
    }
@allure.step('Получаем тело запроса для авторизации курьера с неправильным паролем')
def get_auth_data_wrong_password(login_pass):
    _, password, _ = generate_courier_data()
    login = login_pass[0]
    return {
        "login": login,
        "password": password,
    }

@allure.step('Получаем тело запроса для авторизации курьера без логина')
def get_auth_data_without_login(login_pass):
    password = login_pass[1]
    return {
        "login": "",
        "password": password,
    }

@allure.step('Получаем тело запроса для авторизации курьера без пароля')
def get_auth_data_without_password(login_pass):
    login = login_pass[0]
    return {
        "login": login,
        "password": "",
    }

@allure.step('Получаем тело запроса для авторизации незарегистрированного курьера')
def get_auth_data_for_nonexistent_user():
    login, password, _ = generate_courier_data()
    return {
        "login": login,
        "password": password,
    }

@allure.step('Получаем тело запроса для создания заказа')
def get_order_payload(color):
    return {
    "firstName": "Naruto",
    "lastName": "Uchiha",
    "address": "Konoha, 142 apt.",
    "metroStation": 4,
    "phone": "+7 800 355 35 35",
    "rentTime": 5,
    "deliveryDate": "2020-06-06",
    "comment": "Saske, come back to Konoha",
    "color": [color]
}

# Коды ответов и сообщения на создание курьера
create_courier = {
    201: {"ok": True},
    400: {"code": 400, "message": "Недостаточно данных для создания учетной записи"},
    409: {"code": 409, "message": "Этот логин уже используется. Попробуйте другой."}
}

# Коды ответов и сообщения на авторизацию курьера
auth_courier = {
    200: {"id": 12345},
    400: {"code": 400, "message":  "Недостаточно данных для входа"},
    404: {"code": 404, "message":  "Учетная запись не найдена"}
  }


