import allure
from selenium.common import NoSuchElementException

from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage


class MainPage(BasePage):

    @allure.step('Получаем текст элемента')
    def get_answer_text(self, num):
        locator_q_formatted = self.format_locators(MainPageLocators.QUESTION_LOCATOR, num)
        locator_a_formatted = self.format_locators(MainPageLocators.ANSWER_LOCATOR, num)
        locator_8_formatted = MainPageLocators.QUESTION_LOCATOR_8
        self.scroll_to_element(locator_8_formatted)
        self.click_to_element(locator_q_formatted)
        return self.get_text_from_element(locator_a_formatted)
