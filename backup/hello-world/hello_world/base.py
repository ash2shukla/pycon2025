from abc import ABC, abstractmethod
from importlib import metadata

class BaseLanguage(ABC):
    @abstractmethod
    def say_hello(self):
        ...


class EnglishLanguage(BaseLanguage):
    def say_hello(self):
        print("hello world")


class LanguageLoader:
    def __init__(self):
        self._impls = {}
    
    def load(self):
        for ep in metadata.entry_points().select(group="hello_world"):
            self.register(ep.name, ep.load())

    def get(self, name: str) -> BaseLanguage:
        return self._impls[name]

    def keys(self):
        return list(self._impls)

    def register(self, name: str, language: BaseLanguage):
        self._impls[name] = language

registry = LanguageLoader()
registry.load()
registry.register("english", EnglishLanguage)
