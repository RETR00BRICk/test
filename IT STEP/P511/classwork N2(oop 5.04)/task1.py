class Book:
    def __init__(self, name : str, authors : list, year : int):
        self.name = name
        self.authors = authors
        self.year = year
    def __str__(self):
        return f"Name: {self.name}, Year: {self.year}, authors: {" ".join(self.authors)}"

class Library:
    def __init__(self, name : str, location : str, books : list):
        self.name = name
        self.location = location
        self.books = books

    def __str__(self):
        return f"Name: {self.name}, Location: {self.location}, Books count: {len(self.books)}"
    
    def print_books(self):
        for book in self.books:
            print(f">{book.name} by {" ".join(book.authors)} written in {book.year}")

    def add_book(self, book : Book):
        if type(book) == Book:          #по факту эта проверка тут не нужна, ну я для красоты добавил, выглядит круто просто
            self.books.append(book) 
            return True
        else: 
            return False
    
    def rm_book(self, book_name : str):
        for book in self.books:
            if book.name.lower() == book_name.lower():
                self.books.remove(book)
                return True
        return False
    
    def find_by_name(self, book_name : str):
        for book in self.books:
            if book.name.lower() == book_name.lower():
                return book
        return False

    def find_by_author(self, search : str):
        result = []
        for book in self.books:
            for author in book.authors:
                if search.lower() in author.lower():
                    result.append(book)
                    break
        return result

library = Library("Central", "Prospect Mira 5", [])

while True:
    print("\n--- LIBRARY MENU ---")
    print("1. Add Book")
    print("2. Remove Book")
    print("3. Show All Books")
    print("4. Find by Title")
    print("5. Find by Author")
    print("0. Exit")
    
    choice = input("Select an option: ")

    match choice:
        case "1":
            name = input("Title: ")
            authors = input("enter book authors and place coma between names >>>").split(",")
            year = int(input("Year: "))
            authors = [a.strip() for a in authors] #чтобы пробелы с конца убрать у имени/фамилии автора
            book = Book(name, authors, year)
            print("Book added successfully" if library.add_book(book) else "Error adding book")

        case "2":
            name = input("Enter title to remove>>>")
            print("Book removed" if library.rm_book(name) else "Not found")

        case "3":
            library.print_books()

        case "4":
            name = input("Search title>>>")
            result = library.find_by_name(name)
            print(result if result else "Not found")

        case "5":
            author = input("Search author>>>")
            result = library.find_by_author(author)
            if len(result) == 0:
                print("Not found!")
            for book in result:
                print(book)

        case "0":
            break

        case _:
            print("Invalid choice!")