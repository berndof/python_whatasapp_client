from unittest.util import _count_diff_all_purpose
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.remote.webelement import WebElement

from modules.elements import Elements
from modules.pages import Pages

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

from time import sleep

from typing import Union

class Interactor():
    def __init__ (self, session):
        self.session = session
        self.elements = self.session.elements
        self.driver = self.session.driver
    
        self.action = ActionChains(self.driver)
        
        
######## PROFILE ########
    # [Ready]
    def openProfile(self) -> bool:
        #sleep(0.5)
        profile_div = self.elements.profile_div

        if profile_div.is_enabled() and profile_div.is_displayed():
            profile_div.click()
            return True
        else:
            return False
    
    # [Ready]
    def closeProfile(self):
        """while self.pages.isProfilePage:
            try:
                #sleep(0.1)
                self.action.send_keys(Keys.ESCAPE)
                self.action.perform()
            except: pass
        return True"""
        
        self.action.send_keys(Keys.ESCAPE)
        self.action.perform()
    
    # [Ready]
    def extractProfileData(self):
        if self.session.isProfilePage:
            
            my_username = self.elements.username
            my_phone = self.elements.phone
            
            return my_username, my_phone
        else: return "", ""

######## NAVIGATION ########
    # [X] Ready
    def returnMain(self):
        while not self.session.isMainPage:
            try:
                sleep(0.1)
                self.action.send_keys(Keys.ESCAPE)
                self.action.perform()
            except: pass
        return True
    
    # [X] Ready
    def closeChat(self):
        sleep(0.1)
        self.action.send_keys(Keys.ESCAPE)
        self.action.perform()
        
    # [X] Ready
    def openChat(self, chat):
        try:
            chat.click()
            return True
        except: return False

######## SEARCH ######## TODO
    
    # [X] Ready 
    def searchByTitle(self, chat_title:str):
        search_box = self.elements.search_box
        
        search_box.clear()
        search_box.send_keys(chat_title)
        
        sleep(1)
        
        return self.elements.SearchResults

    # [W] TODO 
    def searchByTitle_then_click(self, chat_title:str):
        results = self.searchByTitle(chat_title)        
        for title, element in results:
            if title == chat_title:
                element.click()
                #confirmar que entrou no chat certo
                return True
            else: return False

######## CHATS ######## TODO

    # [W] TODO
    def sendMessage(self, message:str): #add parametro chat
        #Checar se estou no chat certo
        
        sleep(0.2)
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

    # [X] Ready
    def pinChat(self, chat) -> bool:
        if not chat.isPinned:
            self.action.context_click(chat.element).perform()
            sleep(1)
            
            context_box = WebDriverWait(self.driver, 1).until(EC.presence_of_element_located((By.CSS_SELECTOR, '[class="_3bcLp"]')))
        
            sleep(0.5)
            pin_btn = context_box.find_element(By.XPATH, './/*[@aria-label="Fixar conversa"]')
            pin_btn.click()
            return True
        else: return True