# src/utils.py
import logging
import os

def setup_logging(log_file='app.log'):
    logging.basicConfig(
        filename=log_file,
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    logger = logging.getLogger(__name__)
    return logger

def clean_string(s):
    return s.strip().replace('\n', '').replace('\r', '')

def read_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as file:
        return file.read()

def write_file(filepath, content):
    with open(filepath, 'w', encoding='utf-8') as file:
        file.write(content)

def ensure_dir(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)