from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from typing import Tuple

from time import sleep

class Elements():
    def __init__(self,driver):
        self.driver = driver 
    
    @property
    def qr_data(self) -> str:
        try:
            return self.driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[3]/div[1]/div/div/div[2]/div').get_attribute('data-ref')
        except: return ""
        
    @property    
    def profile_div(self):
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
        sleep(3)
        try:
            div = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(By.XPATH,'/html/body/div[1]/div/div/div[3]/div[1]/span/div/span/div/div/div[2]/div[1]/div[1]/div[2]/div/div[1]'))
            
            content = div.get_attribue("innerHTML")
            return content
        except: return None
        
    @property
    def phone_div(self) -> Tuple[str, None]:
        """
        InnerHtml da div de telefone do usuário

        Returns:
            Tuple[str, None]: phone, exception
        """
        pass
        return 