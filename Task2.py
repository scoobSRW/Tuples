# Existing library data
library = [("1984", "George Orwell"), ("Brave New World", "Aldous Huxley")]

def add_book(library, book):
    if book in library:
        print(f"The book '{book[0]}' by {book[1]} already exists in the library.")
    else:
        library.append(book)
        print(f"Added '{book[0]}' by {book[1]} to the library.")

# Example usage
new_book_1 = ("Fahrenheit 451", "Ray Bradbury")
new_book_2 = ("1984", "George Orwell")

add_book(library, new_book_1)
add_book(library, new_book_2)

print("\nUpdated Library:")
for book in library:
    print(f"'{book[0]}' by {book[1]}")
