import csv
import os
import string

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from typing import Tuple, Union, List, Literal
from selenium.webdriver.remote.webelement import WebElement

class Chat():
    def __eq__ (self, other_chat):
        if type(other_chat) == str:
            return self.title == other_chat
        if type(other_chat) == Chat:
            return self.title == other_chat.title
    
    def __init__(self, title, unreadCounter, lastMessage, time_lastMessage, queue):
        
        self.title:str = title
        self.unreadCounter:int = int(unreadCounter)
        self.lastMessage:str = lastMessage
        self.time_lastMessage:str = time_lastMessage
        
        self.queue = queue
        
        self.message_history = []
        
        #chat.addMessage_to_hist(chat.lastMessage)
        
    def addMessage_to_hist(self, message, time):
        
        self.message_history.append((message, time))

        return
    
class Chats():
    def __init__(self, driver, interactor):
        self.driver = driver
        self.interactor = interactor

        self.chatList = []

    def chatsView(self):
        for chat in self.chatList:
            print(f"{chat.title} , {chat.lastMessage}\n {chat.message_history}")
            input("proximo chat ")
        return

    @property
    def firstContact_queue(self):
        resposta = []
        for chat in self.chatList:
            if chat.queue == "firstContact":
                resposta.append(chat)
            return resposta

    @property
    def _update_chatList(self):
        
        for element in self._elements_list:
            
            #extração dos dados 
            chat_data =  self._extract_chat_data(element)
            title, unreadCounter, time_lastMessage, lastMessage  = chat_data

            if title == "Ditec":
                queue = "my_chat"
            
            if title == "Tecnico":
                queue = "tech_chat"
                
            else: queue = "firstContact"

            #Primeira colocada
            if title not in self.chatList and int(unreadCounter) > 0:
                chat = Chat(title, unreadCounter, time_lastMessage, lastMessage, queue)
                self.chatList.append(chat)
            else:
                self._update_chat(chat_data)

        return self.chatList
    
    def _update_chat(self, chat_data):
        
        title, unreadCounter, time_lastMessage, lastMessage  = chat_data
        
        
        for chat in self.chatList:
            
            if chat == title:
                if chat.unreadCounter != unreadCounter:
                    chat.unreadCounter = unreadCounter
                    
                elif chat.lastMessage != lastMessage:
                    chat.addMessage_to_hist(lastMessage, time_lastMessage)
                    chat.lastMessage = lastMessage
                    
                elif chat.time_lastMessage != time_lastMessage:
                    chat.time_lastMessage = time_lastMessage
                    
        return
        
    def _extract_chat_data(self, element):
        
        """
        Args:
            element: elemento web do chat

        Returns: title:str > [0], unread_counter:str > [1], time_last_message:str > [2], last_message:str > [3]
        """
        
        chat_data = element.text.split("\n")
        
        title = chat_data[0]
        time_last_message = chat_data[2]
        last_message = chat_data[1]
        
        if len(chat_data) == 3 or title == "Ditec": #TODO 
            unread_counter = 0
        else:
            unread_counter = chat_data[3]
        
        return title, unread_counter, time_last_message, last_message
        
    @property
    def _elements_list(self):
        
        elements = []


        chat_tab = self.driver.find_element(By.CSS_SELECTOR, '[aria-label="Lista de conversas"]')


        for chat_element in chat_tab.find_elements(By. XPATH, './*'):
            
            chat_data = chat_element.text.split("\n")
            
            #if chat_data[0] != 'Ditec' and chat_data[2] != 'digitando...':
            #    elements.append(chat_element)
            
            if chat_data[2] != 'digitando...':
                elements.append(chat_element)
            else: pass
        
        return elements