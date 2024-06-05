import tkinter as tk
from tkinter import messagebox
from library_db import LibraryDB

class LibraryApp:
    def __init__(self, root):
        self.db = LibraryDB('localhost', 'user_name', 'password', 'library')

        self.root = root
        self.root.title("Library Management System")
        self.root.configure(bg="#f0f0f0")

        self.create_widgets()

    def create_widgets(self):
        frame = tk.Frame(self.root, bg="#f0f0f0", padx=20, pady=20)
        frame.pack(padx=10, pady=10)

        tk.Button(frame, text="Add Member", command=self.add_member_window, bg="#4CAF50", fg="white").grid(row=0, column=0, pady=10, padx=10, sticky="ew")
        tk.Button(frame, text="Add Book", command=self.add_book_window, bg="#2196F3", fg="white").grid(row=1, column=0, pady=10, padx=10, sticky="ew")
        tk.Button(frame, text="Borrow Book", command=self.borrow_book_window, bg="#FF9800", fg="white").grid(row=2, column=0, pady=10, padx=10, sticky="ew")
        tk.Button(frame, text="View Books", command=self.view_books, bg="#9C27B0", fg="white").grid(row=3, column=0, pady=10, padx=10, sticky="ew")
        tk.Button(frame, text="View Members", command=self.view_members, bg="#E91E63", fg="white").grid(row=4, column=0, pady=10, padx=10, sticky="ew")

    def add_member_window(self):
        self.new_window = tk.Toplevel(self.root)
        self.app = AddMemberWindow(self.new_window, self.db)

    def add_book_window(self):
        self.new_window = tk.Toplevel(self.root)
        self.app = AddBookWindow(self.new_window, self.db)

    def borrow_book_window(self):
        self.new_window = tk.Toplevel(self.root)
        self.app = BorrowBookWindow(self.new_window, self.db)

    def view_books(self):
        books = self.db.get_books()
        for book in books:
            print(book)

    def view_members(self):
        members = self.db.get_members()
        for member in members:
            print(member)

class AddMemberWindow:
    def __init__(self, root, db):
        self.db = db
        self.root = root
        self.root.title("Add Member")
        self.root.configure(bg="#f0f0f0")

        self.create_widgets()

    def create_widgets(self):
        frame = tk.Frame(self.root, bg="#f0f0f0", padx=20, pady=20)
        frame.pack(padx=10, pady=10)

        tk.Label(frame, text="Name", bg="#f0f0f0").grid(row=0, column=0, pady=5, padx=5, sticky="e")
        self.name_entry = tk.Entry(frame)
        self.name_entry.grid(row=0, column=1, pady=5, padx=5, sticky="ew")

        tk.Label(frame, text="Email", bg="#f0f0f0").grid(row=1, column=0, pady=5, padx=5, sticky="e")
        self.email_entry = tk.Entry(frame)
        self.email_entry.grid(row=1, column=1, pady=5, padx=5, sticky="ew")

        tk.Label(frame, text="Phone", bg="#f0f0f0").grid(row=2, column=0, pady=5, padx=5, sticky="e")
        self.phone_entry = tk.Entry(frame)
        self.phone_entry.grid(row=2, column=1, pady=5, padx=5, sticky="ew")

        tk.Label(frame, text="Address", bg="#f0f0f0").grid(row=3, column=0, pady=5, padx=5, sticky="e")
        self.address_entry = tk.Entry(frame)
        self.address_entry.grid(row=3, column=1, pady=5, padx=5, sticky="ew")

        tk.Label(frame, text="Join Date (YYYY-MM-DD)", bg="#f0f0f0").grid(row=4, column=0, pady=5, padx=5, sticky="e")
        self.join_date_entry = tk.Entry(frame)
        self.join_date_entry.grid(row=4, column=1, pady=5, padx=5, sticky="ew")

        tk.Button(frame, text="Add", command=self.add_member, bg="#4CAF50", fg="white").grid(row=5, column=0, columnspan=2, pady=10, padx=5, sticky="ew")

    def add_member(self):
        name = self.name_entry.get()
        email = self.email_entry.get()
        phone = self.phone_entry.get()
        address = self.address_entry.get()
        join_date = self.join_date_entry.get()

        self.db.add_member(name, email, phone, address, join_date)
        messagebox.showinfo("Success", "Member added successfully!")
        self.root.destroy()

