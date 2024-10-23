import allure
from data import Urls
from pages.switch_page import SwitchPage


class TestSwitchPage:

    @allure.title('Тест: Переход на главную страницу Самоката через логотип')
    @allure.description('Проверка перехода на главную страницу Самоката при клике на логотип')
    @allure.feature('Переход по логотипам')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_click_scooter_logo(self, driver):
        with allure.step('Переход на страницу заказа'):
            switch_page = SwitchPage(driver)
            switch_page.go_to_url(Urls.ORDER_PAGE_URL)

        with allure.step('Клик по логотипу Самоката'):
            switch_page.click_scooter_logo()

        with allure.step('Скролл до общего вопроса'):
            switch_page.scroll_to_general_question()

        with allure.step('Проверка, что общий вопрос отображается'):
            assert switch_page.is_general_question_displayed()

    @allure.title('Тест: Переход на главную страницу Дзена через логотип Яндекса')
    @allure.description('Проверка редиректа на главную страницу Дзена через логотип Яндекса')
    @allure.feature('Переход по логотипам')
    @allure.severity(allure.severity_level.NORMAL)
    def test_click_yandex_logo(self, driver):
        with allure.step('Переход на главную страницу'):
            switch_page = SwitchPage(driver)
            switch_page.go_to_url(Urls.MAIN_PAGE_URL)

        with allure.step('Клик по логотипу Яндекса'):
            switch_page.click_yandex_logo()

        with allure.step('Переключение на новую вкладку'):
            switch_page.switch_to_new_tab()

        with allure.step('Проверка, что главная страница Дзена отображается'):
            assert switch_page.is_dzen_page_displayed()
