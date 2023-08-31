from modules.elements import Elements, Chat
from modules.pages import Pages

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

from time import sleep

class Interactor():
    def __init__ (self, driver):
        self.driver = driver
        self.elements = Elements(driver)
        self.pages = Pages(driver)
        self.actions = ActionChains(self.driver)
        
    def openProfile(self):
        sleep(0.5)
        if self.elements.profile_div != None:
            self.elements.profile_div.click()
            return True
        else:
            return False
    
    def closeProfile(self):
        while self.pages.isProfilePage:
            self.returnMain()
        return True
    
    def extractProfileData(self):
        if self.pages.isProfilePage:
            
            my_username = self.elements.username
            my_phone = self.elements.phone
            
            return my_username, my_phone
        else: return None
        
    def returnMain(self):
        try:
            sleep(0.1)
            self.actions.send_keys(Keys.ESCAPE)
            self.actions.perform()
        except: pass
        
    def searchByName(self, name):
        search_box = self.elements.search_box
        
        search_box.clear()
        search_box.send_keys(name)
        
        sleep(1)
        
        return self.elements.SearchResults

    def searchByname_and_click(self, search_input:str ):
        """_summary_

        Args:
            search_input (str): _description_

        Returns:
            (result_title, webelement)
        """
        results = self.searchByName(search_input)
        for result in results:
            if result[0] == search_input:
                result[1].click()
                return True, result
            else: return False

    def sendMessage_on_Chat(self, message:str): #add parametro chat
        #Checar se estou no chat certo
        sleep(0.5)
        input_field = self.elements.message_box

        input_field.click()
        input_field.clear()
        
        try:
            lines = message.split('\n')
            for line in lines:
                input_field.send_keys(line)  # envia cada linha
                input_field.send_keys(Keys.SHIFT, Keys.RETURN)
        except:
            input_field.send_keys(message)
        finally:
            input_field.send_keys(Keys.RETURN)

    def find_on_ChatList(self, chat_title:str): 
        for chat in self.elements.ChatList:
            if chat.title == chat_title:
                return True, chat
            else: return False, None

    def enterChat_on_ChatList(self, chat_title:str):
        exists, chat = self.find_on_ChatList(chat_title)
        if exists:
            chat.element.click()
            return True
        else: return False
