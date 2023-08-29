from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from modules.utils import generate_qr

from modules.pages import Pages
from modules.elements import Elements
from modules.interactions import Interactor

from typing import Tuple

from time import sleep

class Session(Elements, Interactor):
    def __init__(self, driver):
        #super().__init__(driver)
        Elements.__init__(self, driver)
        Interactor.__init__(self, driver)
        
        self.driver = driver
        
        
        #self.elements = Elements(self.driver)
        self.pages = Pages(self.driver)
        self.actual_qr_data:str = ''
        
        self.my_profile:Profile
        
    def start(self) -> bool:
        """Inicia a sessão

        Returns:
            bool: sessão iniciada com sucesso >>> True
        """
        
        is_auth = False
        
        while not is_auth:
            if self.pages.isMainPage:
                is_auth = True
                break
            if self.pages.isLoginPage:
                self.actual_qr_data = self.waiting_scan()
                continue
            else:
                continue
        
        while self.pages.isMainPage:
            self.build_my_profile()
        
        return True
                
    def waiting_scan(self) -> Tuple[str, bool]:
        if self.qr_data != self.actual_qr_data and self.actual_qr_data != '':
            return generate_qr(qr_data=self.qr_data)
        return self.qr_data
                
    
    def build_my_profile(self):
        if self.openProfile():
            my_username = self.extractProfileData()
            input(f"{my_username}")
            
            
class Profile():
    def __init__(self, username, phone, photo_url, chat_element):
        
        self.username:str = username
        self.phone:str = phone
        self.photo_url:str = photo_url
        self.chat_element:str = chat_element
        