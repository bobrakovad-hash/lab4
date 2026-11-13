from books import add_book, find_book, add_genre, long_books, upper_books
import books_data

def test_add_book():
    test_books = []
    print("--- Тест add_book: вручную введи название, потом Enter, потом год или Enter ---")
    add_book(test_books)
    assert len(test_books) == 1, "Книга не добавилась!"
    print("add_book работает")

def test_find_book():
    test_books = ["Евгений Онегин", "Мёртвые души", "Анна Каренина"]
    assert find_book(test_books, "Онегин") == ["Евгений Онегин"]
    assert find_book(test_books, "Чехов") == []
    print("find_book работает")

def test_add_genre():
    test_genres = {"роман"}
    assert add_genre(test_genres, "поэма") is True
    assert add_genre(test_genres, "роман") is False
    print("add_genre работает")

def test_long_books():
    test_books = ["Короткое", "Очень длинное название книги про всё"]
    assert long_books(test_books) == ["Очень длинное название книги про всё"]
    print("long_books работает")

def test_upper_books():
    test_books = ["Евгений Онегин", "Мёртвые души"]
    assert upper_books(test_books) == ["ЕВГЕНИЙ ОНЕГИН", "МЁРТВЫЕ ДУШИ"]
    print("upper_books работает")

# Запуск
print("=== Запуск тестов ===")
test_add_book()
test_find_book()
test_add_genre()
test_long_books()
test_upper_books()
print("\n Все тесты пройдены!")
