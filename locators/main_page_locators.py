from selenium.webdriver.common.by import By


class MainPageLocators:

    QUESTION_LOCATOR = By.XPATH, '//div[@id="accordion__heading-{}"]'
    ANSWER_LOCATOR = By.XPATH, '//div[@id="accordion__panel-{}"]'
    QUESTION_LOCATOR_8 = By.XPATH, '//div[@id="accordion__heading-7"]'

    ORDER_BUTTON_LOCATOR = By.XPATH, '//div[contains(@class,"Header_Nav")]//button[text()="Заказать"]'
    ORDER_BIG_BUTTON_LOCATOR = By.XPATH, '//div[contains(@class,"Home_FinishButton")]//button[text()="Заказать"]'