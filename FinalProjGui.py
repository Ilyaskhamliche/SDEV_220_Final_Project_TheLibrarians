import tkinter as tk
from tkinter import messagebox 

class BookManager:
    def __init__(self, master):
        self.master = master
        self.master.title("Book Manager")
        
        self.books = []
        
        # label
        self.label_book = tk.Label(master, text="Book:")
        self.label_author = tk.Label(master, text="Author:")
        self.label_publisher = tk.Label(master, text="Publisher:")
        
        
        # tk widgets(allows user to input)
        self.entry_book = tk.Entry(master)
        self.entry_author = tk.Entry(master)
        self.entry_publisher = tk.Entry(master)
        
        # choices for the user
        self.button_add = tk.Button(master, text="Add Book", command=self.add_book)
        self.button_update = tk.Button(master, text="Update Book", command=self.update_book)
        self.button_delete = tk.Button(master, text="Delete Book", command=self.delete_book)
        
        
        # layout of the Gui
        
        self.label_book.grid(row = 0, column = 0, sticky=tk.E)
        self.label_author.grid(row=1, column=0, sticky=tk.E)
        self.label_publisher.grid(row=2, column=0, sticky=tk.E) # where the widget should be placed within a cell
        
        self.entry_book.grid(row=0, column=1)
        self.entry_author.grid(row=1, column=1)
        self.entry_publisher.grid(row=2, column=1)

        self.button_add.grid(row=3, column=0, columnspan=2, pady=10)
        self.button_update.grid(row=4, column=0, columnspan=2, pady=10)
        self.button_delete.grid(row=5, column=0, columnspan=2, pady=10) #number of vertical spaces
        
    def add_book(self):
        book = {
            "title": self.entry_book.get(),
            "author": self.entry_author.get(),
            "publisher": self.entry_publisher.get(),
        }
        self.books.append(book)
        self.clear_entries()
        messagebox.showinfo("success", "Book added successfully!")
        
    def update_book(self):
        title_to_update = self.entry_book.get()
        for book in self.books:
            if book["title"] == title_to_update:
                book["author"] = self.entry_author.get()
                book["publisher"] = self.entry_publisher.get()
                self.clear_entries()
                messagebox.showinfo("Success", "Book updated successfully!")
                return
        messagebox.showerror("Error", "Book not found!")
    def delete_book(self):
        title_to_delete = self.entry_book.get()
        for book in self.books:
            if book["title"] == title_to_delete:
                self.books.remove(book)
                self.clear_entries()
                messagebox.showinfo("Success", "Book deleted successfully!")
                return
            messagebox.showerror("Error", "Book not found!")
            
    def clear_entries(self):
        self.entry_book.delete(0, tk.END)
        self.entry_author.delete(0, tk.END)
        self.entry_publisher.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = BookManager(root)
    root.mainloop()    