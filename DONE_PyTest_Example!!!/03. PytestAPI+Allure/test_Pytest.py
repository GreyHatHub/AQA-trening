import pytest
import allure

@allure.feature('List of dog images')
@allure.story('Список определенного количества случайных фото')
@pytest.mark.parametrize("number_of_images", [i for i in range(1, 10)])
def test_get_few_sub_breed_random_images(request_api, number_of_images):
    response = request_api.get(f"breed/hound/afghan/images/random/{number_of_images}")

    with allure.step("Запрос отправлен. Десериализируем ответ из json в словарь."):
        response = response.json()

    with allure.step("Посмотрим длину списка со ссылками на фото"):
        final_len = len(response["message"])

    assert final_len == number_of_images, f"Количество фото не {number_of_images}, а {final_len}"


if __name__ == "__main__":
    pytest.main(["-s", "-q", "--alluredir", "./report", "-n", "auto"])
