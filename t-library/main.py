from mylibrary.library import Library

def main():
    lbr = Library()

    while True:
        print("\nLibrary Menu")
        print("1. Add Book")
        print("2. Remove Book")
        print("3. Search Book")
        print("4. Show All Books")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            title = input("Enter title: ")
            author = input("Enter author: ")
            lbr.add_book(title, author)
            print("Book added.")

        elif choice == "2":
            title = input("Enter title to remove: ")
            print(lbr.remove_book(title))

        elif choice == "3":
            title = input("Enter title to search: ")
            print(lbr.search_book(title))

        elif choice == "4":
            print(lbr.show_books())

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()