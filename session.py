from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from modules.utils import generate_qr

from modules.pages import Pages
from modules.elements import Elements
from modules.interactions import Interactor

from typing import Tuple

from time import sleep

class Session(Elements, Pages):
    def __init__(self, driver):
        #super().__init__(driver)
        Elements.__init__(self, driver)
        Pages.__init__(self, driver)
        
        self.driver = driver
        
        self.interactor = Interactor(self.driver)    
        #self.elements = Elements(self.driver)
        #self.pages = Pages(self.driver)
        
    
        
        self.actual_qr_data:str = ''
        
        self.my_profile:Profile
        
    def start(self) -> bool:
        """Inicia a sessão

        Returns:
            bool: sessão iniciada com sucesso >>> True
        """
        
        is_auth = False
        
        while not is_auth:
            if self.isMainPage:
                is_auth = True
                break
            if self.isLoginPage:
                self.actual_qr_data = self.waiting_scan()
                continue
            else:
                continue
        
        if not self.isProfilePage:
            self.build_my_profile()
        return True
                
    def waiting_scan(self) -> Tuple[str, bool]:
        if self.qr_data != self.actual_qr_data and self.actual_qr_data != '':
            return generate_qr(qr_data=self.qr_data)
        return self.qr_data
                
    def build_my_profile(self):
        if self.interactor.openProfile():
            my_username, my_phone = self.interactor.extractProfileData()
            self.interactor.closeProfile()
        self.my_profile = Profile(self, my_username, my_phone)
        return True
            
            
class Profile():
    def __init__(self, session, username, phone):
        
        self.username:str = username
        self.phone:str = phone
        self.session = session
        self.interactor = self.session.interactor
        
        self.test_message = "Hello, world"
        
        self.hello_world()
        
    def hello_world(self):
        if self.interactor.searchByname_and_click(self.username)[0]:
            #AQUI
            
            #TODO Checar se o nome do chat bate com o nome da pesquisa
            
            # [x] logica para enviar a mensagem 
            self.interactor.sendMessage_on_Chat(self.test_message)
                
            #TODO verificar se a mensagem esta na conversa
            
            while not self.session.isMainPage:
                self.interactor.returnMain()
                sleep(0.1)
            
            
            
            #Achar meu chat na lista de chats

            self.interactor.enterChat_on_ChatList(self.username)
            input("caca")
            
            # fixar meu contato
        
            
            # retornar
        
        #self.photo_url:str = photo_url
        #self.chat_element:str = chat_element
        