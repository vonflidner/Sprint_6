import allure
import pytest
from locators.main_page_locators import MainPageLocators
from pages.main_page import MainPage
from pages.order_page import OrderPage
from locators.order_page_locators import OrderPageLocators
from data import Urls


class TestScooterOrder:

    @allure.title("Тест заказа самоката через верхнюю кнопку")
    @pytest.mark.parametrize("order_parameters", [
        (OrderPageLocators.LUBIANKA_STATION_LOCATOR, OrderPageLocators.DURATION_ITEM_2_LOCATOR,
         OrderPageLocators.BLACK_COLOUR_LOCATOR)
    ])
    def test_order_scooter_top_button(self, driver, order_parameters):
        with allure.step("Переход на главную страницу"):
            main_page = MainPage(driver)
            main_page.go_to_url(Urls.MAIN_PAGE_URL)

        with allure.step("Нажатие на кнопку заказа"):
            main_page.click_to_element(MainPageLocators.ORDER_BUTTON_LOCATOR)

        with allure.step("Переход на страницу заказа"):
            order_page = OrderPage(driver)

        with allure.step("Заполнение формы заказа"):
            station_locator, duration_locator, color_locator = order_parameters
            order_page.set_order(station_locator, duration_locator, color_locator)

        with allure.step("Проверка успешного создания заказа"):
            assert order_page.check_order(OrderPageLocators.SUCCESSFULLY_ORDER_LOCATOR)

    @allure.title("Тест заказа самоката через нижнюю кнопку")
    @pytest.mark.parametrize("order_parameters", [
        (OrderPageLocators.SOKOLNIKI_STATION_LOCATOR, OrderPageLocators.DURATION_ITEM_3_LOCATOR,
         OrderPageLocators.GREY_COLOUR_LOCATOR)
    ])
    def test_order_scooter_bottom_button(self, driver, order_parameters):
        with allure.step("Переход на главную страницу"):
            main_page = MainPage(driver)
            main_page.go_to_url(Urls.MAIN_PAGE_URL)

        with allure.step("Прокрутка страницы до кнопки заказа"):
            main_page.scroll_to_element(MainPageLocators.ORDER_BIG_BUTTON_LOCATOR)

        with allure.step("Нажатие на большую кнопку заказа"):
            main_page.click_to_element(MainPageLocators.ORDER_BIG_BUTTON_LOCATOR)

        with allure.step("Переход на страницу заказа"):
            order_page = OrderPage(driver)

        with allure.step("Заполнение формы заказа"):
            station_locator, duration_locator, color_locator = order_parameters
            order_page.set_order(station_locator, duration_locator, color_locator)

        with allure.step("Проверка успешного создания заказа"):
            assert order_page.check_order(OrderPageLocators.SUCCESSFULLY_ORDER_LOCATOR)
