from abc import ABC, abstractmethod
from importlib import metadata as importlib_metadata

class BaseLanguage(ABC):
    @classmethod
    @abstractmethod
    def say_hello(cls):
        ...


class LanguagePluginLoader:
    def __init__(self):
        self.impls = {}

    def get(self, language) -> BaseLanguage:
        if language in self.impls:
            return self.impls[language]

        raise ValueError("Language not found")
    
    def list(self) -> tuple[str, ...]:
        return tuple(self.impls)

    def load_external_plugins(self):
        entrypoints = importlib_metadata.entry_points()
        for impl in entrypoints.select(group="hello_world"):
            self.impls[impl.name] = impl.load()

    def register(self, name: str, impl: BaseLanguage):
        self.impls[name] = impl


registry = LanguagePluginLoader()


