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
        #ChatList.__init__(self)
        
        self.driver = driver
        
        #self.bot = Bot
        
        self.interactor = Interactor(self.driver)    
        #self.elements = Elements(self.driver)
        #self.pages = Pages(self.driver)
        
        self.actual_qr_data:str = ''
        self.current_chat_list = []
        
        #self.my_profile:Profile
        #self.chat_list = ChatList(self)
    
        
    def start(self) -> bool:
        input("logado?")
        
        while True:
            op = input("> ")
            if op == "chat":
                print(self.chats)
                
            if op == "quit":
                break
    
