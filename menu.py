from library import Library


def main():
    library = Library()

    while True:
        print("\n=== Главное меню ===")
        print("1. Добавить книгу")
        print("2. Удалить книгу")
        print("3. Поиск книги")
        print("4. Отобразить все книги")
        print("5. Изменить статус книги")
        print("0. Выход")

        choice = input("Выберите действие: ")

        if choice == '1':
            title = input("Введите название книги: ")
            author = input("Введите автора книги: ")
            year = input("Введите год издания: ")
            library.add_book(title, author, int(year))
            print("Книга добавлена.")

        elif choice == '2':
            book_id = int(input("Введите ID книги для удаления: "))
            library.remove_book(book_id)
            print("Книга удалена.")

        elif choice == '3':
            query = input("Введите название, автора или год для поиска: ")
            found_books = library.find_books(query)
            if found_books:
                for book in found_books:
                    print(f"{book.id}: {book.title}, {book.author}, {book.year}, {book.status}")
            else:
                print("Книги не найдены.")

        elif choice == '4':
            library.display_books()

        elif choice == '5':
            book_id = int(input("Введите ID книги для изменения статуса: "))
            new_status = input("Введите новый статус ('в наличии' или 'выдана'): ")
            try:
                library.change_status(book_id, new_status)
                print("Статус изменен.")
            except ValueError as e:
                print(e)

        elif choice == '0':
            break

        else:
            print("Некорректный ввод, попробуйте снова.")

