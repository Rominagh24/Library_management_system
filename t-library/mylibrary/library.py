class Library:
    def __init__(self):
        self.books = []

    def add_book(self, title, author):
        self.books.append({"title": title, "author": author})

    def remove_book(self, title):
        for book in self.books:
            if book["title"] == title:
                self.books.remove(book)
                print("کتاب حذف شد.")
                return
        print("کتاب پیدا نشد.")

    def search_book(self, title):
        for book in self.books:
            if book["title"] == title:
                print("کتاب پیدا شد:", book)
                return
        print("کتاب پیدا نشد.")

    def show_books(self):
        for book in self.books:
            print(f"{book['title']} - {book['author']}")


