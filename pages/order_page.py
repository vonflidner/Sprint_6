import allure
from selenium.common import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from locators.order_page_locators import OrderPageLocators
from helper import generate_name, generate_surname, generate_phone, generate_address, generate_date, generate_comment
from pages.base_page import BasePage


class OrderPage(BasePage):

    @allure.step('Создаем заказ')
    def set_order(self, station_locator, duration_locator, color_locator):
        with allure.step("Ввод имени"):
            self.add_text_to_element(OrderPageLocators.NAME_LOCATOR, generate_name())
        with allure.step("Ввод фамилии"):
            self.add_text_to_element(OrderPageLocators.SURNAME_LOCATOR, generate_surname())
        with allure.step("Ввод телефона"):
            self.add_text_to_element(OrderPageLocators.PHONE_LOCATOR, generate_phone())
        with allure.step("Ввод адреса"):
            self.add_text_to_element(OrderPageLocators.ADDRESS_LOCATOR, generate_address())
        with allure.step("Выбор станции"):
            self.click_to_element(OrderPageLocators.STATION_LOCATOR)
            self.click_to_element(station_locator)
        with allure.step("Переход на следующий шаг"):
            self.click_to_element(OrderPageLocators.NEXT_BUTTON_LOCATOR)
        with allure.step("Ввод даты аренды"):
            self.add_text_to_element(OrderPageLocators.DATE_LOCATOR, generate_date())
            self.driver.find_element(*OrderPageLocators.DATE_LOCATOR).send_keys(Keys.ENTER)
        with allure.step("Выбор продолжительности аренды"):
            self.click_to_element(OrderPageLocators.DURATION_FIELD_LOCATOR)
            self.click_to_element(duration_locator)
        with allure.step("Выбор цвета самоката"):
            self.click_to_element(color_locator)
        with allure.step("Ввод комментария"):
            self.add_text_to_element(OrderPageLocators.COMMENT_LOCATOR, generate_comment())
        with allure.step("Подтверждение заказа"):
            self.click_to_element(OrderPageLocators.ORDER_BUTTON_LOCATOR)
            self.find_element_with_wait(OrderPageLocators.ORDER_POPUP_LOCATOR)
            self.click_to_element(OrderPageLocators.YES_BUTTON_LOCATOR)

    @allure.step('Проверяем, что заказ создался')
    def check_order(self, locator):
        try:
            element = self.driver.find_element(*locator)
            return element.is_displayed()
        except NoSuchElementException:
            return False


