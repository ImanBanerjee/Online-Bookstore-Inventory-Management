import tkinter as tk
from tkinter import messagebox

# Global list to store books
book_list = []

def save_list():
    with open("books.txt", "w") as file:
        for book in book_list:
            file.write(f"{book['name']}, {book['author']}, {book['genre']}, {book['price']}, {book['quantity']}, {book['available']}\n")

def load_list():
    try:
        with open("books.txt", "r") as file:
            for line in file:
                name, author, genre, price, quantity, available = line.strip().split(", ")
                book = {
                    "name": name,
                    "author": author,
                    "genre": genre,
                    "price": float(price),
                    "quantity": int(quantity),
                    "available": available == "True"
                }
                book_list.append(book)
    except FileNotFoundError:
        print("No book list found")

def add_book():
    name = name_entry.get()
    author = author_entry.get()
    genre = genre_entry.get()
    price = price_entry.get()
    quantity = quantity_entry.get()

    # Validate input
    if not (name and author and genre and price and quantity):
        messagebox.showerror("Error", "Please fill in all fields")
        return

    try:
        price = float(price)
        quantity = int(quantity)
    except ValueError:
        messagebox.showerror("Error", "Price and quantity must be numeric")
        return

    book = {
        "name": name,
        "author": author,
        "genre": genre,
        "price": price,
        "quantity": quantity,
        "available": True
    }
    book_list.append(book)
    messagebox.showinfo("Success", "Book added successfully")
    save_list()
    clear_entries()

def update_book():
    name = update_name_entry.get()
    author = update_author_entry.get()
    genre = update_genre_entry.get()
    price = update_price_entry.get()
    quantity = update_quantity_entry.get()

    # Validate input
    if not (name and author and genre and price and quantity):
        messagebox.showerror("Error", "Please fill in all fields")
        return

    try:
        price = float(price)
        quantity = int(quantity)
    except ValueError:
        messagebox.showerror("Error", "Price and quantity must be numeric")
        return

    # Search for the book
    found_books = [book for book in book_list if book["name"].lower() == name.lower()]
    if found_books:
        for book in found_books:
            book["author"] = author
            book["genre"] = genre
            book["price"] = price
            book["quantity"] = quantity
        messagebox.showinfo("Success", "Book updated successfully")
        save_list()
        clear_update_entries()
    else:
        messagebox.showerror("Error", f"No book found with the name {name}")

def remove_book():
    name = remove_name_entry.get()

    # Search for the book
    found_books = [book for book in book_list if book["name"].lower() == name.lower()]
    if found_books:
        for book in found_books:
            book_list.remove(book)
        messagebox.showinfo("Success", "Book removed successfully")
        save_list()
        clear_remove_entry()
    else:
        messagebox.showerror("Error", f"No book found with the name {name}")

def search_book():
    search_query = search_entry.get().lower()
    found_books = [book for book in book_list if search_query in book["name"].lower()]
    if found_books:
        search_result.delete(1.0, tk.END)
        for book in found_books:
            search_result.insert(tk.END, f"Name: {book['name']}, Author: {book['author']}, Genre: {book['genre']}, Price: {book['price']}, Quantity: {book['quantity']}, Available: {book['available']}\n")
    else:
        messagebox.showinfo("Info", f"No book found with the name {search_query}")

def display_books():
    display_result.delete(1.0, tk.END)
    for book in book_list:
        display_result.insert(tk.END, f"Name: {book['name']}, Author: {book['author']}, Genre: {book['genre']}, Price: {book['price']}, Quantity: {book['quantity']}, Available: {book['available']}\n")

def total_quantity():
    total = sum(book['quantity'] for book in book_list)
    messagebox.showinfo("Total Quantity", f"Total Quantity: {total}")

def clear_entries():
    name_entry.delete(0, tk.END)
    author_entry.delete(0, tk.END)
    genre_entry.delete(0, tk.END)
    price_entry.delete(0, tk.END)
    quantity_entry.delete(0, tk.END)

