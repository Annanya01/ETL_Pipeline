import pandas as pd
from Transform import set_data
import numpy as np

def transform_data(data):
    df = pd.DataFrame.from_dict(data['items'])
    df = pd.json_normalize(data, 'items')
    df_columns = ['volumeInfo.title', 'volumeInfo.authors', 'volumeInfo.publisher', 
                    'volumeInfo.publishedDate','volumeInfo.pageCount', 'volumeInfo.categories',
                    'volumeInfo.averageRating', 'saleInfo.saleability'
                ]

    df = df[df_columns]
    df.rename(
        columns={
            'volumeInfo.title': 'title', 
            'volumeInfo.authors': 'author', 
            'volumeInfo.publisher': 'publisher',
            'volumeInfo.publishedDate': 'publishedDate',
            'volumeInfo.pageCount' : 'pageCount',
            'volumeInfo.categories' : 'category',
            'volumeInfo.averageRating' : 'averageRating',
            'saleInfo.saleability' : 'saleability',
            }, inplace=True)
            
    df['averageRating'] = df['averageRating'].replace(np.nan, 1.0)
    set_data.put_data(df)

