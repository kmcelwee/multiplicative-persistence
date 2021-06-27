import os
import typer

from MultiplicativePersistence import Explorer

app = typer.Typer(name="Multiplicative Persistence Explorer", add_completion=False)


@app.command()
def search(
    start: int = typer.Option(
        ...,
        "--start",
        "-s",
        help="What power should the MP search begin with?",
    ),
    end: int = typer.Option(
        ...,
        "--end",
        "-e",
        help="What power should the MP search end with?",
    ),
    output_dir: str = typer.Option(
        "output",
        "--output-dir",
        "-o",
        help="The directory where the output JSON be written",
    ),
):
    explorer = Explorer()
    explorer.explore(start, end)
    collection = explorer.collection
    collection.write_json(os.path.join(output_dir, f"{start}-{end}.json"))


if __name__ == "__main__":
    app()
