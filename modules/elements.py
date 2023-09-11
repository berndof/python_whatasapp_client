#### IMPORTS
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from typing import Tuple, Union, List, Literal
from selenium.webdriver.remote.webelement import WebElement

from modules import utils

from time import sleep

##################################################################################################


## Queue 0 fila esperando fila (esperando setor especifico)
##     - queue_state 0 (enviar mensagem de boas vindas), primeiro contato first_contact
##     - queue_state 1 (mensagem de boas vindas enviada), aguardando resposta waiting
##     - queue_state 2 (mensagem de boas vindas respondida), encaminhando para a fila especifica redirecting
##     - queue state 3 (mensagem de boas vindas respondida errado), reenviar mensagem queue_state = 1 resend_greetings



class Chat():
    def __eq__(self, outro_chat):
        return self.title == outro_chat.title
    
    def __init__(self, title, time_lastMessage, lastMessage, unreadCounter,  element, queue = 0, queue_state = 0):
        
        self.title = title
        self.time_lastMessage = time_lastMessage
        self.lastMessage = lastMessage
        self.unreadCounter = int(unreadCounter)
        self.element = element
        self.queue = queue
        self.queue_state = queue_state
        self.messages = []
        
######## QUEUE #######

    # [Ready]
    @property
    def waitingQueue(self) -> bool:
        if self.queue == 0:
            return True
        else: return False
        
    # [Ready]
    def addQueue(self, queue:int) -> Literal[True]:
        self.queue = queue
        return True

######## PROPERTIES ########
    # [Ready]
    @property
    def isPinned(self) -> bool:
        try:
            self.element.find_element(By.XPATH, './/*[@data-icon="pinned2"]')
            return True 
        except: return False


class Elements():
    def __init__(self,driver):
        
        self.driver = driver 
        self.utils = utils
        
        self.current_chats = []
    
####### QRCODE #######
    
    # [Ready]
    @property
    def qr_data(self) -> str:
        try:
            return self.driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[3]/div[1]/div/div/div[2]/div').get_attribute('data-ref')
        except: return ""
        
####### PROFILE #######
        
    # [Ready]
    @property    
    def profile_div(self) -> Union[WebElement, None]:
        try: 
            return self.driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[4]/header/div[1]/div')
        except: return None
        
    # [Ready]    
    @property
    def username(self) -> Union[str, None]:   
        try:
            div = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div/div[3]/div[1]/span/div/span/div/div/div[2]/div[1]/div[1]/div[2]/div/div[1]'))) 
            content = div.get_attribute('innerHTML')
            return content
        except Exception as e: return None
            #!TODO tratar exceção

    # [Ready]
    @property
    def phone(self) -> Union[str, None]:
        try:
            div = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div/div[3]/div[1]/span/div/span/div/div/div[2]/div[3]/div[3]/div[2]/div/div[1]')))
            content = div.get_attribute('innerHTML')
            return content
        except Exception as e: return None
        
####### SEARCH #######
    
    # [Ready]
    @property
    def search_box(self) -> WebElement:
        return self.driver.find_element(By.XPATH, '//*[@title="Caixa de texto de pesquisa"]')
    
    # [Ready]
    @property    
    def SearchResults(self) -> List[Tuple[str, WebElement]]:

        container = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '[aria-label="Resultados da pesquisa."]')))
        list_resultElements = container.find_elements(By.XPATH, './*')
        
        if len(list_resultElements) < 2:
            print("nenhum resultado")
            input("#erro nenhum resultado")
        else:
        #set start y position
            for element in list_resultElements:
                if element.text == "CONTATOS" or element.text == "CONVERSAS":
                    y_start = element.location['y']
                if element.text == "MENSAGENS": #Y_end
                    y_end = element.location['y']
                    pass
                    #y_end = element.location['y']
                #!TODO set y end position for search in messages or limit the search results only to contacts
        
        search_results = self.utils.organize_search_results(list_resultElements, y_start, y_end)
        return search_results  

    # [Ready]
    @property
    def message_box(self):
        try: return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/div/div/div[5]/div/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]')))
        except: return None

######## CHATS #######

    # [Not Ready] TODO
    @property
    def chats(self) -> List[Chat]:
        
        
        chat_tab = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '[aria-label="Lista de conversas"]')))

        for chat_element in chat_tab.find_elements(By. XPATH, './*'):
            
            #chat_data = chat_element.text.split('\n')
            #chat_title, time_lastMessage, lastMessage, unreadCounter = chat_data
            
            if chat_element.text.split('\n')[0] == "Ditec": #TODO SABE QUE ISSO TA ERRA NÉ?
                chat_title, x, time_lastMessage, lastMessage  = chat_element.text.split('\n')
                unreadCounter=0
                chat_object = Chat(chat_title, time_lastMessage, lastMessage, unreadCounter, chat_element)
                
            else:
                if len(chat_element.text.split('\n')) == 3:
                    
                    unreadCounter=0
                    chat_title, time_lastMessage, lastMessage = chat_element.text.split('\n')
                    chat_object = Chat(chat_title, time_lastMessage, lastMessage, unreadCounter, chat_element)
                
                else: 
                    chat_title, time_lastMessage, lastMessage, unreadCounter = chat_element.text.split('\n')
                    chat_object = Chat(chat_title, time_lastMessage, lastMessage, unreadCounter, chat_element)
            
            
            
            
            
            existing_chat = next((chat for chat in self.current_chats if chat.title == chat_title), None)
            if existing_chat:
                existing_chat.time_last_message = time_lastMessage
                existing_chat.last_message = lastMessage
                existing_chat.unread_counter = unreadCounter
            else:
                chat_object = Chat(chat_title, time_lastMessage, lastMessage, unreadCounter, chat_element)
                self.current_chats.append(chat_object)

        return self.current_chats
            
      
        """if chat_element.text.split('\n')[0] == "Ditec": #TODO SABE QUE ISSO TA ERRA NÉ?
                #meu chat
                #return self.myChat
                chat_title, x, time_lastMessage, lastMessage  = chat_element.text.split('\n')
                chat_object = Chat(chat_title, time_lastMessage, lastMessage, "0", chat_element)
                
            else:
                
                if len(chat_element.text.split('\n')) == 3:
                    chat_title, time_lastMessage, lastMessage = chat_element.text.split('\n')
                    chat_object = Chat(chat_title, time_lastMessage, lastMessage, 0, chat_element)
                
                else: 
                    chat_title, time_lastMessage, lastMessage, unreadCounter = chat_element.text.split('\n')
                    chat_object = Chat(chat_title, time_lastMessage, lastMessage, unreadCounter, chat_element)
            
            
            current_chat_list.append(chat_object)
        
        return current_chat_list"""
    