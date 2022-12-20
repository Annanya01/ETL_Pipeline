from load.insert_data import InsertData, get_book_id

class InsertDescription : 

    @staticmethod
    def insert_description(description):
        book_id = get_book_id()
        sql = f"""INSERT INTO description(book_id, description)
                VALUES({book_id}, '{description}');"""
        InsertData.create_connection(sql)
