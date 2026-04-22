'''
Esse arquivo tem a utilidade somente de teste de execução local para verificar o funcionamento das funções e do pipeline, antes de orquestrar de forma automática 
'''

from src.extract_data import extract_weather_data
from src.transform_data import data_transformations 
from src.load_data import load_weather_data 

from pathlib import Path
from dotenv import load_dotenv

import os 
import logging
import traceback

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s') 

env_path = Path(__file__).resolve().parent.parent / 'config' / '.env'
load_dotenv(env_path) 

API_KEY = os.getenv("API_KEY")

url = f'https://api.openweathermap.org/data/2.5/weather?q=Brasilia,BR&units=metric&appid={API_KEY}'

table_name = 'bsb_weather'

def pipeline(): 
    try: 
        logging.info("Iniciando Extração...")
        extract_weather_data(url)

        logging.info("Iniciando Transformação")
        df = data_transformations()

        logging.info("Iniciando carregamento")
        load_weather_data(table_name, df)

        print("Pipeline finalizada com sucesso")

    except Exception as e: 
        logging.error(f"Erro gerado no pipeline: {e}")
        traceback.print_exc()

pipeline()