from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from modules.pages import Pages
from modules.utils import generate_qr

from time import sleep

class Session():
    def __init__(self, driver):
        self.driver = driver
        
        
        self.elements = Elements(self.driver)
        self.pages = Pages(self.driver)
        
        self.my_profile:Profile
        
    def start(self) -> bool:
        """Inicia a sessão

        Returns:
            bool: sessão iniciada com sucesso >>> True
        """
        waitqrscan, actual_qr_data = generate_qr(qr_data=self.elements.qr_data)
        
        while not is_auth:
            if self.pages.isMainPage:
                is_auth = True
                break

            if self.pages.isLoginPage:
                is_auth = self.waitqrscan()
                break

            else:
                continue
            
        input("checar meu perfil")
        return True
                
                
        input("calma")
            
        
        input("faça login")
        
    def waitqrscan(self) -> bool:
        return True
    
    
        
class Profile():
    def __init__(self, username, phone, photo_url, chat_element):
        
        self.username:str = username
        self.phone:str = phone
        self.photo_url:str = photo_url
        self.chat_element:str = chat_element
        