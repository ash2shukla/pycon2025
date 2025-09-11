from typer import Typer

app = Typer(name="Hello World CLI")

@app.command()
def main():
    ...