def clear_update_entries():
    update_name_entry.delete(0, tk.END)
    update_author_entry.delete(0, tk.END)
    update_genre_entry.delete(0, tk.END)
    update_price_entry.delete(0, tk.END)
    update_quantity_entry.delete(0, tk.END)

def clear_remove_entry():
    remove_name_entry.delete(0, tk.END)

# Create GUI window
root = tk.Tk()
root.title("Online Bookstore Inventory Management")

# Load existing data
load_list()

# Labels and Entry fields for book details
tk.Label(root, text="Name:").grid(row=0, column=0, sticky="e")
name_entry = tk.Entry(root)
name_entry.grid(row=0, column=1)

tk.Label(root, text="Author:").grid(row=1, column=0, sticky="e")
author_entry = tk.Entry(root)
author_entry.grid(row=1, column=1)

tk.Label(root, text="Genre:").grid(row=2, column=0, sticky="e")
genre_entry = tk.Entry(root)
genre_entry.grid(row=2, column=1)

tk.Label(root, text="Price:").grid(row=3, column=0, sticky="e")
price_entry = tk.Entry(root)
price_entry.grid(row=3, column=1)

tk.Label(root, text="Quantity:").grid(row=4, column=0, sticky="e")
quantity_entry = tk.Entry(root)
quantity_entry.grid(row=4, column=1)

# Button to add book
add_button = tk.Button(root, text="Add Book", command=add_book)
add_button.grid(row=5, column=1, pady=5)

# Labels and Entry fields for updating book
tk.Label(root, text="Name:").grid(row=6, column=0, sticky="e")
update_name_entry = tk.Entry(root)
update_name_entry.grid(row=6, column=1)

tk.Label(root, text="Author:").grid(row=7, column=0, sticky="e")
update_author_entry = tk.Entry(root)
update_author_entry.grid(row=7, column=1)

tk.Label(root, text="Genre:").grid(row=8, column=0, sticky="e")
update_genre_entry = tk.Entry(root)
update_genre_entry.grid(row=8, column=1)

tk.Label(root, text="Price:").grid(row=9, column=0, sticky="e")
update_price_entry = tk.Entry(root)
update_price_entry.grid(row=9, column=1)

tk.Label(root, text="Quantity:").grid(row=10, column=0, sticky="e")
update_quantity_entry = tk.Entry(root)
update_quantity_entry.grid(row=10, column=1)

# Button to update book
update_button = tk.Button(root, text="Update Book", command=update_book)
update_button.grid(row=11, column=1, pady=5)

# Labels and Entry fields for removing book
tk.Label(root, text="Name:").grid(row=12, column=0, sticky="e")
remove_name_entry = tk.Entry(root)
remove_name_entry.grid(row=12, column=1)

# Button to remove book
remove_button = tk.Button(root, text="Remove Book", command=remove_book)
remove_button.grid(row=13, column=1, pady=5)

# Label and Entry field for searching book
tk.Label(root, text="Search:").grid(row=14, column=0, sticky="e")
search_entry = tk.Entry(root)
search_entry.grid(row=14, column=1)

# Button to search book
search_button = tk.Button(root, text="Search", command=search_book)
search_button.grid(row=15, column=1, pady=5)

# Text widget to display search results
search_result = tk.Text(root, height=5, width=50)
search_result.grid(row=16, columnspan=2, pady=5)

# Button to display all books
display_button = tk.Button(root, text="Display All Books", command=display_books)
display_button.grid(row=17, column=1, pady=5)

# Text widget to display all books
display_result = tk.Text(root, height=10, width=50)
display_result.grid(row=18, columnspan=2, pady=5)

# Button to calculate total quantity
total_quantity_button = tk.Button(root, text="Total Quantity", command=total_quantity)
total_quantity_button.grid(row=19, column=1, pady=5)

root.mainloop()
