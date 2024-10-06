import time
import pytest
import allure
from pages.AbsolutPages import SearchHelper, SeacrhLocators


@pytest.mark.parametrize('data', [["Иванов Иван Иванович",
                                   "18.05.2004",
                                   "1234-567890",
                                   "18.10.2023",
                                   "Респ Крым, г Симферополь, пр-кт Академика Вернадского, д 7",
                                   "(999)999-9999",
                                   "email@absolutins.io"]])
def test_search(browser, data):

    # Подгружаем локаторы
    locators = SeacrhLocators()

    # Инициализация драйвера
    open_page = SearchHelper(browser)

    # Переходим на страницу
    with allure.step('Открытие страницы в драйвере'):
        open_page.go_to_site()

    with allure.step('Прохождение формы: "Рассчет".'):

        with allure.step('Последовательный клик по чекбоксам.'):
            with allure.step("Чекбокс #1 --- Профессиональная сфера связана с медицинской деятельностью"):
                open_page.click_on_the_search_element(locators.LOCATOR_FIRST_CHECKBOX)

            with allure.step("Чекбокс #2 --- Подтверждаю что ..."):
                open_page.click_on_the_search_element(locators.LOCATOR_SECOND_CHECKBOX)

            with allure.step("Чекбокс #3 --- Согласие на обработку персональных данных"):
                open_page.click_on_the_search_element(locators.LOCATOR_THIRD_CHECKBOX)

        with allure.step('Переход к форме "Ввод данных" по кнопке "Продолжить"'):

            # with allure.step('Шаг #0 --- Проверяем активна или кнопка "Продолжить"'):
            #     open_page.is_clickable(locators.LOCATOR_FIRST_BUTTON)

            with allure.step('Шаг #1 --- Разблокировка кнопки'):
                open_page.unblock_element(locators.LOCATOR_FIRST_BUTTON)

            with allure.step('Шаг #2 --- Нажатие на кнопку "Продолжить"'):
                open_page.click_on_the_search_element(locators.LOCATOR_FIRST_BUTTON)

#####################################################################################################################
#####################################################################################################################
#####################################################################################################################

    with allure.step('Заполнение формы "Ввод данных".'):

        with allure.step('Заполнение формы "Ввод данных"'):
            with allure.step('Заполнение поля "ФИО страхователя"'):
                open_page.enter_word(locators.LOCATOR_Name, data[0])

            with allure.step('Заполнение поля "Дата рождения страхователя"'):
                open_page.enter_word(locators.LOCATOR_Birthday, data[1])

            with allure.step('Заполнение поля "Серия/номер паспорта страхователя"'):
                open_page.enter_word(locators.LOCATOR_Passport_number, data[2])

            with allure.step('Заполнение поля "Дата выдачи"'):
                open_page.enter_word(locators.LOCATOR_Passport_date, data[3])

            with allure.step('Заполнение поля "Адресс регистрации"'):
                open_page.enter_word(locators.LOCATOR_Place_of_Registracit, data[4])

            with allure.step('Заполнение поля "Телефон"'):
                open_page.enter_word(locators.LOCATOR_Telefon_number, data[5])

            with allure.step('Заполнение поля "Email"'):
                open_page.enter_word(locators.LOCATOR_Email, data[6])

        with allure.step('Заполнение дополнительных данных на форме "Ввод данных"'):
            with allure.step('Сняимаем чек с чекбокса "Страхователь является застрахованным"'):
                open_page.click_on_the_search_element(locators.LOCATOR_DOP_CHECKBOX)

            with allure.step('Заполнение поля "ФИО застрахованного"'):
                open_page.enter_word(locators.LOCATOR_DOP_Name, data[0])

            with allure.step('Заполнение поля "Дата рождения застрахованного"'):
                open_page.enter_word(locators.LOCATOR_DOP_Birthday, data[1])

            with allure.step('Заполнение поля "Серия и номер паспорта застрахованного"'):
                open_page.enter_word(locators.LOCATOR_DOP_Passport_number, data[2])

            with allure.step('Заполнение поля "Дата выдачи паспорта застрахованного"'):
                open_page.enter_word(locators.LOCATOR_DOP_Passport_date, data[3])

        with allure.step('Переход к форме "Оплата" по кнопке "Перейти к оплате"'):
            open_page.click_on_the_search_element(locators.LOCATOR_SECOND_BUTTON)

#####################################################################################################################
#####################################################################################################################
#####################################################################################################################

    with allure.step('Взаимодействие с банками на форме "Оплата".'):

        with allure.step('Проверка отображения "Суммы"'):
            open_page.check_value_on_the_element(locators.LOCATOR_BUY_COST)

        with allure.step('Проведение оплаты'):

            with allure.step('Оплата "Tinkoff"'):

                with allure.step('Клик по кнопке "Tinkoff"'):
                    open_page.click_on_the_search_element(locators.LOCATOR_BUY_TINKOFF)
                    time.sleep(2)

                with allure.step('Закрытие QR-кода оплаты'):
                    open_page.click_on_the_search_element(locators.LOCATOR_BUY_CLOSE)
                    time.sleep(2)

            with allure.step('Оплата "СБП"'):

                with allure.step('Клик по кнопке "СБП"'):
                    open_page.click_on_the_search_element(locators.LOCATOR_BUY_SBP)
                    time.sleep(2)

                with allure.step('Закрытие QR-кода оплаты'):
                    open_page.click_on_the_search_element(locators.LOCATOR_BUY_CLOSE)
                    time.sleep(2)

            with allure.step('Оплата "Картой"'):

                with allure.step('Проводим олату картой по кнопке "Оплатить"'):

                    with allure.step('Клик по кнопке "Оплатить"'):
                        open_page.search_element(locators.LOCATOR_BUY_BUTTON)
                        open_page.final_screen()


if __name__ == "__main__":
    pytest.main(["-s", "-q"])
