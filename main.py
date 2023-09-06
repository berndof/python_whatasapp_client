from selenium.webdriver.chrome.options import Options
from selenium import webdriver

import threading

from time import sleep

from session import Session


class App(Session):
    def __init__(self, driver):
        super().__init__(driver)
        
        self.stop_checking_messages = False
        self.thread_check_messages = threading.Thread(target=self.check_new_messages)
        self.thread_check_messages.daemon = True

        self.last_chatList_Cheked = []
        self.cli()
        
                
    def cli(self):
        
        if self.start():
            self.thread_check_messages.start()

            while True:
                self.stop_checking_messages = False
                option = input ("Oque deseja: ")
                
                if option == "profile":
                    self.stop_checking_messages = True
                    print(self.my_profile.username, self.my_profile.phone)
                    continue
                    
                if option == "lista":
                    print(self.a)
                    continue
                    
                if option == "teste1":
                    self.check_new_chat()
                    print(self.queue)
                    continue               
                
                if option == "teste2":
                    self.answer_queue()
                    continue     
                
                
                if option == "quit":
                    self.stop_checking_messages = True
                    print("saindo")
                    break
                
    def check_new_messages(self):
        self.a = 0
        
        while not self.stop_checking_messages:  # Continue executando enquanto a variável não for True
            # Coloque aqui a lógica para verificar novas mensagens
            self.a = 1 + self.a
            
            # Se houver novas mensagens, faça algo aqui
            sleep(1)  # Aguarde um segundo entre as verificações
        pass

        
if __name__ == "__main__":
    
    chrome_options = Options()
    chrome_options.binary_location = '//usr//bin//google-chrome' 
    
    profile_path = "data//browser//"    
    chrome_options.add_argument(f"user-data-dir={profile_path}")
    
    chrome_options.add_argument("--lang=pt-BR")

    driver = webdriver.Chrome(options=chrome_options)

    driver.get('https://web.whatsapp.com')

    app = App(driver)
    