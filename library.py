import json
import os


class Book:
    def __init__(self, id: int, title: str, author: str, year: int, status: str = "в наличии"):
        self.id = id
        self.title = title
        self.author = author
        self.year = year
        self.status = status

    def to_dict(self) -> dict:
        """Конвертирует объект Book в словарь для хранения в JSON."""
        return {
            'id': self.id,
            'title': self.title,
            'author': self.author,
            'year': self.year,
            'status': self.status
        }

    @staticmethod
    def from_dict(data: dict) -> 'Book':
        """Создает объект Book из словаря."""
        return Book(data['id'], data['title'], data['author'], data['year'], data['status'])


class Library:
    def __init__(self, filename: str = 'data.json'):
        self.filename = filename
        self.books = self.load_books()

    def load_books(self) -> list:
        """Загружает книги из файла JSON."""
        if os.path.exists(self.filename):
            with open(self.filename, 'r', encoding='utf-8') as file:
                return [Book.from_dict(book) for book in json.load(file)]
        return []

    def save_books(self) -> None:
        """Сохраняет книги в файл JSON."""
        with open(self.filename, 'w', encoding='utf-8') as file:
            json.dump([book.to_dict() for book in self.books], file, ensure_ascii=False, indent=4)

    def add_book(self, title: str, author: str, year: int) -> None:
        """Добавляет книгу в библиотеку."""
        new_id = max([book.id for book in self.books], default=0) + 1
        new_book = Book(new_id, title, author, year)
        self.books.append(new_book)
        self.save_books()

    def remove_book(self, book_id: int) -> None:
        """Удаляет книгу из библиотеки по id."""
        self.books = [book for book in self.books if book.id != book_id]
        self.save_books()

    def find_books(self, query: str) -> list:
        """Ищет книги по title, author или year."""
        return [book for book in self.books if query.lower() in book.title.lower() or
                                               query.lower() in book.author.lower() or
                                               query == str(book.year)]

    def display_books(self) -> None:
        """Отображает все книги в библиотеке."""
        if not self.books:
            print("Библиотека пуста.")
        else:
            for book in self.books:
                print(f"{book.id}: {book.title}, {book.author}, {book.year}, {book.status}")

    def change_status(self, book_id: int, new_status: str) -> None:
        """Изменяет статус книги по id."""
        for book in self.books:
            if book.id == book_id:
                if new_status in ["в наличии", "выдана"]:
                    book.status = new_status
                    self.save_books()
                else:
                    raise ValueError("Статус может быть только 'в наличии' или 'выдана'.")
                return
        raise ValueError("Книга с данным ID не найдена.")
