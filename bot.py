
import queue
from typing import List

from time import sleep


class Gary():
    def __init__(self, session):
        self.session = session
        self.interactor = session.interactor
        
        self.queue:List = []
        # self.queue_zero = []
        
        self.newQueueMessage = "Você entrou em contato com o Serviço de Atendimento ao Cliente Ditec\nselecione uma fila:\n1 - Manutenção\n2 - Vendas"

    @property
    def queue_zero(self):
        queue = []
        for chat in self.queue:
            if chat.queue == 0:
                queue.append(chat)
        return queue
    
    @property
    def queue_one(self):
        queue = []
        for chat in self.queue:
            if chat.queue == 1:
                queue.append(chat)
        return queue


    def start(self):
        
        while True:
            self.queue = self.queueMonitor()
            
            if len(self.queue_zero) > 0:
                self.answer_newQueue()
        
    def queueMonitor(self):
        queue = []
        
        for chat in self.session.chatList:
            
            #se tiver mensagem e não tiver fila, fila = 0
            if chat.unreadCounter > 0 and chat.queue == 0:
                chat.addQueue(1)
                queue.append((chat))
                
            if chat.unreadCounter > 0 and chat.queue == 1:
                if chat.lastMessage == int(1):
                    chat.addQueue(2)  
                    input(f"{chat.title}, {chat.queue}")  
            
        return queue
        
    def answer_newQueue(self):
        
        for chat in self.queue_zero:
            self.interactor.enterChat(chat)
            self.interactor.sendMessage(self.newQueueMessage)
            self.interacotr.closeChat()
        return

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