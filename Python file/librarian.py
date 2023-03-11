import tkinter as tk
from tkinter import ttk
import psycopg2
from tkinter import messagebox


class AdminPage(tk.Frame):
    def __init__(self, master, switch_frame):
        super().__init__(master)
        self.switch_frame = switch_frame

        self.label = tk.Label(self, text='Admin page')
        self.label.grid(row=0, column=0)

        self.search_var = tk.StringVar()

        self.book_entry = tk.Entry(self, textvariable=self.search_var, width=50)
        self.book_entry.grid(row=1, column=0, columnspan=2)
        self.book_entry.bind('<KeyRelease>', self.search_books)

        self.search_button = tk.Button(self, text="search", command=self.search_books)
        self.search_button.grid(row=1, column=2)

        self.tree = ttk.Treeview(self, columns=('ID', 'Title', 'Author', '# of copies available'))
        self.tree.heading('#0', text='ID')
        self.tree.heading('#1', text='Title')
        self.tree.heading('#2', text='Author')
        self.tree.heading('#3', text='# of copies available')

        self.AddBooks = tk.Button(self, text='Add books', command=lambda: switch_frame(AddBooks))
        self.AddBooks.grid(row=2, column=0)

        self.UpdateRemove = tk.Button(self, text="Update/Remove books", command=lambda: switch_frame(UpdateRemove))
        self.UpdateRemove.grid(row=2, column=1)

        self.search_books()

    def search_books(self, event=None):
        book_title = self.search_var.get()
        self.tree.delete(*self.tree.get_children())
        conn = psycopg2.connect(
            host="localhost",
            database="library",
            user="admin",
            password="Admin@123"
        )

        # Create a cursor object for executing SQL queries
        cur = conn.cursor()
        query = """SELECT books.id,books.title,author.name,books.copies 
        FROM books
        JOIN author ON books.author_id = author.id;
        """

        # Execute a SELECT query
        if book_title:
            print(query[:-10])
            query = query[:-10] + f" WHERE books.title LIKE'%{book_title}%';"
            print(query)

        cur.execute(query)
        # Fetch the results of the query
        results = cur.fetchall()
        # print(results)
        print_result = ''
        for res in results:
            self.tree.insert('', 'end', text=res[0], values=(res[1], res[2], res[3]))
        self.tree.grid(row=3, column=0, columnspan=3)


