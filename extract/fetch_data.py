import requests
from Transform.preprocessing import transform_data
import json

def get_data(book_title):
    try:
        with open(f"book_data/{book_title}.json","r") as openfile:
            json_object = json.load(openfile)
        transform_data(json_object)

    except Exception as error:
        print(error)

def get_api_data(book_title):
    try:
        params = {'q' : book_title}
        response = requests.get(f'https://www.googleapis.com/books/v1/volumes',params = params)
        data = response.json()
        data1 = json.dumps(data)
        file = open(f"book_data/{book_title}.json","w")
        file.write(data1)
        get_data(book_title)
        file.close()

    except Exception as error:
        print(error)



