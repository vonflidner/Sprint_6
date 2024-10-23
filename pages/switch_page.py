from locators.switch_page_locators import SwitchPageLocators
from pages.base_page import BasePage


class SwitchPage(BasePage):

    def click_scooter_logo(self):
        self.click_to_element(SwitchPageLocators.SCOOTER_LOGO_LOCATOR)

    def click_yandex_logo(self):
        self.click_to_element(SwitchPageLocators.YANDEX_LOGO_LOCATOR)

    def switch_to_new_tab(self):
        self.driver.switch_to.window(self.driver.window_handles[-1])

    def is_general_question_displayed(self):
        return self.find_element_with_wait(SwitchPageLocators.GENERAL_QUESTION_LOCATOR).is_displayed()

    def scroll_to_general_question(self):
        self.scroll_to_element(SwitchPageLocators.GENERAL_QUESTION_LOCATOR)

    def is_dzen_page_displayed(self):
        return self.find_element_with_wait(SwitchPageLocators.DZEN_PAGE_LOCATOR).is_displayed()
