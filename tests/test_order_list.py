import allure
from api_methods import ApiMethods

class TestOrderList:

    @allure.title('Проверяем, что в теле ответа возвращается список заказов')
    @allure.description('Проверяем, что в теле ответа содержиться ключ "orders" и что значение по ключу "orders" это список')
    def test_get_order_list(self):
        response = ApiMethods.get_order_list()
        assert response.status_code == 200
        assert "orders" in response.json() and isinstance(response.json()['orders'], list)