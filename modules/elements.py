from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from typing import Tuple

from modules import utils

from time import sleep

class Elements():
    def __init__(self,driver):
        self.driver = driver 
        self.utils = utils
        
    @property
    def qr_data(self) -> str:
        try:
            return self.driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[3]/div[1]/div/div/div[2]/div').get_attribute('data-ref')
        except: return ""
        
    @property    
    def profile_div(self):
        """find profile div on web page

        Returns:
            WebElement or None
        """
        
        try: 
            return self.driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[4]/header/div[1]/div')
        except: return None
        
    @property
    def username(self) -> Tuple[str,None]:
        """
        InnerHtml da div do nome de usuário

        Returns:
            Tuple[str, None]: username, exception
        """
        try:
            div = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div/div[3]/div[1]/span/div/span/div/div/div[2]/div[1]/div[1]/div[2]/div/div[1]'))) 
            content = div.get_attribute('innerHTML')
            return content
        except Exception as e: return None
            #!TODO tratar exceção

    @property
    def phone(self) -> Tuple[str, None]:
        """
        InnerHtml da div de telefone do usuário

        Returns:
            Tuple[str, None]: phone, exception
        """ 
        try:
            div = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div/div[3]/div[1]/span/div/span/div/div/div[2]/div[3]/div[3]/div[2]/div/div[1]')))
            content = div.get_attribute('innerHTML')
            return content
        except Exception as e: return None
        
    @property
    def search_box(self):
        return self.driver.find_element(By.XPATH, '//*[@title="Caixa de texto de pesquisa"]')
        
    @property    
    def SearchResults(self):

        container = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '[aria-label="Resultados da pesquisa."]')))
        list_resultElements = container.find_elements(By.XPATH, './*')
        
        if len(list_resultElements) < 2:
            print("nenhum resultado")
            input("#erro nenhum resultado")
        else:
        #set start y position
            for element in list_resultElements:
                if element.text == "CONVERSAS":
                    y_start = element.location['y']
                if element.text == "MENSAGENS": #Y_end
                    pass
                    #y_end = element.location['y']
                #!TODO set y end position for search in messages or limit the search results only to contacts
        
        search_results = self.utils.organize_search_results(list_resultElements, y_start)
        return search_results  

    @property
    def message_box(self):
        try: return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/div/div/div[5]/div/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]')))
        except: return None
        
    @property
    def ChatList(self):
        current_chat_list = []
        
        chats_tab = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '[aria-label="Lista de conversas"]')))


        for chat_element in chats_tab.find_elements(By. XPATH, './*'):
            
            chat_title = utils.break_chat_text(chat_element.text)
            
            chat_object = Chat(chat_title, chat_element)
            
            current_chat_list.append(chat_object)
        
        return current_chat_list
        

class Chat():
    def __init__(self, title, element):
        self.title = title
        self.element = element
        
    @property
    def isPinned(self) -> bool:
        try:
            self.element.find_element(By.XPATH, './/*[@data-testid="pinned2"]')
            return True
        except: return False