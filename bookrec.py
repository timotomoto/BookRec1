from linkedlist import LinkedList
from data import *

def insert_genres():
    genre_list = LinkedList()
    for genre in genres:
        genre_list.insert_beginning(genre)
    return genre_list

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

my_genre_list = insert_genres()
my_book_list = insert_books()

selected_genre = ""

while len(selected_genre) == 0:
    user_input = str(input(
        "\nWhat genre would you like to read?\n"
    )).title()

    matching_types = []
    genre_list_head = my_genre_list.get_head_node()
    while genre_list_head is not None:
        if genre_list_head.get_value() == user_input:
            matching_types.append(genre_list_head.get_value())
        genre_list_head = genre_list_head.get_next_node()
    

    if len(matching_types) == 1:
        select_type = str(input(
            "\nThe only matching type for the specified input is " + matching_types[0] + ". \nDo you want to look at " +
            matching_types[0] + " books? Enter y for yes and n for no\n")).lower()

        if select_type == 'y':
            selected_genre = matching_types[0]
            print("selected_genre: " + selected_genre)
            book_list_head = my_book_list.get_head_node()
            # while book_list_head.get_next_node() is not None:
            sublist_head = book_list_head.get_value().get_head_node()
            while sublist_head.get_next_node() is not None:
                for g in sublist_head.get_value()[0]:
                    if g == selected_genre:
                        print("*")
                        print("Name: " + sublist_head.get_value()[1])
                        print("Author: "+ sublist_head.get_value()[2])
                        print("genre: " + str(sublist_head.get_value()[0]))
                        print("Rating: " + sublist_head.get_value()[3])
                        print("Year published: " + sublist_head.get_value()[4])
                        print("*")
                sublist_head = sublist_head.get_next_node()
                # book_list_head = book_list_head.get_next_node()
