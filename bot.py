
from typing import List

from time import sleep


class Gary():
    def __init__(self, session):
        self.session = session
        self.interactor = session.interactor
        self.queue:List = []

    def start(self):
        
        
        while True:
            temMensagem, comprimento = self.MessageWatcher()
            sleep(1)
            if temMensagem:
                aEncaminhar = self.answer_queue()
                sleep(0.5)
                self.encaminhar()
            
            
    def encaminhar(self):
        self.interactor.searchByTitle_then_click("Tecnico")
            #AQUI
            
        self.interactor.sendMessage(self.mensagemAencaminhar)
        self.mensagemAencaminhar = ''
            
            #verificar se a mensagem esta na conversa

        self.interactor.returnMain()
                
    def answer_queue(self):
        self.interactor.automatic_answer(self.queue)
        return
    
    def MessageWatcher(self):
        queue = []
        while True:
            for chat in self.session.chatList:
                if chat.unreadCounter > 0:
                    self.mensagemAencaminhar = (f"{chat.title},  {chat.lastMessage}")
                    queue.append(chat)
            self.queue = queue
            if len(self.queue) > 0:
                #print(self.queue)
                return True, len(self.queue)
            else: return False, 0