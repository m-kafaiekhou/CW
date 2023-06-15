from abc import ABC , abstractmethod


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

    def listen(self, time):
        if self.listen_time + time > self.time:
            raise ValueError(f"you can not listen more than {self.__class.__name__}'s length.")
        else:
            self.listen_time += time

            if self.listen_time == self.time:
                print(f"you have listen {time} more minutes from {self.title}.")
                print(f"Congrats you have finished the {self.title}")

            else:
                print(f"you have listen {time} more minutes from {self.title}. There are {self.time - self.listen_time} minutes left")

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
            raise ValueError(f"you can not read more than {self.__class__.__name__}'s pages.")
        else:
            self.readen_pages += pages

            if self.readen_pages == self.pages:
                print(f"you have read {pages} more pages from {self.title}.")
                print(f"Congrats you have finished the {self.title}")

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
        text = f"""Book name: {self.title}\nBook author: {self.author}\nPublish year: {self.publish_year}\nBook pages: {self.pages}\nLanguage: {self.language}\nprice: {"%.2f"%self.price}$"""
        
        return text
    

class Magazine(Readable):
    shelf = {}

    def __init__(self, title, author, publish_year, pages, language, price, issue):
        super().__init__(title, author, publish_year, pages, language, price)
        self.issue = issue
        Magazine.shelf[self.title] = self

    def __str__(self) -> str:
        text = f"""Magazine name: {self.title}\nMagazine issue: {self.issue}\nMagazine author: {self.author}\nPublish year: {self.publish_year}\nMagazine pages: {self.pages}\nLanguage: {self.language}\nprice: {"%.2f"%self.price}$"""
        
        return text
    
class Podcast(Audible):
    shelf = {}
    def __init__(self, title, publish_year, speaker, time, price, language):
        super().__init__(title, publish_year, speaker, time, price)
        self.language = language
        Podcast.shelf[self.title] = self



    def __str__(self) -> str:
        text = f"Podcast name: {self.title}\nSpeaker: {self.speaker}\nPublish year: {self.publish_year}\nTime: {self.time}\nLanguage: {self.language}\nPrice: {'%.2f'%self.price}$"
        return text

class AudioBook(Audible):
    shelf = {}
    def __init__(self, title, publish_year, speaker, time, price, book_language, audio_language, author):
        super().__init__(title, publish_year, speaker, time, price)
        self.book_language = book_language
        self.audio_language = audio_language
        self.author = author
        Podcast.shelf[self.title] = self



    def __str__(self) -> str:
        text = f"Podcast name: {self.title}\nSpeaker: {self.speaker}\nAuthor: {self.author}\nPublish year: {self.publish_year}\nTime: {self.time}\nBook Language: {self.book_language}\nAudio Language: {self.audio_language}\nPrice: {'%.2f'%self.price}$"
        return text


# a = Book("ahmad", "ahmad", "1", "100", "ahmad", "100")
# a.read(50)
# print(a)
# b = Magazine("asghar", "ahmad", "1", "100", "ahmad", "100", "ahmad")
# b.read(50)
# print(b)
# c = Magazine("Kolbe zendegi", "Ahmad", 1380, 86, "fa", 12, "something")
# print(c)
# c.read(50)
# c.read(36)

def print_inspect(obj):
    print(f"{type(obj)}\n")
    var_names = [attr for attr in dir(obj) if not callable(getattr(obj, attr)) and not attr.startswith("__")]
    for v in var_names:
        print(f"\tself.{v} = {getattr(obj, v)}\n")

def choose_class():
    text = 'Choose category:'\
    '1. Book'\
    '2. Magazine'\
    '3. Podcast'\
    '4. Audio Book'\
    '>>> '
    
    choice =input(text)
    match choice:
        case "1":
            return Book
        case "2":
            return Magazine
        case "3":
            return Podcast
        case "4":
            return AudioBook
        


def main_menu():
    text="""
1. Add new item
2. Read/Listen
3. Inspect shelf
4. Status
>>> """
    choice = input(text)

    match choice:
        case "1":
            class_ = choose_class()
            list1 = list(class_.__init__.__code__.co_varnames)[1:]
            list2 = list()
            for item in list1:
                list2.append( input(f"\n{item}\n>>> "))
            
            obj = class_(*list2)
            print(obj)
    
# main_menu()

# Audible("ali", 1400, "ahmad ebn ali", 1500, 4000)



# class Shape(ABC):
#     @abstractmethod
#     def area(self):
#         pass

# class Triangle(Shape):
#     pass

# class Circle(Shape):
#     def area(self):
#         return super().area()

# Circle()