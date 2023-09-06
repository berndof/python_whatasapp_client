
from typing import List

from time import sleep


class Gary():
    def __init__(self, session):
        self.session = session
        self.interactor = session.interactor
        self.queue:List = []

    def start(self):
        while True:
            self.queueMonitor()
            
            if self.messageMonitor():
                self.answerQueue()
                
            
            
    def encaminhar(self):
        self.interactor.searchByTitle_then_click("Tecnico")
            #AQUI
            
        self.interactor.sendMessage(self.mensagemAencaminhar)
        self.mensagemAencaminhar = ''
            
            #verificar se a mensagem esta na conversa

        self.interactor.returnMain()
                
    def answerQueue(self):
        queue_message = """
        Você entrou em contato com Serviço de Atendimento ao Cliente da Ditec\nDigite um número para escolher uma fila:\n1 - Manutenção
        """
        
        for chat in self.queue:
            if chat.title != "Ditec" and chat.title != "Tecnico" and chat.unreadCounter > 0:
                self.interactor.enterChat(chat)
                self.interactor.sendMessage(queue_message)
                sleep(5) # TODO espera cinco segundos e checa se o usuário já respondeu, se não vai para o próximo chat TALVEZ
                self.interactor.exitChat()
        #self.interactor.automatic_answer(self.queue)
        return
    
    def queueMonitor(self):
        queue = []

        for chat in self.session.chatList:
            if chat.unreadCounter >= 0:
                
                self.mensagemAencaminhar = (f"{chat.title},  {chat.lastMessage}")
                
                queue.append(chat)
                
            self.queue = queue
            
    def messageMonitor(self):
        if len(self.queue) > 0:
            print(self.queue, len(self.queue))            
            return True    
        else: return False