import requests
import urls
from data import *

class ApiMethods:
    @staticmethod
    @allure.step('Метод регистрации нового курьера возвращает ответ на запрос и список из логина, пароля и имени')
    def register_new_courier_and_return_login_password(data):
        login_pass = []
        reg_response = requests.post(urls.courier, json=data)

        # если регистрация прошла успешно (код ответа 201), добавляем в список login_pass логин, пароль и имя курьера
        if reg_response.status_code == 201:
            login_pass.append(data["login"])
            login_pass.append(data["password"])
            login_pass.append(data["firstName"])

        return login_pass, reg_response

    @staticmethod
    @allure.step('Метод авторизации курьера')
    def courier_auth(auth_data):
        auth_response = requests.post(urls.courier_login, json=auth_data)
        return auth_response

    @staticmethod
    @allure.step('Метод удаления курьера')
    def delete_courier(courier_id):
        del_response = requests.delete(f"{urls.courier}/{courier_id}")
        return del_response

    @staticmethod
    @allure.step('Метод создания заказа')
    def create_order(color):
        payload = get_order_payload(color)
        order_response = requests.post(urls.orders, json=payload)
        return order_response

    @staticmethod
    @allure.step('Метод получение списка заказов')
    def get_order_list():
        response = requests.get(urls.orders)
        return response