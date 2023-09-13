#### IMPORTS
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from typing import Tuple, Union, List, Literal
from selenium.webdriver.remote.webelement import WebElement

from modules import utils

from time import sleep



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

            for element in list_resultElements:
                if element.text == "CONTATOS" or element.text == "CONVERSAS":
                    y_start = element.location['y']
                if element.text == "MENSAGENS": #Y_end
                    y_end = element.location['y']

        
        search_results = self.utils.organize_search_results(list_resultElements, y_start, y_end)
        return search_results  

######## MESSAGES ########
    # [Ready]
    @property
    def message_box(self):
        try: return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/div/div/div[5]/div/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]')))
        except: return None
