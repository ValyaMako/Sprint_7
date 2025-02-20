import random
import string
import allure

@allure.step('Метод генерирует строку, состоящую только из букв нижнего регистра, в качестве параметра передаём длину строки')
def generate_random_string(length):
    letters = string.ascii_lowercase
    random_string = ''.join(random.choice(letters) for i in range(length))
    return random_string

@allure.step('Генерируем логин, пароль и имя курьера')
def generate_courier_data():
    login = generate_random_string(10)
    password = generate_random_string(10)
    first_name = generate_random_string(10)
    return login, password, first_name