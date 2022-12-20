from extract import fetch_data, fetch_wiki_data
import pandas as pd

class InputData:

    @staticmethod
    def read_csv():
        try:
            input_data = pd.read_csv('input.csv')
            for index, row in input_data.iterrows():
                book_title = row[0]
                print()
                print('Book Title : ', book_title)
                fetch_data.get_api_data(book_title)
                fetch_wiki_data.get_description(book_title)

        except:
            print("Can not find path of file")