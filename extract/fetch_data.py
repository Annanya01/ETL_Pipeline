
import pandas as pd
import requests
import sys
from Transform.preprocessing import transform_data

sys.path.insert(0, '/Users/annanya/code/ETL_Pipeline/TRansform/')

def get_data(book_title):
    try:
        response_API = requests.get(f'https://www.googleapis.com/books/v1/volumes?q={book_title}')
        data = response_API.json()
        transform_data(data)
        
    except Exception as error:
        print(error)