class AddBookWindow:
    def __init__(self, root, db):
        self.db = db
        self.root = root
        self.root.title("Add Book")
        self.root.configure(bg="#f0f0f0")

        self.create_widgets()

    def create_widgets(self):
        frame = tk.Frame(self.root, bg="#f0f0f0", padx=20, pady=20)
        frame.pack(padx=10, pady=10)

        tk.Label(frame, text="Title", bg="#f0f0f0").grid(row=0, column=0, pady=5, padx=5, sticky="e")
        self.title_entry = tk.Entry(frame)
        self.title_entry.grid(row=0, column=1, pady=5, padx=5, sticky="ew")

        tk.Label(frame, text="Author", bg="#f0f0f0").grid(row=1, column=0, pady=5, padx=5, sticky="e")
        self.author_entry = tk.Entry(frame)
        self.author_entry.grid(row=1, column=1, pady=5, padx=5, sticky="ew")

        tk.Label(frame, text="Genre", bg="#f0f0f0").grid(row=2, column=0, pady=5, padx=5, sticky="e")
        self.genre_entry = tk.Entry(frame)
        self.genre_entry.grid(row=2, column=1, pady=5, padx=5, sticky="ew")

        tk.Button(frame, text="Add", command=self.add_book, bg="#2196F3", fg="white").grid(row=3, column=0, columnspan=2, pady=10, padx=5, sticky="ew")

    def add_book(self):
        title = self.title_entry.get()
        author = self.author_entry.get()
        genre = self.genre_entry.get()

        self.db.add_book(title, author, genre)
        messagebox.showinfo("Success", "Book added successfully!")
        self.root.destroy()

class BorrowBookWindow:
    def __init__(self, root, db):
        self.db = db
        self.root = root
        self.root.title("Borrow Book")
        self.root.configure(bg="#f0f0f0")

        self.create_widgets()

    def create_widgets(self):
        frame = tk.Frame(self.root, bg="#f0f0f0", padx=20, pady=20)
        frame.pack(padx=10, pady=10)

        tk.Label(frame, text="Member ID", bg="#f0f0f0").grid(row=0, column=0, pady=5, padx=5, sticky="e")
        self.member_id_entry = tk.Entry(frame)
        self.member_id_entry.grid(row=0, column=1, pady=5, padx=5, sticky="ew")

        tk.Label(frame, text="Book ID", bg="#f0f0f0").grid(row=1, column=0, pady=5, padx=5, sticky="e")
        self.book_id_entry = tk.Entry(frame)
        self.book_id_entry.grid(row=1, column=1, pady=5, padx=5, sticky="ew")

        tk.Label(frame, text="Borrow Date (YYYY-MM-DD)", bg="#f0f0f0").grid(row=2, column=0, pady=5, padx=5, sticky="e")
        self.borrow_date_entry = tk.Entry(frame)
        self.borrow_date_entry.grid(row=2, column=1, pady=5, padx=5, sticky="ew")

        tk.Label(frame, text="Return Date (YYYY-MM-DD)", bg="#f0f0f0").grid(row=3, column=0, pady=5, padx=5, sticky="e")
        self.return_date_entry = tk.Entry(frame)
        self.return_date_entry.grid(row=3, column=1, pady=5, padx=5, sticky="ew")

        tk.Button(frame, text="Borrow", command=self.borrow_book, bg="#FF9800", fg="white").grid(row=4, column=0, columnspan=2, pady=10, padx=5, sticky="ew")

    def borrow_book(self):
        member_id = self.member_id_entry.get()
        book_id = self.book_id_entry.get()
        borrow_date = self.borrow_date_entry.get()
        return_date = self.return_date_entry.get()

        self.db.borrow_book(member_id, book_id, borrow_date, return_date)
        messagebox.showinfo("Success", "Book borrowed successfully!")
        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = LibraryApp(root)
    root.mainloop()
