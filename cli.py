import os
import typer
import datetime
from rich.console import Console

from MultiplicativePersistence import Explorer, Tree, MpNumberCollection

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

    json_path = os.path.join(output_dir, f"{start}-{end}.json")
    collection.write_json(json_path)
    Console().print(f'Wrote {collection.count()} MP numbers to "{json_path}"')
    Console().print(
        f"Process completed in {explorer.run_time} seconds. ({datetime.timedelta(seconds=explorer.run_time)})"
    )


@app.command()
def print_tree(
    root: int = typer.Argument(
        default=None,
        help="Which root should be printed?",
    ),
):
    collection = MpNumberCollection(json_path="output/0-475.json")
    tree = Tree(collection)
    if root is not None:
        tree.print(root=root)
    tree.print_summary(root=root)


if __name__ == "__main__":
    app()
