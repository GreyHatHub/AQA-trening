import allure
from app.BaseApp import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class SeacrhLocators:

    # Меню расчет
    LOCATOR_FIRST_CHECKBOX = (By.XPATH, '//div[contains(@class, "step1")]/label[1]/span')
    LOCATOR_SECOND_CHECKBOX = (By.XPATH, '//div[contains(@class, "step1")]/label[2]/span')
    LOCATOR_THIRD_CHECKBOX = (By.XPATH, '//div[contains(@class, "step1")]/label[3]/span')
    LOCATOR_FIRST_BUTTON = (By.XPATH, '//button[@name="calculate"]')
    
    # Меню формы
    # Локаторы основного меню
    LOCATOR_Name = (By.ID, 'name')
    LOCATOR_Birthday = (By.ID, 'dateBirth')
    LOCATOR_Passport_number = (By.ID, 'id')
    LOCATOR_Passport_date = (By.ID, 'idDate')
    LOCATOR_Place_of_Registracit = (By.ID, 'address')
    LOCATOR_Telefon_number = (By.ID, 'phone')
    LOCATOR_Email = (By.ID, 'email')
    LOCATOR_SECOND_BUTTON = (By.XPATH, '//*[contains(text(), "Перейти к оплате")]')
    # Локаторы домолнительного меню
    LOCATOR_DOP_CHECKBOX = (By.XPATH, '//form[contains(@class, "step2")]/label/span')
    LOCATOR_DOP_Name = (By.ID, 'nameInsured')
    LOCATOR_DOP_Birthday = (By.ID, 'dateBirthInsured')
    LOCATOR_DOP_Passport_number = (By.ID, 'idInsured')
    LOCATOR_DOP_Passport_date = (By.ID, 'idDateInsured')

    # Кабинет оплаты
    # Меню суммы
    LOCATOR_BUY_COST = (By.XPATH, '//span[contains(@class, "t-container")]/span[1]/span[1]')
    LOCATOR_BUY_DROP_DOWN_LIST = (By.XPATH, '//tui-svg[contains(@class, "expand-arrow")]/svg')
    # Быстрая оплата
    LOCATOR_BUY_CLOSE = (By.XPATH, '//button[contains(@class, "close")]')
    LOCATOR_BUY_TINKOFF = (By.XPATH, '//div[contains(@data-appearance, "tinkoffPay")]')
    LOCATOR_BUY_SBP = (By.XPATH, '//div[contains(@data-appearance, "payment")]')
    # Оплата картой
    LOCATOR_BUY_CARD_NUMBER = (By.XPATH, '//input[contains(@automation-id, "tui-input-card-grouped__card")]')
    LOCATOR_BUY_CARD_DATE = (By.XPATH, '//input[contains(@id, "_expire")]')
    LOCATOR_BUY_CARD_CVC = (By.XPATH, '//input[contains(@automation-id, "tui-input-card-grouped__cvc")]')
    LOCATOR_BUY_CHECKBOX = (By.XPATH, '//input[contains(@automation-id, "tui-checkbox__native")]')
    LOCATOR_BUY_EMAIL = (By.ID, 'email')
    LOCATOR_BUY_BUTTON = (By.XPATH, '//button[contains(@class, "eacq-form__button")]')


class SearchHelper(BasePage):

    def enter_word(self, locator, word):
        search_field = self.find_element(locator)
        search_field.click()
        search_field.send_keys(word, Keys.ENTER)
        return search_field
        
    def unblock_element(self, locator):
        search_element = self.find_element(locator)
        self.driver.execute_script("arguments[0].removeAttribute('disabled')", search_element)

    def click_on_the_search_element(self, locator):
        return self.find_element(locator, time=2).click()

    def check_value_on_the_element(self, locator):
        search_element = self.find_element(locator, 60)
        return search_element
    
    def search_element(self, locator):
        buy_form = self.find_element(locator)
        return buy_form

    def final_screen(self):
        allure.attach(self.driver.get_full_page_screenshot_as_png(),
                      name='Finish_Screenshot',
                      attachment_type=allure.attachment_type.PNG)
