from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def go_to_url(self, url):
        self.driver.get(url)

    def find_element_with_wait(self, locator):
        WebDriverWait(self.driver, 40).until(
            EC.visibility_of_element_located(locator)
        )
        return self.driver.find_element(*locator)

    def click_to_element(self, locator):
        WebDriverWait(self.driver, 40).until(
            EC.element_to_be_clickable(locator)
        )
        self.driver.find_element(*locator).click()

    def add_text_to_element(self, locator, text):
        element = self.find_element_with_wait(locator).send_keys(text)

    def get_text_from_element(self, locator):
        return self.find_element_with_wait(locator).text

    def scroll_to_element(self, locator):
        element = self.find_element_with_wait(locator)
        WebDriverWait(self.driver, 40).until(EC.visibility_of(element))
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)

    def format_locators(self, locator_1, num):
        method, locator = locator_1 # '//*[@class="my-question-locator-{}"]'
        locator = locator.format(num) # '//*[@class="my-question-locator-1"]'
        return method, locator
