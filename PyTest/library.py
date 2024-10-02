class LibraryCart:
    def __init__(self, max_size: int):
        self.books = []
        self.max_size = max_size

    def add_book(self, book_name: str):
        if self.size() >= self.max_size:
            raise OverflowError("Cannot add more books to the cart.")
        self.books.append(book_name)

    def size(self):
        return len(self.books)

    def get_books(self):
        return self.books

    def get_total_price(self, book_db) -> float:
        total_price = 0.0
        for book in self.books:
            total_price += book_db.get_price(book)
        return total_price
