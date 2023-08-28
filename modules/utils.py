def generate_qr(qr_data:str='', qr_path:str='data//session//', qr_filename:str='qr-code.png'):
    
    if qr_data =='':
        return False, qr_data
    
    qr = qrcode.QRCode()
    qr.add_data(qr_data)
    qr.make(fit=True)
    qr_image = qr.make_image(fill_color='black', back_color='white')
    check_path(qr_path)
    qr_fullname = qr_path + qr_filename
    qr_image.save(qr_fullname)
    return True, qr_data