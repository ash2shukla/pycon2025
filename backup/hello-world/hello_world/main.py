from typer import Typer, Option
from hello_world.base import registry
from click import Choice

app = Typer(name="hello-world CLI")
CHOICES = registry.keys()

@app.command()
def main(language: str = Option(default="english", click_type=Choice(CHOICES))):
    registry.get(language)().say_hello()
