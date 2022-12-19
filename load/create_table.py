
class CreateTable:
    @staticmethod
    def create_table_books():
        command = '''CREATE TABLE books(
            id              SERIAL PRIMARY KEY,
            publisher_id    INT,
            title           TEXT,
            page_count      INT,
            average_rating  NUMERIC DEFAULT 1.0,
            sale_ability    VARCHAR(20),

            FOREIGN KEY (publisher_id) REFERENCES publishers(id)
            );'''

        return command

    @staticmethod
    def create_table_publishers():
        command = '''CREATE TABLE publishers(
                    id              SERIAL PRIMARY KEY,
                    publisher_name  VARCHAR(100) NOT NULL
                  );'''

        return command

    @staticmethod
    def create_table_authors():
        command = '''CREATE TABLE authors(
                    id      SERIAL PRIMARY KEY,
                    name    VARCHAR(30)
                    );'''

        return command

    @staticmethod
    def create_table_categories():
        command = '''CREATE TABLE categories(
            id          SERIAL PRIMARY KEY,
            category    VARCHAR(30)
            );'''

        return command

    @staticmethod
    def create_table_book_authors():
        command = '''CREATE TABLE book_authors(
                    id          SERIAL PRIMARY KEY,
                    book_id     INT,
                    author_id   INT,
                    FOREIGN KEY (book_id) REFERENCES books(id),
                    FOREIGN KEY (author_id) REFERENCES authors(id)
                    );'''

        return command
    
    @staticmethod
    def create_table_book_categories():
        command = '''CREATE TABLE book_categories(
                    id          SERIAL PRIMARY KEY,
                    book_id     INT,
                    category_id INT,
                    FOREIGN KEY (book_id) REFERENCES books(id),
                    FOREIGN KEY (category_id) REFERENCES categories(id)
                    );'''

        return command

    @staticmethod
    def create_table_description():
        command = '''CREATE TABLE description(
                    id          SERIAL PRIMARY KEY,
                    description TEXT,
                    book_id     INT,
                    FOREIGN KEY (book_id) REFERENCES books(id)
                    );
                '''

        return command


def create_tables():
    yield CreateTable.create_table_publishers()
    yield CreateTable.create_table_books()
    yield CreateTable.create_table_authors()
    yield CreateTable.create_table_categories()
    yield CreateTable.create_table_book_authors()
    yield CreateTable.create_table_book_categories()
    yield CreateTable.create_table_description()



