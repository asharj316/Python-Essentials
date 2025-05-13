class Library_management:
    def __init__(self):
        self._no_books = 0  
        self._books = []    
        
    def add(self, book):
        """Add a book to the library"""
        if not isinstance(book, str):
            raise ValueError("Book must be a string!")
        if book in self._books:
            print("Book is already in list!")
        else:
            self._books.append(book)
            self._no_books += 1
            
    def show(self):
        
        print("\nLibrary Books:")
        for i, book in enumerate(self._books, 1):  
            print(f"{i}. {book}")
        print()
            
    def count(self):
        
        print("Total books:",self._no_books)


library = Library_management()  
l1=library.add("Oliver Twist")     
l1=library.add("Goosebump")
l1=library.add("Haryy Potter")
l1=library.add("Lord Of Ring")
l1=library.show()
library.count()