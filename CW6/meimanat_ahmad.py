from abc import ABC


class Audible(ABC):
    def __init__(self, title, publish_year, speaker, time, price):
        self.title = title
        self.publish_year = publish_year
        self.speaker = speaker
        self.time = time 
        self.price = price
        self.listen_time = 0

    def get_status(self):
        if self.listen_time == self.time:
            print("Finished")

        elif self.listen_time == 0:
            print("Unread")

        else:
            print("Reading")


class Readable(ABC):
    def __init__(self, title, author, publish_year, pages, language, price):
        self.title = title
        self.publish_year = publish_year
        self.author = author
        self.pages = int(pages)
        self.language = language
        self.price = float(price)
        self.readen_pages = 0
        

    def read(self, pages):
        if self.readen_pages + pages > self.pages:
            raise ValueError("you can not read more than book's pages.")
        else:
            self.readen_pages += pages

            if self.readen_pages == self.pages:
                print(f"you have read {pages} more pages from {self.title}.")
                print("Congrats you have finished the book")

            else:
                print(f"you have read {pages} more pages from {self.title}. There are {self.pages - self.readen_pages} pages left")


    def get_status(self):
        if self.readen_pages == self.pages:
            print("Finished")

        elif self.readen_pages == 0:
            print("Unread")

        else:
            print("Reading")


class Book(Readable):
    shelf = {}

    def __init__(self, title, author, publish_year, pages, language, price):
        super().__init__(title, author, publish_year, pages, language, price)
        Book.shelf[self.title] = self


    def __str__(self) -> str:
        text = f"""Book name: {self.title}\nBook author: {self.author}\nPublish year: {self.publish_year}\nBook pages: {self.author}\nLanguage: {self.language}\nprice: {"%.2f"%self.price}$"""
        
        return text
    

class Magazine(Readable):
    shelf = {}

    def __init__(self, title, author, publish_year, pages, language, price, issue):
        super().__init__(title, author, publish_year, pages, language, price)
        self.issue = issue
        Magazine.shelf[self.title] = self

    def __str__(self) -> str:
        text = f"""Book name: {self.title}\nMagazine issue: {self.issue}\nBook author: {self.author}\nPublish year: {self.publish_year}\nBook pages: {self.author}\nLanguage: {self.language}\nprice: {"%.2f"%self.price}$"""
        
        return text
    
a = Book("ahmad", "ahmad", "1", "100", "ahmad", "100")
# a.read(50)
b = Magazine("asghar", "ahmad", "1", "100", "ahmad", "100", "ahmad")
b.read(50)
print(b)
# a.read(50)



    

        