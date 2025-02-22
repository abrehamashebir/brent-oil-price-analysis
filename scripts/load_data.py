import pandas as pd
import logging

logging.basicConfig(
    level=logging.INFO
)

def load(file_path):
    
    try:
        df = pd.read_csv(file_path)
        logging.info(f'{file_path} loaded')
    except Exception as e:
        logging.error('File not found')
    
    return df