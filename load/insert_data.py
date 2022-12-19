from load.connection import Database

class InsertData:
    @staticmethod
    def create_connection(sql):
        db_obj = Database()
        db_obj.connect()
        db_obj.insert_rows(sql)

    @staticmethod
    def insert_publishers(publishers):
        sql = f"""INSERT INTO publishers(publisher_name)
                     VALUES('{publishers}');"""

        InsertData.create_connection(sql)

    @staticmethod
    def insert_books(title, pageCount, saleability, averageRating = 1.0):
        publisher_id = get_publisher_id()
        sql = f"""INSERT INTO books(publisher_id, title, page_count, average_rating, sale_ability )
                         VALUES({publisher_id}, '{title}', {int(pageCount)},  {averageRating} ,'{saleability}');"""
        InsertData.create_connection(sql)

    @staticmethod
    def insert_authors(author):
        sql = f"""INSERT INTO authors(name)
                VALUES('{author}');"""
        InsertData.create_connection(sql)

    @staticmethod
    def insert_categories(category):
        sql = f"""INSERT INTO categories(category)
                VALUES( '{category}');"""
        InsertData.create_connection(sql)

    @staticmethod
    def insert_book_authors():
        book_id = get_book_id()
        author_id = get_author_id()
        sql = f"""INSERT INTO book_authors(book_id, author_id)
                VALUES( {book_id}, {author_id});"""
        InsertData.create_connection(sql)

    @staticmethod
    def insert_book_categories():
        book_id = get_book_id()
        category_id = get_category_id()

        sql = f"""INSERT INTO book_categories(book_id, category_id)
                VALUES( {book_id}, {category_id});"""
        InsertData.create_connection(sql)

def get_id(sql):
    db_obj = Database()
    db_obj.connect()
    cur = db_obj.conn.cursor()
    cur.execute(sql)
    id = cur.fetchone()
    db_obj.conn.commit()
    cur.close()
    return id

def get_publisher_id():
    sql = f"""SELECT MAX(id) FROM publishers;"""
    publisher_id = get_id(sql)
    return publisher_id[0]

def get_book_id():
    sql = f"""SELECT MAX(id) FROM books;"""
    book_id = get_id(sql)
    return book_id[0]

def get_category_id():
    sql = f"""SELECT MAX(id) FROM categories;"""
    category_id = get_id(sql)
    return category_id[0]

def get_author_id():
    sql = f"""SELECT MAX(id) FROM authors;"""
    author_id = get_id(sql)
    return author_id[0]