class AddBooks(tk.Frame):
    def __init__(self, master, switch_frame):
        super().__init__(master)
        self.switch_frame = switch_frame
        self.entries = {}

        self.label = tk.Label(self, text='Add Books')
        self.label.pack()

        self.Title = tk.Label(self, text='Title')
        self.Title.pack()
        self.Title_entry = tk.Entry(self, width=50)
        self.Title_entry.pack()
        self.Title_entry.insert(0, "The Lighting Thief")

        self.Author = tk.Label(self, text='Author Name')
        self.Author.pack()
        self.Author_entry = tk.Entry(self, width=50)
        self.Author_entry.pack()
        self.Author_entry.insert(0, "Rick Riordan")

        self.AuthorInfo = tk.Label(self, text='Author Info')
        self.AuthorInfo.pack()
        self.AuthorInfo_entry = tk.Entry(self, width=50)
        self.AuthorInfo_entry.pack()
        self.AuthorInfo_entry.insert(0, "9735644644")

        self.Publisher = tk.Label(self, text='Publisher Name')
        self.Publisher.pack()
        self.Publisher_entry = tk.Entry(self, width=50)
        self.Publisher_entry.pack()
        self.Publisher_entry.insert(0, "Marimax books")

        self.PublisherInfo = tk.Label(self, text='Publisher Info')
        self.PublisherInfo.pack()
        self.PublisherInfo_entry = tk.Entry(self, width=50)
        self.PublisherInfo_entry.pack()
        self.PublisherInfo_entry.insert(0, "9735655655")

        self.PublisherDate = tk.Label(self, text='Publication date (YYYY-MM-DD)')
        self.PublisherDate.pack()
        self.PublisherDate_entry = tk.Entry(self, width=50)
        self.PublisherDate_entry.pack()
        self.PublisherDate_entry.insert(0, "2005-07-02")

        self.isbn = tk.Label(self, text='isbn')
        self.isbn.pack()
        self.isbn_entry = tk.Entry(self, width=50)
        self.isbn_entry.pack()
        self.isbn_entry.insert(0, "9780786856299")

        self.location = tk.Label(self, text='location name')
        self.location.pack()
        self.location_entry = tk.Entry(self, width=50)
        self.location_entry.pack()
        self.location_entry.insert(0, "golden arch")

        self.copies = tk.Label(self, text='number of copies')
        self.copies.pack()
        self.copies_entry = tk.Entry(self, width=50)
        self.copies_entry.pack()
        self.copies_entry.insert(0, "2")

        self.new_fields_frame = tk.Frame(self)
        self.new_fields_frame.pack(side="top", pady=10)

        self.button1 = tk.Button(self, text='Go to admin page', command=lambda: switch_frame(AdminPage))
        self.button1.pack(side="bottom", pady=10)

        self.add_to_db = tk.Button(self, text='add to database', command=self.addToDB)
        self.add_to_db.pack(side="bottom", pady=10)

        self.AdditionalLC = tk.Button(self, text='add loc and copy field', command=self.add_fields)
        self.AdditionalLC.pack(side="bottom", pady=10)

    def add_fields(self):
        location = tk.Label(self.new_fields_frame, text='location name')
        location.pack()
        location_entry = tk.Entry(self.new_fields_frame, width=50)
        location_entry.pack()
        location_entry.insert(0, "city square")

        copies = tk.Label(self.new_fields_frame, text='number of copies')
        copies.pack()
        copies_entry = tk.Entry(self.new_fields_frame, width=50)
        copies_entry.pack()
        copies_entry.insert(0, "3")

        self.entries[location_entry] = copies_entry

    def get_entries(self):
        entry_values = {}

        for location_entry, copies_entry in self.entries.items():
            location = location_entry.get()
            copies = copies_entry.get()

            entry_values[location] = copies

        return entry_values

    def addToDB(self):
        conn = psycopg2.connect(
            host="localhost",
            database="library",
            user="admin",
            password="Admin@123"
        )

        # Create a cursor object for executing SQL queries
        cur = conn.cursor()

        title = self.Title_entry.get()
        author = self.Author_entry.get()
        author_info = self.AuthorInfo_entry.get()
        publisher = self.Publisher_entry.get()
        publisher_info = self.PublisherInfo_entry.get()
        publication_date = self.PublisherDate_entry.get()
        isbn = self.isbn_entry.get()
        location = self.location_entry.get()
        print(location)
        copies = self.copies_entry.get()
        print(copies)
        location_list = []
        copies_list = []
        tot_copies = 0
        if len(self.entries) != 0:
            entry_values = self.get_entries()
            location_list = list(entry_values.keys())
            copies_list = list(entry_values.values())
        location_list.insert(0, location)
        copies_list.insert(0, copies)
        copies_list_int = list(map(int, copies_list))
        for i in copies_list_int:
            tot_copies += i

        print(location_list, copies_list)

        cur.execute("SELECT id FROM author WHERE name = %s;", (author,))
        result = cur.fetchone()
        if result is None:
            cur.execute("INSERT INTO author (name, bio) VALUES (%s, %s);", (author, author_info,))
            cur.execute("SELECT * FROM author WHERE name = %s;", (author,))
            author_id = cur.fetchone()[0]
        else:
            author_id = result[0]

        cur.execute("SELECT id FROM publisher WHERE name = %s;", (publisher,))
        result = cur.fetchone()
        if result is None:
            cur.execute("INSERT INTO publisher (name, address) VALUES (%s, %s);", (publisher, publisher_info,))
            cur.execute("SELECT * FROM publisher WHERE name = %s;", (publisher,))
            publisher_id = cur.fetchone()[0]
        else:
            publisher_id = result[0]

        cur.execute(
            "SELECT id FROM books WHERE title = %s AND author_id = %s AND publisher_id = %s AND publication_date = %s;",
            (title, int(author_id), int(publisher_id), publication_date,))
        result = cur.fetchone()
        if result is not None:
            book_id = result[0]
            cur.execute("UPDATE books SET copies = copies + %s WHERE id = %s;", (tot_copies, book_id,))

            for i in range(len(location_list)):
                copies_loc = copies_list_int[i]
                cur.execute("SELECT id FROM liblocation WHERE name = %s;", (location_list[i],))
                loc_id = cur.fetchone()[0]
                cur.execute("SELECT copy_id FROM copytable WHERE book_id = %s AND lib_id = %s", (book_id, loc_id,))
                copy_no = cur.fetchall()
                latest_copy_no = max([row[0] for row in copy_no]) if copy_no else 0
                print(latest_copy_no)
                for j in range(1, copies_loc + 1):
                    cur.execute("INSERT INTO copytable (book_id, lib_id, copy_id) VALUES (%s, %s, %s);",
                                (book_id, loc_id, int(latest_copy_no)+j,))
                    print(book_id, loc_id, j)

        else:
            cur.execute(
                "INSERT INTO books (title, author_id, publisher_id, publication_date, isbn, copies) VALUES (%s, %s, %s, %s, %s, %s);",
                (title, int(author_id), int(publisher_id), publication_date, isbn, tot_copies,))
            cur.execute("SELECT * FROM books WHERE title = %s;", (title,))
            book_id = cur.fetchone()[0]

            for i in range(len(location_list)):
                copies_loc = copies_list_int[i]
                cur.execute("SELECT id FROM liblocation WHERE name = %s;", (location_list[i],))
                loc_id = cur.fetchone()[0]
                for j in range(1, copies_loc + 1):
                    cur.execute("INSERT INTO copytable (book_id, lib_id, copy_id) VALUES (%s, %s, %s);", (book_id, loc_id, j,))
                    print(book_id, loc_id, j)

        conn.commit()
        cur.close()
        conn.close()


