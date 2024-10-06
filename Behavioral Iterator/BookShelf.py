class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
    
    def __str__(self) -> str:
        return f"'{self.title}' by {self.author}"
    

class BookShelf:
    def __init__(self):
        self._books = []
        
    def add_book(self, book):
        self._books.append(book)
        
    def __iter__(self):
        return BookShelfIterator(self)
    
    
class BookShelfIterator:
    def __init__(self, book_shelf):
        self._book_shelf = book_shelf
        self._index = 0
        
    def __iter__(self):
        return self
    
    def __next__(self):
        if self._index < len(self._book_shelf._books):
            book = self._book_shelf._books[self._index]
            self._index += 1
            return book
        else:
            raise StopIteration
        

#Client code
if __name__ == "__main__":
    shelf = BookShelf()
    shelf.add_book(Book("The Great Gatsby", "F.Scott Fitzgerald"))
    shelf.add_book(Book("Moby Dick", "Herman Melville"))
    shelf.add_book(Book("1984", "George Orwell"))
    
    for book in shelf:
        print(book)
            