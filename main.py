from selenium.webdriver.chrome.options import Options
from selenium import webdriver

import threading

from time import sleep

from session import Session
from bot import Gary


class App(Session):
    def __init__(self, driver):
        super().__init__(driver)
        
        self.last_chatList_Cheked = []
        #self.gary = Gary(self)
        
        if self.start():
            self.run() 
        
        
    def run(self):
        self.gary = Gary(self)
        self.gary.start()


        
if __name__ == "__main__":
    
    chrome_options = Options()
    chrome_options.binary_location = '//usr//bin//google-chrome' 
    
    profile_path = "data//browser//"    
    chrome_options.add_argument(f"user-data-dir={profile_path}")
    
    chrome_options.add_argument("--lang=pt-BR")

    driver = webdriver.Chrome(options=chrome_options)

    driver.get('https://web.whatsapp.com')

    app = App(driver)
    