class UpdateRemove(tk.Frame):
    def __init__(self, master, switch_frame):
        super().__init__(master)
        self.switch_frame = switch_frame

        self.label = tk.Label(self, text='Update or Remove Books')
        self.label.pack()

        self.Title = tk.Label(self, text='Title')
        self.Title.pack()
        self.Title_entry = tk.Entry(self, width=50)
        self.Title_entry.pack()
        self.Title_entry.insert(0, "The Lighting Thief")

        self.new_fields_frame = tk.Frame(self)
        self.new_fields_frame.pack(side="top", pady=10)

        self.Title_Button = tk.Button(self, text='fill info for title', command=self.get_info)
        self.Title_Button.pack()

    def get_info(self):
        self.Title_Button.destroy()

        conn = psycopg2.connect(
            host="localhost",
            database="library",
            user="admin",
            password="Admin@123"
        )

        # Create a cursor object for executing SQL queries
        cur = conn.cursor()

        cur.execute("""SELECT *
                FROM books
                WHERE title = %s;
                """, (self.Title_entry.get(),))

        result = cur.fetchall()
        print(result)

        cur.execute(""""SELECT * 
                FROM author
                WHERE id = %s;
        """, (result[2],))

        auth_result = cur.fetchall()
        print(auth_result)

        cur.execute(""""SELECT * 
                        FROM publisher
                        WHERE id = %s;
                """, (result[3],))

        pub_result = cur.fetchall()
        print(pub_result)

        Author = tk.Label(self.new_fields_frame, text='Author Name')
        Author.pack()
        Author_entry = tk.Entry(self.new_fields_frame, width=50)
        Author_entry.pack()
        Author_entry.insert(0, )

        AuthorInfo = tk.Label(self.new_fields_frame, text='Author Info')
        AuthorInfo.pack()
        AuthorInfo_entry = tk.Entry(self.new_fields_frame, width=50)
        AuthorInfo_entry.pack()
        AuthorInfo_entry.insert(0, "9735644644")

        Publisher = tk.Label(self.new_fields_frame, text='Publisher Name')
        Publisher.pack()
        Publisher_entry = tk.Entry(self.new_fields_frame, width=50)
        Publisher_entry.pack()
        Publisher_entry.insert(0, "Marimax books")

        PublisherInfo = tk.Label(self.new_fields_frame, text='Publisher Info')
        PublisherInfo.pack()
        PublisherInfo_entry = tk.Entry(self.new_fields_frame, width=50)
        PublisherInfo_entry.pack()
        PublisherInfo_entry.insert(0, "9735655655")

        PublisherDate = tk.Label(self.new_fields_frame, text='Publication date (YYYY-MM-DD)')
        PublisherDate.pack()
        PublisherDate_entry = tk.Entry(self.new_fields_frame, width=50)
        PublisherDate_entry.pack()
        PublisherDate_entry.insert(0, "2005-07-02")

        isbn = tk.Label(self.new_fields_frame, text='isbn')
        isbn.pack()
        isbn_entry = tk.Entry(self.new_fields_frame, width=50)
        isbn_entry.pack()
        isbn_entry.insert(0, "9780786856299")

        location = tk.Label(self.new_fields_frame, text='location name')
        location.pack()
        location_entry = tk.Entry(self.new_fields_frame, width=50)
        location_entry.pack()
        location_entry.insert(0, "golden arch")

        copies = tk.Label(self.new_fields_frame, text='number of copies')
        copies.pack()
        copies_entry = tk.Entry(self.new_fields_frame, width=50)
        copies_entry.pack()
        copies_entry.insert(0, "2")


class MainApplication(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.title('My Application')

        container = tk.Frame(self)
        container.pack(side='top', fill='both', expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (AdminPage, AddBooks, UpdateRemove):
            frame = F(container, self.switch_frame)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky='nsew')

        self.switch_frame(AdminPage)

    def switch_frame(self, frame_class):
        frame = self.frames[frame_class]
        frame.tkraise()


if __name__ == '__main__':
    app = MainApplication()
    app.mainloop()
    cur.close()
    conn.close()
