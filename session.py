import queue
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from modules.utils import generate_qr

from modules.pages import Pages
from modules.elements import Elements, Chat
#from bot import Bot
from modules.interactions import Interactor

from typing import Tuple, List, Union

from time import sleep

class Session(Elements, Pages):
    def __init__(self, driver):
        #super().__init__(driver)
        Elements.__init__(self, driver)
        Pages.__init__(self, driver)
        
        self.driver = driver
        
        #self.bot = Bot
        
        self.interactor = Interactor(self.driver)    
        #self.elements = Elements(self.driver)
        #self.pages = Pages(self.driver)
        
        self.actual_qr_data:str = ''
        self.current_chat_list = []
        
        self.my_profile:Profile
        self.chat_list = ChatList(self)
    
        
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
        
        #if not self.isProfilePage:
        self.build_my_profile()
        
        # [W] Depois de buildar o meu perfil, vou fazer a primeira checagem dos chats
        self.current_chat_list = self.chatList
        
        return True
                
    # [X] Ready
    def waiting_scan(self) -> Tuple[str, bool]:
        if self.qr_data != self.actual_qr_data and self.actual_qr_data != '':
            return generate_qr(qr_data=self.qr_data)
        return self.qr_data
                
    # [X] Ready
    def build_my_profile(self):
        if self.interactor.openProfile():
            my_username, my_phone = self.interactor.extractProfileData()
            self.interactor.closeProfile()
        self.my_profile = Profile(self, my_username, my_phone)
        return True
        
class ChatList():
    def __init__(self, session):
        
        self.session = session
        
        self.chat_list = []
        
    @property
    def actual_list(self):
        
        for element in self.session.chats:
            input(element.text.slipt("\n")[0])
        
        pass
        

        

class Profile():
    def __init__(self, session, username, phone,):
        
        self.session = session
        self.interactor = self.session.interactor
        
        self.username:str = username
        self.phone:str = phone
        
        self.hello_world()
        self.pinMyChat()
        
    #### Properties ###############################
    @property        
    def webElement(self):
        return self.interactor.searchByTitle_on_chatList(self.username)
        
    ###############################################
    
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
        