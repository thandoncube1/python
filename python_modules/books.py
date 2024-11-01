from connections.mysql_database import *

class Book:
    def __init__(self, title: str, author: str):
        self.title = title,
        self.author = author,
        self.cur = connection.cursor()

    def create_table(self, name: str) -> None:
        query = f"CREATE TABLE {name}(isbn TEXT PRIMARY KEY, title TEXT, author TEXT)"""
        print(query)
        self.cur.execute(query)

    def insert_row(self, isbn: str, title: str, author: str, table: str) -> None:
        query = f"INSERT INTO {table} VALUES ('{isbn}', '{title}', '{author}')"
        print(query)
        self.cur.execute(query)

    def find_one(self, column: str, table: str, title: str) -> list[str]:
        query = f"SELECT {column} FROM {table} WHERE {column} = '{title}' LIMIT 1"
        result = self.cur.execute(query)
        return result.fetchall()

    def find(self, column: str, title: str, table: str) -> list:
        query = f"SELECT * FROM {table} WHERE {column} LIKE '%{title}%'"
        result = self.cur.execute(query)
        return result.fetchall()

    def select_all(self, table: str) -> list[str]:
        query = f"SELECT * FROM {table}"
        result = self.cur.execute(query)
        return result.fetchall()

    def save_data(self) -> None:
        self.cur.connection.commit()

    def __str__(self):
        return f"{self.title} Author: ({self.author}) \
    Database connection: {connection}"

book = Book('Oliver Twist', 'Charles Dickens')
# book.create_table("shelf")
# ------- New Rows ---------
# book.insert_row("978-0-13-652023-8", "The Alchemist", "Paulo Coelho", "shelf")
# book.insert_row("978-1-13-652024-9", "Oliver Twist", "Charles Dickens", "shelf")
# book.insert_row("918-12-9-472032-9", "Hackers And Painters", "Paul Graham", "shelf")
# book.insert_row("213-10-13-438927-1", "Learn Ruby Programming", "Mitsuyo Maida", "shelf")
# -------- Save the data ---------
# book.save_data()
print(book.find_one("title", "shelf", "Hackers And Painters"))
print(book.select_all("shelf"))
print(book.find("title", "hackers", "shelf"))