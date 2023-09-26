import sqlite3

# Connect to the database
conn = sqlite3.connect('library.db')

# Create the Books table
conn.execute('''CREATE TABLE Books
             (BookID TEXT PRIMARY KEY NOT NULL,
             Title TEXT NOT NULL,
             Author TEXT NOT NULL,
             ISBN TEXT NOT NULL,
             Status TEXT NOT NULL);''')

# Create the Users table
conn.execute('''CREATE TABLE Users
             (UserID TEXT PRIMARY KEY NOT NULL,
             Name TEXT NOT NULL,
             Email TEXT NOT NULL);''')

# Create the Reservations table
conn.execute('''CREATE TABLE Reservations
             (ReservationID TEXT PRIMARY KEY NOT NULL,
             BookID TEXT NOT NULL,
             UserID TEXT NOT NULL,
             ReservationDate TEXT NOT NULL,
             FOREIGN KEY (BookID) REFERENCES Books(BookID),
             FOREIGN KEY (UserID) REFERENCES Users(UserID));''')

# Function to add a new book to the Books table
def add_book():
    book_id = input("Enter the BookID: ")
    title = input("Enter the title: ")
    author = input("Enter the author: ")
    isbn = input("Enter the ISBN: ")
    status = input("Enter the status: ")
    conn.execute(f"INSERT INTO Books (BookID, Title, Author, ISBN, Status) VALUES ('{book_id}', '{title}', '{author}', '{isbn}', '{status}')")
    conn.commit()
    print("Book added successfully!")

# Function to search for a book by BookID and display its details
def search_book():
    book_id = input("Enter the BookID: ")
    cursor = conn.execute(f"SELECT Books.BookID, Books.Title, Books.Author, Books.ISBN, Books.Status, Reservations.ReservationID, Reservations.UserID, Reservations.ReservationDate FROM Books LEFT JOIN Reservations ON Books.BookID = Reservations.BookID WHERE Books.BookID = '{book_id}'")
    rows = cursor.fetchall()
    if len(rows) == 0:
        print("Book not found!")
    else:
        for row in rows:
            print(f"BookID: {row[0]}")
            print(f"Title: {row[1]}")
            print(f"Author: {row[2]}")
            print(f"ISBN: {row[3]}")
            print(f"Status: {row[4]}")
            if row[5] is not None:
                print(f"ReservationID: {row[5]}")
                print(f"UserID: {row[6]}")
                print(f"ReservationDate: {row[7]}")
                print("This book has been reserved.")
            else:
                print("This book has not been reserved.")

# Function to search for a book by BookID, Title, UserID or ReservationID and display its reservation status
def search_reservation():
    search_text = input("Enter the search text: ")
    if search_text.startswith("LB"):
        cursor = conn.execute(f"SELECT Books.BookID, Books.Title, Books.Author, Books.ISBN, Books.Status, Reservations.ReservationID, Reservations.UserID, Reservations.ReservationDate FROM Books LEFT JOIN Reservations ON Books.BookID = Reservations.BookID WHERE Books.BookID = '{search_text}'")
    elif search_text.startswith("LU"):
        cursor = conn.execute(f"SELECT Books.BookID, Books.Title, Books.Author, Books.ISBN, Books.Status, Reservations.ReservationID, Reservations.UserID, Reservations.ReservationDate FROM Books LEFT JOIN Reservations ON Books.BookID = Reservations.BookID WHERE Reservations.UserID = '{search_text}'")
    elif search_text.startswith("LR"):
        cursor = conn.execute(f"SELECT Books.BookID, Books.Title, Books.Author, Books.ISBN, Books.Status, Reservations.ReservationID, Reservations.UserID, Reservations.ReservationDate FROM Books LEFT JOIN Reservations ON Books.BookID = Reservations.BookID WHERE Reservations.ReservationID = '{search_text}'")
    else:
        cursor = conn.execute(f"SELECT Books.BookID, Books.Title, Books.Author, Books.ISBN, Books.Status, Reservations.ReservationID, Reservations.UserID, Reservations.ReservationDate FROM Books LEFT JOIN Reservations ON Books.BookID = Reservations.BookID WHERE Books.Title = '{search_text}'")
    rows = cursor.fetchall()
    if len(rows) == 0:
        print("Book not found!")
    else:
        for row in rows:
            print(f"BookID: {row[0]}")
            print(f"Title: {row[1]}")
            print(f"Author: {row[2]}")
            print(f"ISBN: {row[3]}")
            print(f"Status: {row[4]}")
            if row[5] is not None:
                print(f"ReservationID: {row[5]}")
                print(f"UserID: {row[6]}")
                print(f"ReservationDate: {row[7]}")
                print("This book has been reserved.")
            else:
                print("This book has not been reserved.")

# Function to display all books in the Books table
def display_books():
    cursor = conn.execute("SELECT Books.BookID, Books.Title, Books.Author, Books.ISBN, Books.Status, Reservations.ReservationID, Reservations.UserID, Reservations.ReservationDate FROM Books LEFT JOIN Reservations ON Books.BookID = Reservations.BookID")
    rows = cursor.fetchall()
    if len(rows) == 0:
        print("No books found!")
    else:
        for row in rows:
            print(f"BookID: {row[0]}")
            print(f"Title: {row[1]}")
            print(f"Author: {row[2]}")
            print(f"ISBN: {row[3]}")
            print(f"Status: {row[4]}")
            if row[5] is not None:
                print(f"ReservationID: {row[5]}")
                print(f"UserID: {row[6]}")
                print(f"ReservationDate: {row[7]}")
                print("This book has been reserved.")
            else:
                print("This book has not been reserved.")

# Function to update the details of a book by BookID
def update_book():
    book_id = input("Enter the BookID: ")
    title = input("Enter the title (press enter to skip): ")
    author = input("Enter the author (press enter to skip): ")
    isbn = input("Enter the ISBN (press enter to skip): ")
    status = input("Enter the status (press enter to skip): ")
    if title != "":
        conn.execute(f"UPDATE Books SET Title = '{title}' WHERE BookID = '{book_id}'")
    if author != "":
        conn.execute(f"UPDATE Books SET Author = '{author}' WHERE BookID = '{book_id}'")
    if isbn != "":
        conn.execute(f"UPDATE Books SET ISBN = '{isbn}' WHERE BookID = '{book_id}'")
    if status != "":
        conn.execute(f"UPDATE Books SET Status = '{status}' WHERE BookID = '{book_id}'")
    conn.commit()
    print("Book details updated successfully!")

# Function to delete a book by BookID
def delete_book():
    book_id = input("Enter the BookID: ")
    conn.execute(f"DELETE FROM Books WHERE BookID = '{book_id}'")
    conn.execute(f"DELETE FROM Reservations WHERE BookID = '{book_id}'")
    conn.commit()
    print("Book deleted successfully!")

# Main function to display the menu and handle user input
def main():
    while True:
        print("1. Add a new book")
        print("2. Search for a book by BookID")
        print("3. Search for a book by BookID, Title, UserID or ReservationID")
        print("4. Display all books")
        print("5. Update book details by BookID")
        print("6. Delete a book by BookID")
        print("7. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            add_book()
        elif choice == "2":
            search_book()
        elif choice == "3":
            search_reservation()
        elif choice == "4":
            display_books()
        elif choice == "5":
            update_book()
        elif choice == "6":
            delete_book()
        elif choice == "7":
            break
        else:
            print("Invalid choice. Please try again.")

# Call the main function
if __name__ == '__main__':
    main()
