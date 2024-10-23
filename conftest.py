import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from locators.order_page_locators import OrderPageLocators


@pytest.fixture(scope="function")
def driver():
    service = Service(GeckoDriverManager().install())
    driver = webdriver.Firefox(service=service)
    yield driver
    driver.quit()


# @pytest.fixture(params=[
#     (OrderPageLocators.LUBIANKA_STATION_LOCATOR, OrderPageLocators.DURATION_ITEM_2_LOCATOR, OrderPageLocators.BLACK_COLOUR_LOCATOR),
#     (OrderPageLocators.SOKOLNIKI_STATION_LOCATOR, OrderPageLocators.DURATION_ITEM_3_LOCATOR, OrderPageLocators.GREY_COLOUR_LOCATOR)
# ], scope='function')
# def order_parameters(request):
#     return request.param
