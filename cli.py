import os
import typer
import datetime
import json
from deepdiff import DeepDiff
from rich.console import Console
from rich.table import Table

from MultiplicativePersistence import Explorer, Tree, MpNumberCollection, SpeedyExplorer

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


@app.command()
def speed_test(
    use_cache: bool = typer.Option(False, "--use-cache", "-u"),
    test_count: int = typer.Option(default=5),
    start: int = typer.Option(
        100,
        "--start",
        "-s",
        help="What power should the MP search begin with?",
    ),
    end: int = typer.Option(
        120,
        "--end",
        "-e",
        help="What power should the MP search end with?",
    ),
):
    console = Console()
    test_results = {"start": start, "end": end, "old": [], "new": []}
    with open("tmp/speed-test-cache.json") as f:
        cache = json.load(f)

    # Don't use the cache if it doesn't match the requested parameters
    if cache["start"] != start or cache["end"] != end:
        use_cache = False
        console.print(f"Cache doesn't match requested parameters. Not using cache.")

    if use_cache:
        test_results["old"] = cache["old"]
        test_results["old_dict"] = cache["old_dict"]
    else:
        console.print("Processing old explorer...")
        for _ in range(test_count):
            explorer_o = Explorer()
            explorer_o.explore(start, end)
            seconds = explorer_o.run_time
            test_results["old"].append(seconds)
        test_results["old_dict"] = explorer_o.collection.to_dict()

    console.print("Processing speedy explorer...")
    for _ in range(test_count):
        explorer_n = SpeedyExplorer()
        explorer_n.explore(start, end)
        seconds = explorer_n.run_time
        test_results["new"].append(seconds)
    test_results["new_dict"] = explorer_n.collection.to_dict()

    with open("tmp/speed-test-cache.json", "w") as f:
        json.dump(test_results, f, indent=4)

    ##
    # Ensure that refactoring didn't cause numbers to be missed
    assert test_results["new_dict"] == test_results["old_dict"], DeepDiff(
        test_results["old_dict"], test_results["new_dict"]
    )

    ##
    # Calculate and display results
    table = Table(show_footer=False)
    table.add_column("Test")
    table.add_column("Original")
    table.add_column("Speedy")

    for i, (test_o, test_n) in enumerate(zip(test_results["old"], test_results["new"])):
        table.add_row(str(i), str(test_o), str(test_n))

    avg_o = round(sum(test_results["old"]) / len(test_results["old"]), 2)
    avg_n = round(sum(test_results["new"]) / len(test_results["new"]), 2)
    table.add_row("Average", str(avg_o), str(avg_n))

    console.print(f"Start: {start}")
    console.print(f"End: {end}")
    console.print(table)
    console.print(f"Average speed increase: {avg_o/avg_n}x", style="green")


if __name__ == "__main__":
    app()
