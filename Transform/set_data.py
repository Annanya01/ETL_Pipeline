
from load.insert_data import InsertData

def put_books(df):
    print('Page Count : ',df['pageCount'][0] )
    print('Average Rating : ', df['averageRating'][0])
    print('Publisher : ', df['publisher'][0])
    InsertData.insert_books(df['title'][0], df['publisher'][0], int(df['pageCount'][0]), df['saleability'][0] ,df['averageRating'][0] )

def put_authors(df):
    print('Author name : ')
    for author in df['author'][0]:
        print( author, sep=',')
        InsertData.insert_authors(author)
        put_book_authors()

def put_category(df):
    try:
        for category in df['category'][0]:
            print('Category : ', category)
            InsertData.insert_categories(category)
            put_book_categories()
    except:
        print('No category found!')

def put_book_authors():
    InsertData.insert_book_authors()

def put_book_categories():
    InsertData.insert_book_categories()

def put_data(df):
    put_books(df)
    put_authors(df)
    put_category(df)







