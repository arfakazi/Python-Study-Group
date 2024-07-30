class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return f"{self.title} by {self.author}"

    def __len__(self):
        return self.pages

book = Book("The Great Gatsby", "F. Scott Fitzgerald", 180)
print(book)  # Output: The Great Gatsby by F. Scott Fitzgerald
print(len(book))  # Output: 180
