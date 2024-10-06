import allure
import pytest


class Test_Pytest():

    @allure.feature("«Примеры использования для успешного тестирования»")
    def test_one(self):
        print("выполнение метода test_one")
        assert 1 == 1

    @allure.feature("«Случаи использования, когда тест не прошел»")
    def test_two(self):
        print("выполнение метода test_two")
        assert "s" in "love"

    @allure.feature("«Случаи сбоя теста»")
    def test_three(self):

        print("Выполнение метода test_three")
        assert 3 - 2 != 1

    @allure.feature("«Случаи сбоя теста»")
    def test_four(self):
        print("Выполнение метода test_four")

if __name__ == "__main__":
    pytest.main(["-s", "-q", "--alluredir", "./report", "-n", "auto"])
