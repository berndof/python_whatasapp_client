from modules.elements import Elements, Chat
from modules.pages import Pages

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

from time import sleep

class Interactor(Profile):
    def __init__ (self, driver):
        self.driver = driver
        self.elements = Elements(driver)
        self.pages = Pages(driver)
        self.action = ActionChains(self.driver)
        
        
    ### PROFILE ########################################
    # [X] Ready
    def openProfile(self) -> bool:
        sleep(0.5)
        if self.elements.profile_div != None:
            self.elements.profile_div.click()
            return True
        else:
            return False
    
    # [X] Ready
    def closeProfile(self):
        while self.pages.isProfilePage:
            self.returnMain()
        return True
    
    # [\] Ready for now, extrair mais dados perfil
    def extractProfileData(self):
        if self.pages.isProfilePage:
            
            my_username = self.elements.username
            my_phone = self.elements.phone
            
            return my_username, my_phone
        else: return None
    ####################################################
    
    ### ACTIONS ########################################
    # [X] Ready
    def returnMain(self):
        while not self.pages.isMainPage:
            try:
                sleep(0.1)
                self.actions.send_keys(Keys.ESCAPE)
                self.actions.perform()
            except: pass
        return True
        
    ####################################################    
        
        
    ### Search ######################################### 
    
    # [X] Ready 
    def searchByTitle(self, chat_title):
        search_box = self.elements.search_box
        
        search_box.clear()
        search_box.send_keys(chat_title)
        
        sleep(1)
        
        return self.elements.SearchResults

    # [W] TODO 
    def searchByTitle_then_click(self, chat_title ):

        results = self.searchByName(chat_title)
        
        for title, element in results:
            if title == chat_title:
                element.click()
                #confirmar que entrou no chat certo
                return True
            else: return False

    # [W] TODO
    def sendMessage(self, message:str): #add parametro chat
        #Checar se estou no chat certo
        
        sleep(0.5)
        input_field = self.elements.message_box

        input_field.click()
        input_field.clear()
        
        try:
            lines = message.split('\n')
            for line in lines:
                input_field.send_keys(line)  # envia cada linha
                input_field.send_keys(Keys.SHIFT, Keys.RETURN)
        except:
            input_field.send_keys(message)
        finally:
            input_field.send_keys(Keys.RETURN)

    def find_on_ChatList(self, chat_title:str): 
        for chat in self.elements.ChatList:
            if chat.title == chat_title:
                return chat
            else: return None

    # [x] Ready for now, adicionar confirmação de que entrou no chat certo antes de retornar
    def enterChat(self, chat:Chat()):
        try:
            chat.element.click()
            return True
        except: return False

    def enterChat_on_ChatList(self, chat_title:str):
        exists, chat = self.find_on_ChatList(chat_title)
        if exists:
            chat.element.click()
            return True
        else: return False
    
    def pinChat_on_ChatList(self, chat_title:str):
        exists, chat = self.find_on_ChatList(chat_title)
        if exists and chat.element.is_displayed() and not self.chat.isPinned:
            #pin chat
            return True
        else: return False
    
    def pinChat(self, chat:Chat):
        if not chat.isPinned:
            self.actions.context_click(chat.element).perform()
            
            context_box = self.element
    