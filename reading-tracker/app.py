import json

BOOK_DB = "tracker.json"

def load_books():
    try:
        with open(BOOK_DB, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_books(books):
    with open(BOOK_DB, "w") as file:
        json.dump(books, file, indent=4)

def add_book(title, author, pages):
    books = load_books()
    books.append({"title": title, "author": author, "pages": pages, "progress": 0, "review": ""})
    save_books(books)

def update_progress(title, pages_read):
    books = load_books()
    for book in books:
        if book["title"] == title:
            book["progress"] += pages_read
            save_books(books)
            return
    print("Book not found!")

if __name__ == "__main__":
    add_book("1984", "George Orwell", 328)
    update_progress("1984", 50)