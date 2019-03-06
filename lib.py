def create_book(title, author, price, availability, tags):
    return {
        'title': title,
        'author': author,
        'price': price,
        'available': availability,
        'tags': tags
    }

def add_books(container, book):
    container.append(book)


def list_books(container, page, page_size):
    start = (page-1) * page_size
    finish = start + page_size
    return container[start:finish]

def search_books(container, search): #search - строка поиска
    searched_lowercased = search.strip().lower()
    result = []
    for book in container :
        if searched_lowercased in book['title'].lower():
            result.append(book)
            continue

        if searched_lowercased in book['author'].lower():
            result.append(book)
            continue

        tags_list = book['tags'].replace(' ', '').lower().split('#')
        if searched_lowercased[1:] in tags_list:
            result.append(book)
            continue
    return result



