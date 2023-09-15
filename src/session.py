from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from modules.utils import generate_qr

from modules.pages import Pages
from modules.elements import Elements
from modules.interactions import Interactor
from modules.chats import Chats, Chat

from typing import Tuple, List, Union

from time import sleep

class Session (Pages):
    def __init__(self, driver):

        self.driver = driver
        self.elements = Elements(self.driver)
        self.interactor = Interactor(self)
        self.chats = Chats(self.driver, self.interactor)
        #Elements.__init__(self, self.driver)
        
        Pages.__init__(self, self.driver)
        #Chats.__init__(self, self.driver, self.interactor)
                
        self.actual_qr_data:str = ''
        
        self.my_profile:Profile
    
    # [XW] Almost Ready but working on
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
                self.actual_qr_data = self._update_qr_data()
                continue
            else:
                continue
        
        #TODO if not self.isProfilePage:
        self._build_my_profile()
        
        return True

######## QRCODE ########
    # [X] Ready
    def _update_qr_data(self) -> str:
        if self.elements.qr_data != self.actual_qr_data and self.actual_qr_data != '':
            return generate_qr(qr_data=self.elements.qr_data)
        return self.elements.qr_data
                
######## MY PROFILE ########
    # [X] Ready
    def _build_my_profile(self):
        #sleep(1)
        if self.interactor.openProfile():
            my_username, my_phone = self.interactor.extractProfileData()        
            self.interactor.closeProfile()
            self.my_profile = Profile(self, my_username, my_phone)
            return True
        else: input("aconteceu algo estranho, vá olhar e resolver")

class Profile():
    def __init__(self, session, username, phone,):
        
        self.session = session
        self.interactor = self.session.interactor
        
        self.username:str = username
        self.phone:str = phone
        
        #self.my_chat TODO
        
        self.hello_world()
        self.pinMyChat()
        
#### Properties ###############################
    @property        
    def webElement(self):
        if self.username in self.session.chatList:
            #indice = self.session.chatList.index(self.username)
            return self.session.chatList[self.session.chatList.index(self.username)]
            
#### Actions ##################################
    
    # [W] TODO
    def hello_world(self):
        if self.interactor.searchByTitle_then_click(self.username):
            #AQUI
            
            self.interactor.sendMessage("Hello, world!")
            
            #verificar se a mensagem esta na conversa

            self.interactor.returnMain()
            return True
    
    def pinMyChat(self):
        try:
            self.interactor.pinChat(self.webElement)
        except: pass
        
        return True
            #input("vai tratar exceção burro!")
        
            #Achar meu chat na lista de chats

            
            # fixar meu contato
        
            
            # retornar
        
        #self.photo_url:str = photo_url
        #self.chat_element:str = chat_element
        