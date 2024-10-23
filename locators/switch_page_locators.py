from selenium.webdriver.common.by import By


class SwitchPageLocators:
    DZEN_PAGE_LOCATOR = By.XPATH, "//a[@data-testid='logo']"
    SCOOTER_LOGO_LOCATOR = By.XPATH, "//a[contains(@class,'Header_LogoScooter')]"
    YANDEX_LOGO_LOCATOR = By.XPATH, "//a[contains(@class,'Header_Logo') and contains(@href,'//yandex.ru')]"
    GENERAL_QUESTION_LOCATOR = By.XPATH, '//div[contains(@class,"Home_Sub") and contains(text(),"Вопросы о важном")]'