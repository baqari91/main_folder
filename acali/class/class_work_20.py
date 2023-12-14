# #SOLID
# #1. Single Responsibility Principle
# class Book:
#     def __init__(self, title, author, content):
#         self.title = title
#         self.author = author
#         self.content = content
#
#     def get_title(self):
#         return self.title
#
#     def get_author(self):
#         return self.author
#
#     def get_content(self):
#         return self.content
#
# class BookPrinter:
#     def print_book(self, book):
#         print(f"Title: {book.get_title()}")
#         print(f"Author: {book.get_author()}")
#         print(f"Content: {book.get_content()}")
#
# #2 The Open/Closed Principle
# class BookFormatter:
#     def format(self, book):
#         formatted_content = self.format_content(book.get_content())
#         return f"Title: {book.get_title()}\nAuthor: {book.get_author()}\nContent: {formatted_content}"
#
#     def format_content(self, content):
#         #content formatting ...
#         return content
#


#3 Liskov Substitution Principle
# class KitchenApp:
#     @classmethod
#     def on(cls):
#         pass
#
#     @classmethod
#     def off(cls):
#         pass
#
#     @classmethod
#     def set_temperature(cls):
#         pass
#
# class Toster(KitchenApp):
#     @classmethod
#     def on(cls):
#         print("turned on toaster")
#
#     @classmethod
#     def off(cls):
#         print("turned off toaster")
#
#     @classmethod
#     def set_temperature(cls):
#         print("set temperature on toaster")
#
# class Juicer(KitchenApp):
#     @classmethod
#     def on(cls):
#         print("turned on Juicer")
#
#     @classmethod
#     def off(cls):
#         print("turned off Juicer")
#
# class KitchenApp:
#     @classmethod
#     def on(cls):
#         pass
#
#     @classmethod
#     def off(cls):
#         pass
#
# class KitchenAppWithTemperature(KitchenApp):
#     @classmethod
#     def set_temperature(cls):
#         pass
#
# class Toaster(KitchenAppWithTemperature):
#     @classmethod
#     def on(cls):
#         print("turned on toaster")
#
#     @classmethod
#     def off(cls):
#         print("turned off toaster")
#
#     @classmethod
#     def set_temperature(cls):
#         print("set temperature on toaster")
#
# class Juicer(KitchenApp):
#     @classmethod
#     def on(cls):
#         print("turned on Juicer")
#
#     @classmethod
#     def off(cls):
#         print("turned off Juicer")

from abc import ABC, abstractmethod

class Phone(ABC):
    @abstractmethod
    def voice(self):
        pass

class Text(ABC):
    @abstractmethod
    def text(self):
        pass

class Camera(ABC):
    @abstractmethod
    def camera(self):
        pass

class NewMobile(Phone, Text, Camera):
    def voice(self):
        print("Sending Voice")
    def text(self):
        print("Sending Text")
    def camera(self):
        print("Sending Video")

class OldMobileDevice(Phone, Text):
    def voice(self):
        print("Sending Voice")
    def text(self):
        print("Sending Text")