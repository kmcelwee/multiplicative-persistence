import Explorer
import typer

app = typer.Typer(name="Multiplicative Persistence Explorer", add_completion=False)


@app.command()
def search(
    end: int = typer.Option(
        # A triple dot makes this "option" required. It's doesn't follow CLI
        #  convention but it makes for clearer shell commands
        ...,
        "--end",
        "-e",
        help="What power should the MP search end with?",
    ),
    start: int = typer.Option(
        0,
        "--start",
        "-s",
        help="What power should the MP search begin with?",
    ),
):
    assert start < end, "start value must be less than end value"
    assert 0 <= start < end, "start and end values must be greater than 0"

    mpe = MPExplorer()
    mpe.expand_dict(start, end)


if __name__ == "__main__":
    app()
