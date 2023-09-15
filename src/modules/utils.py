import qrcode
import os
from time import sleep

# [X] Ready
def check_path(path:str):
    if not os.path.exists(path):
        os.makedirs(path)
        return True
    else: return True

# [X] Ready
def generate_qr(qr_data:str='', qr_path:str='data//session//', qr_filename:str='qr-code.png'):
    
    qr = qrcode.QRCode() # type: ignore
    
    qr.add_data(qr_data)
    qr.make(fit=True)
    
    qr_image = qr.make_image(fill_color='black', back_color='white')
    
    check_path(qr_path)
    
    qr_fullname = qr_path + qr_filename
    qr_image.save(qr_fullname)
    
    return qr_data

# [W] TODO add y_end (height of div "Mensagens") 
def organize_search_results(list_resultElements, y_start, y_end):
    result_list = []      
    for element in list_resultElements:
        if y_start < int(element.location['y']) and y_end == 0:
            result_title = break_chat_text(element.text)
            
            result_list.append((result_title, element))
        
        if  y_start < int(element.location['y']) and y_end > int(element.location['y']):
            
            result_title = break_chat_text(element.text)
            
            result_list.append((result_title, element))
    return result_list

# [W] TODO
def break_chat_text(chat_text:str):
    #TODO dar uma olhada nisso aqui
    chat_data = chat_text.split('\n') 
    chat_title = chat_data[0]
    #print(chat_data)
    #input("analise bobo")
    
    #last_message_time = chat_data[1]
    #last_message = chat_data[2]
    
    #!TODO dar uma olhada nisso aq 
    #if len(chat_data) > 3:
    #    unread_messages = chat_data[3]
    #else: unread_messages = '0' 
    #aaaaaaaaaaaaaaaaaaaaaaaaaaa
    #
    # TODO retornar chat_data e quebrar depois
    return (chat_title)
