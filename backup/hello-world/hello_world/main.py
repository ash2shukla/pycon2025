from typer import Typer, Option
from click import Choice
from .base import registry
from .plugins import EnglishLanguage

registry.register("english", EnglishLanguage)
registry.load_exts()

app = Typer(name="hello-world")

CHOICES = registry.keys()


@app.command()
def main(language: str = Option(default="english", click_type=Choice(CHOICES))):
    plugin = registry.get(name=language)
    plugin.say_hello()
