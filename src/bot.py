
from typing import List

from time import sleep

class Gary():
    def __init__(self, session):
        #self.session = session
        self.interactor = session.interactor
        self.chats = session.chats
        
        #self.database_path = //data//db//database.csv
        
        self.newQueueMessage = "Você entrou em contato com o Serviço de Atendimento ao Cliente Ditec\nselecione uma fila:\n1 - Manutenção\n2 - Vendas"

    def start(self):
                
        while True:
            self.chats._update_chatList
            
            self.answerQueues(self.chats.chatList)
            #if len(self.chats.firstContact_queue) > 0:
            input(f"{self.chats.chatList}")
            
            pass
    
    def answerQueues(self, chat_list):
        ##AQUI 
        pass