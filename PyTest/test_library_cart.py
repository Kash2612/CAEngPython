from unittest.mock import Mock
import pytest
from library import LibraryCart
from book_database import BookDatabase

# Fixture to initialize LibraryCart with a max size of 3
@pytest.fixture
def cart():
    return LibraryCart(3)

# Test for adding books to the cart
def test_add_book_to_cart(cart):
    cart.add_book("Harry Potter")
    assert cart.size() == 1
    assert "Harry Potter" in cart.get_books()

# Test adding books beyond max size to raise an OverflowError
def test_add_book_overflow(cart):
    cart.add_book("Harry Potter")
    cart.add_book("Lord of the Rings")
    cart.add_book("To Kill a Mockingbird")

    with pytest.raises(OverflowError):
        cart.add_book("1984")

# Test total price calculation using a mock for BookDatabase
def test_total_price_with_mock(cart):
    cart.add_book("Harry Potter")
    cart.add_book("Lord of the Rings")
    
    # Mock the BookDatabase to simulate price retrieval
    book_db = BookDatabase()
    book_db.get_price = Mock(side_effect=lambda book: {"Harry Potter": 15.0, "Lord of the Rings": 20.0}[book])

    total_price = cart.get_total_price(book_db)
    assert total_price == 35.0

# Parameterized test for different book price maps
@pytest.mark.parametrize("book_list, expected_total", [
    (["Harry Potter", "Lord of the Rings"], 35.0),
    (["To Kill a Mockingbird", "Harry Potter"], 25.0),
    (["Lord of the Rings", "To Kill a Mockingbird"], 30.0),
])
def test_total_price_parametrized(cart, book_list, expected_total):
    for book in book_list:
        cart.add_book(book)
    
    book_db = BookDatabase()
    total_price = cart.get_total_price(book_db)
    assert total_price == expected_total
