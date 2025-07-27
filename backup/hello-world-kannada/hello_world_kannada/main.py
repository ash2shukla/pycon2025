from hello_world.base import BaseLanguage


class KannadaLanguage(BaseLanguage):
    @classmethod
    def say_hello(cls):
        print("ನಮಸ್ತೆ")
