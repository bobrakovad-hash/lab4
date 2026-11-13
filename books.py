import random
import books_data
def show_help():
    print("add_book — добавить книгу (название и год)")
    print("list_books — показать каталог")
    print("find_book — найти книгу по фрагменту названия")
    print("add_genre — добавить жанр")
    print("list_genres — показать жанры")
    print("long_books — книги с названием длиннее 20 символов")
    print("upper_books — все названия в верхнем регистре")
    print("random_recommendation — случайная рекомендация")
    print("show_help — показать помощь")
    print("exit — выйти из программы")
def add_book(books):
    title = input("Введите название книги: ").strip()
    if title == "":
        print("Название не может быть пустым.")
        return
    year_input = input("Введите год издания (Enter — пропустить): ").strip()
    if year_input == "" or not year_input.isdigit():
        if year_input != "":
            print("Год должен быть числом. Добавляю без года.")
        books.append(title)
    else:
        books.append(title)
        books_data.years[title] = int(year_input)
    print(f"Книга «{title}» добавлена в каталог.")
def list_books(catalog):
    if len(catalog) == 0:
        print("Каталог пуст.")
        return
    print("Ваш каталог книг:")
    for i, title in enumerate(catalog, start=1):
        year = books_data.years.get(title)
        if year is not None:
            print(f"  {i}. {title} ({year})")
        else:
            print(f"  {i}. {title}")
def find_book(books, query):
    return [b for b in books if query in b]
def add_genre(genres, g):
    if g in genres:
        return False
    genres.add(g)
    return True
def list_genres():
    if not books_data.genres:
        print("Список жанров пуст.")
        return
    print("Жанры:", ", ".join(sorted(books_data.genres)))
def long_books(books):
    return [b for b in books if len(b) > 20]
def upper_books(books):
    return [b.upper() for b in books]
def random_recommendation(catalog):
    if len(catalog) == 0:
        print("Каталог пуст — рекомендовать нечего.")
        return
    print("Рекомендую прочитать:")
    print(random.choice(catalog))
