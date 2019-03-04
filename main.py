from lib import create_book, add_books, search_books, list_books, search_books_tags

books = []

war_and_piece = create_book(
    'Война и мир',
    'Толстой',
    1000,
    True,
    'война, любовь, толстой',
)

anna_karenina = create_book(
    'Анна Каренина',
    'Толстой',
    500,
    False,
    'поезд, любовь, толстой',
)

add_books(books, war_and_piece)
add_books(books, anna_karenina)


print(search_books_tags(books, 'Толстой'))
