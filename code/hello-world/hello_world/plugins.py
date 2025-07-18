from .base import BaseLanguage

class EnglishLanguage(BaseLanguage):    
    @classmethod
    def say_hello(cls):
        print("hello world!")

