class BookDatabase:
    def __init__(self):
        # Simulating a small database of books with prices
        self.book_prices = {
            "Harry Potter": 15.0,
            "Lord of the Rings": 20.0,
            "To Kill a Mockingbird": 10.0
        }

    def get_price(self, book_name: str) -> float:
        if book_name not in self.book_prices:
            raise ValueError(f"Book '{book_name}' not found in the database.")
        return self.book_prices[book_name]
