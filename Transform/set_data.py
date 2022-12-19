
from load.insert_data import InsertData

def put_publishers(df):
    print('Publisher : ', df['publisher'][0])
    InsertData.insert_publishers(df['publisher'][0])

def put_books(df):
    print('Page Count : ',df['pageCount'][0] )
    print('Average Rating : ', df['averageRating'][0])
    
    InsertData.insert_books(df['title'][0], df['pageCount'][0], df['saleability'][0] ,df['averageRating'][0] )

def put_authors(df):
    for author in df['author'][0]:
        print('Author name : ', author)
        InsertData.insert_authors(author)
        put_book_authors()

def put_category(df):
    for category in df['category'][0]:
        print('Category : ', category)
        InsertData.insert_categories(category)
        put_book_categories()

def put_book_authors():
    InsertData.insert_book_authors()

def put_book_categories():
    InsertData.insert_book_categories()

def put_data(df):
    put_publishers(df)
    put_authors(df)
    put_books(df)
    put_category(df)







