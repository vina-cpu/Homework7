import sys
import os
import logging
import argparse
from dotenv import load_dotenv
from datetime import datetime
from pathlib import Path
#configuring logging to be printing out ?

load_dotenv()
QR_DIR = os.getenv('QR_DIR', 'qrcodes')
URL = os.getenv('URL', 'https://github.com/vina-cpu/Homework7')

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