import os
import qrcode
import logging
import validators
from dotenv import load_dotenv

load_dotenv()
FILL = os.getenv('FILL_COLOR', 'white')
BACK = os.getenv('BACK_COLOR', 'black')

def check_url(url):
    if not validators.url(url):
        raise ValueError(f"Invalid URL: {url}")

def make_qr(url, path):    
    try:
        check_url(url)
        making_qr = qrcode.QRCode(version = 1, box_size = 10, border = 3)
        making_qr.add_data(url)
        making_qr.make(fit = True)
        image = making_qr.make_image(fill_color = FILL, back_color = BACK)
        
        with path.open('wb') as my_qr_image:
            image.save(my_qr_image)
        logging.info("QR code made")
        logging.info(f"QR code saved to {path.parent.name}/{path.stem}")
    except Exception as e:
        logging.error(f"An error occured. Could not generate or save the qr code: {e}")