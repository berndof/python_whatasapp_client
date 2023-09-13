import queue
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from modules.utils import generate_qr

from modules.pages import Pages
from modules.elements import Elements
from modules.chats import Chats

from modules.interactions import Interactor

from typing import Tuple, List, Union

from time import sleep

    
class Session(Elements, Pages, Chats):
    def __init__(self, driver):
        self.driver = driver
        
        self.interactor = Interactor(self.driver)    

        Elements.__init__(self, self.driver)
        Pages.__init__(self, self.driver)
        Chats.__init__(self, self.driver, self.interactor)
        
        self.actual_qr_data:str = ''
        self.current_chat_list = []
        
    def start(self) -> bool:
        input("logado?")
        
        return True
    
