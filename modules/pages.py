from modules.locators import Locator


class Pages():
    def __init__(self, driver):
        self.driver = driver
        self.locator = Locator()
    
    @property
    def isLoginPage(self) -> bool:
        return self.locator.login in self.driver.page_source
    
    @property
    def isMainPage(self) -> bool:
        return self.locator.main in self.driver.page_source