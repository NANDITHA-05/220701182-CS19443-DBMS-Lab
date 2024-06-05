import mysql.connector
class LibraryDB:
    def _init_(self, host, user, password, database):
        self.conn = mysql.connector.connect(
         host="localhost",
         user="user_name",
         password="password",
         database="library"
        )
        self.cursor = self.conn.cursor()
 def add_member(self, name, email, phone, address, join_date):
        query = "INSERT INTO members (name, email, phone, address,           
  
     join_date) VALUES (%s, %s, %s, %s, %s)"
     self.cursor.execute(query, (name, email, phone, address,join_date))
     self.conn.commit()
    def add_book(self, title, author, genre):
        query = "INSERT INTO books (title, author,  genre)
        VALUES (%s, %s, %s)"
        self.cursor.execute(query, (title, author, genre))
        self.conn.commit()
 def borrow_book(self, member_id, book_id, 
 borrow_date, return_date):
        query = "INSERT INTO borrows (member_id,
       book_id,     borrow_date, return_date) VALUES(
      %s, %s,%s,%s)"
    self.cursor.execute(query, (member_id, 
    book_id,   borrow_date,return_date))
    self.conn.commit()

    def get_books(self):
        query = "SELECT * FROM books"
         self.cursor.execute(query)
         return self.cursor.fetchall()
 def get_members(self):
        query = "SELECT * FROM members"
        self.cursor.execute(query)
        return self.cursor.fetchall()
 def close(self):
        self.cursor.close()
        self.conn.close()


