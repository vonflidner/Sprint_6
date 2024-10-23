from selenium.webdriver.common.by import By


class OrderPageLocators:
    NAME_LOCATOR = By.XPATH, "//input[@placeholder='* Имя']"
    SURNAME_LOCATOR = By.XPATH, "//input[@placeholder='* Фамилия']"
    ADDRESS_LOCATOR = By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']"
    STATION_LOCATOR = By.XPATH, "//input[@placeholder='* Станция метро']"
    LUBIANKA_STATION_LOCATOR = By.XPATH, "//button[@value='9']"
    SOKOLNIKI_STATION_LOCATOR = By.XPATH, "//button[@value='4']"
    PHONE_LOCATOR = By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']"
    NEXT_BUTTON_LOCATOR = By.XPATH, "//button[contains(text(),'Далее')]"
    DATE_LOCATOR = By.XPATH, "//input[@placeholder='* Когда привезти самокат']"
    DURATION_FIELD_LOCATOR = By.XPATH, "//div[contains(@class,'Dropdown-root')]"
    DURATION_ITEM_2_LOCATOR = By.XPATH, "//div[@class='Dropdown-menu']//div[2]"
    DURATION_ITEM_3_LOCATOR = By.XPATH, "//div[@class='Dropdown-menu']//div[3]"
    BLACK_COLOUR_LOCATOR = By.XPATH, "//label[contains(text(),'чёрный')]"
    GREY_COLOUR_LOCATOR = By.XPATH, "//label[contains(text(),'серая')]"
    COMMENT_LOCATOR = By.XPATH, "//input[@placeholder='Комментарий для курьера']"
    ORDER_BUTTON_LOCATOR = By.XPATH, "//button[contains(@class, 'Button_Middle') and contains(text(), 'Заказать')]"
    ORDER_POPUP_LOCATOR = By.XPATH, "//div[contains(@class, 'Order_Modal') and contains(text(),'оформить заказ')]"
    YES_BUTTON_LOCATOR = By.XPATH, "//button[contains(text(),'Да')]"
    SUCCESSFULLY_ORDER_LOCATOR = By.XPATH, "//div[contains(@class,'Order_ModalHeader')and contains(text(),'Заказ оформлен')]"
