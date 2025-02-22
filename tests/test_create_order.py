import pytest
import allure

from api_methods import ApiMethods

class TestCreateOrder:

    @pytest.mark.parametrize("color", ["BLACK", "GREY", "", "BLACK, GREY"])
    @allure.title('Проверяем создание заказа')
    @allure.description('Проверяем, что заказ можно создать выбрав разные варианты цвета. Тело ответа содержит "track"')
    def test_create_order_with_choice_of_color(self, color):
        order_response = ApiMethods.create_order(color)
        assert order_response.status_code == 201
        assert "track" in order_response.json()
