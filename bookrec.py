from linkedlist import LinkedList
from data import *

def insert_books():
    boocks = []
    book_list = LinkedList()
    for genre in genres:
        book_sublist = LinkedList()
        for book in books:
            for g in book[0]:
                if g == genre:
                    if book not in boocks:
                        boocks.append(book)
    for b in boocks:
        book_sublist.insert_beginning(b)
    book_list.insert_beginning(book_sublist)
    return book_list