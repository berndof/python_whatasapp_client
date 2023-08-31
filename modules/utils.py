import qrcode
import os
from time import sleep

def check_path(path:str):
    if not os.path.exists(path):
        os.makedirs(path)
        return True
    else: return True

def generate_qr(qr_data:str='', qr_path:str='data//session//', qr_filename:str='qr-code.png'):
    
    qr = qrcode.QRCode()
    
    qr.add_data(qr_data)
    qr.make(fit=True)
    
    qr_image = qr.make_image(fill_color='black', back_color='white')
    
    check_path(qr_path)
    
    qr_fullname = qr_path + qr_filename
    qr_image.save(qr_fullname)
    
    return qr_data

def organize_search_results(list_resultElements, y_start):
    result_list = []      
    for element in list_resultElements:
        if  y_start < int(element.location['y']):
            
            result_title = break_chat_text(element.text)
            
            result_list.append((result_title, element))
    return result_list

def break_chat_text(chat_text:str):
    #TODO dar uma olhada nisso aqui
    chat_data = chat_text.split('\n') 
    chat_title = chat_data[0]
    
    #last_message_time = chat_data[1]
    #last_message = chat_data[2]
    
    #!TODO dar uma olhada nisso aq 
    #if len(chat_data) > 3:
    #    unread_messages = chat_data[3]
    #else: unread_messages = '0' 
     
    return (chat_title)
