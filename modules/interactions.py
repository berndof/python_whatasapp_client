from modules.elements import Elements
from modules.pages import Pages

class Interactor():
    def __init__ (self, driver):
        self.driver = driver
        self.elements = Elements(driver)
        self.pages = Pages(driver)
        
    def openProfile(self):
        if self.elements.profile_div != None:
            self.elements.profile_div.click()
            return True
        else:
            return False
    
    def extractProfileData(self):
        if self.pages.isProfilePage:
            my_username = self.elements.username
            return my_username
        else: return None