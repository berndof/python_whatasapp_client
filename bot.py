
import csv
import os

from typing import List

from time import sleep

class Gary():
    def __init__(self, session):
        self.session = session
        self.interactor = session.interactor
        
        #self.database_path = //data//db//database.csv
        
        self.newQueueMessage = "Você entrou em contato com o Serviço de Atendimento ao Cliente Ditec\nselecione uma fila:\n1 - Manutenção\n2 - Vendas"

    def start(self):
                
        while True:
            if input("pode? ") == "":
                print(self.session._chat_list)
                
                for chat in self.session._chat_list:
                    print(chat.title, chat.unreadCounter)
            else: 
                self.session.chatsView()
            
            pass
        
