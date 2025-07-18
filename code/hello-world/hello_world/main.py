from typer import Typer, Option
from click import Choice
from .base import registry
from .plugins import EnglishLanguage

registry.register("english", EnglishLanguage)
registry.load_external_plugins()

app = Typer(name="hello-world")

@app.command()
def main(language: str= Option(default="english", click_type=Choice(registry.list()))):
    plugin = registry.get(language=language)
    plugin.say_hello()
