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