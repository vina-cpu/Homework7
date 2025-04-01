import sys
import qrcode
from dotenv import load_dotenv
import os
import logging
import argparse
from pathlib import Path
from datetime import datetime
import validators

load_dotenv()
QR_DIR = os.getenv('QR_DIR', 'qrcodes')
FILL = os.getenv('FILL_COLOR', 'white')
BACK = os.getenv('BACK_COLOR', 'black')
URL = os.getenv('URL', 'https://github.com/vina-cpu/Homework7')

#configuring logging to be printing out ?
def configure_logging():
    logging.basicConfig(
        level="INFO",
        format='%(asctime)s %(levelname)s %(message)s',
        datefmt="%m-%d-%Y %H:%M:%S",
        handlers=[logging.StreamHandler(sys.stdout)]
    )
    logging.info("Logging configured")

def configure_parser():
    #just separating the parser from the main b/c it was getting crowded in there
    parser = argparse.ArgumentParser(description = 'Provide a url to make a QR code')
    parser.add_argument('--url', help = 'The URL to make the QR code with', default = URL)
    logging.info('Parser configured')
    return parser

def make_file_path():
    time = datetime.now().strftime("%m.%d.%H.%M")
    logging.info("File path made")
    return Path.cwd() / QR_DIR / f"qr_code_{time}.png"

def make_directory():
    logging.info("Directory made or checked")
    os.makedirs(QR_DIR, exist_ok = True)

def check_url(url):
    if not validators.url(url):
        raise ValueError(f"Invalid URL: {url}")

def make_qr(url, path, fill, back):    
    try:
        check_url(url)
        making_qr = qrcode.QRCode(version = 1, box_size = 10, border = 3)
        making_qr.add_data(url)
        making_qr.make(fit = True)
        image = making_qr.make_image(fill_color = fill, back_color = back)
        
        with path.open('wb') as my_qr_image:
            image.save(my_qr_image)
    except Exception as e:
        logging.error(f"An error occured. Could not generate or save the qr code: {e}")

def main():
    configure_logging()
    args = configure_parser().parse_args()
    filepath = make_file_path()
    make_directory()
    make_qr(args.url, filepath, FILL, BACK)

if __name__ == "__main__":
    main()