import pytest
import os
import json
from library import Book, Library


TEST_BOOKS = [
    {'id': 1, 'title': '1984', 'author': 'Джордж Оруэлл', 'year': 1949, 'status': 'в наличии'},
    {'id': 2, 'title': 'По полям', 'author': 'Синий трактор', 'year': 2014, 'status': 'в наличии'}
]


def teardown_module(module):
    try:
        os.remove('data.json')
    except FileNotFoundError:
        pass


def test_book_creation():
    book = Book(1, "1984", "Джордж Оруэлл", 1949)
    assert book.id == 1
    assert book.title == "1984"
    assert book.author == "Джордж Оруэлл"
    assert book.year == 1949
    assert book.status == "в наличии"


def test_book_to_dict():
    book = Book(1, "1984", "Джордж Оруэлл", 1949)
    expected_dict = {
        'id': 1,
        'title': '1984',
        'author': 'Джордж Оруэлл',
        'year': 1949,
        'status': 'в наличии'
    }
    assert book.to_dict() == expected_dict


def test_book_from_dict():
    book_data = {'id': 1, 'title': '1984', 'author': 'Джордж Оруэлл', 'year': 1949, 'status': 'в наличии'}
    book = Book.from_dict(book_data)
    assert book.id == 1
    assert book.title == "1984"
    assert book.author == "Джордж Оруэлл"
    assert book.year == 1949
    assert book.status == "в наличии"


def test_library_load_books_empty():
    library = Library("test_data.json")
    assert len(library.books) == 0


def test_library_save_and_load_books():
    library = Library("test_data.json")

    for book_data in TEST_BOOKS:
        book = Book.from_dict(book_data)
        library.books.append(book)

    library.save_books()

    new_library = Library("test_data.json")

    assert len(new_library.books) == len(TEST_BOOKS)
    for i, book in enumerate(new_library.books):
        assert book.title == TEST_BOOKS[i]['title']
        assert book.author == TEST_BOOKS[i]['author']
        assert book.year == TEST_BOOKS[i]['year']
        assert book.status == TEST_BOOKS[i]['status']


def test_library_save_to_json():
    library = Library("test_data.json")

    book = Book(3, "Три кота", "Одна кошечка", 2015)
    library.books.append(book)

    library.save_books()

    with open("test_data.json", "r", encoding="utf-8") as file:
        data = json.load(file)
        assert len(data) == 3
        assert data[2]['title'] == "Три кота"
        assert data[2]['author'] == "Одна кошечка"
        assert data[2]['year'] == 2015
        assert data[2]['status'] == "в наличии"


if __name__ == "__main__":
    pytest.main()
