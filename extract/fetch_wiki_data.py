import requests
from bs4 import BeautifulSoup
from load.insert_wiki_data import InsertDescription


def get_description(book_title):
    try:
        url = f"https://en.wikipedia.org/wiki/{book_title}"
        req = requests.get(url)
        soup = BeautifulSoup(req.content, "html.parser")
        desc = soup.select_one('.mw-parser-output p:nth-of-type(2)').get_text()
        print('Description : ', desc)
        print()
        InsertDescription.insert_description(desc)

    except Exception as e:
        print(f"No description found for {book_title}!")