from selenium.webdriver.chrome.options import Options
from selenium import webdriver


from session import Session

class App(Session):
    def __init__(self, driver):
        super().__init__(driver)
        
        if self.start():
            while True:
                option = input ("Oque deseja: ")
                
                if option == "profile":
                    print(self.my_profile.username, self.my_profile.phone)
                
                if option == "quit":
                    print("saindo")
                    break

if __name__ == "__main__":
    
    chrome_options = Options()
    chrome_options.binary_location = '//usr//bin//google-chrome' 
    
    profile_path = "data//browser//"    
    chrome_options.add_argument(f"user-data-dir={profile_path}")
    
    chrome_options.add_argument("--lang=pt-BR")

    driver = webdriver.Chrome(options=chrome_options)

    driver.get('https://web.whatsapp.com')

    app = App(driver)
    