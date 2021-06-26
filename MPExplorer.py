import typer
import json
import time
from os.path import join as pjoin

app = typer.Typer(name="Multiplicative Persistence Explorer", add_completion=False)


def stringify(num):
    l = [0] * 10

    if type(num) == int:
        s = str(num)
        for c in s:
            l[int(c)] += 1
    if type(num) == list:
        for c in num:
            l[c] += 1

    return ",".join([str(i) for i in l[2:]])


class MPExplorer:
    """Object that can be used to explore a given range of integers for additions to the MP Tree"""

    def __init__(self, output_dir="output"):
        self.output_dir = output_dir

    def expand_dict(self, start, end):
        """There are two cubes that need to be expanded: 2^x, 3^y, 7^z and 3^x, 5^y, and 7^z"""
        d = {}
        tic = time.time()
        # seven added shapes to a cube: 2, 3, 7

        # expanded_cube:
        for t in range(start, end):
            tp = 2 ** t
            for th in range(start, end):
                thp = 3 ** th
                for s in range(start, end):
                    sp = 7 ** s
                    num = tp * thp * sp
                    if "0" not in str(num):
                        string = stringify(num)
                        d[string] = d.get(string, []) + [[num, (t, th, 0, s)]]

        # dim-longs
        # 7
        for t in range(start, end):
            tp = 2 ** t
            for th in range(start, end):
                thp = 3 ** th
                for s in range(0, start):
                    sp = 7 ** s
                    num = tp * thp * sp
                    if "0" not in str(num):
                        string = stringify(num)
                        d[string] = d.get(string, []) + [[num, (t, th, 0, s)]]

        # 2
        for t in range(0, start):
            tp = 2 ** t
            for th in range(start, end):
                thp = 3 ** th
                for s in range(start, end):
                    sp = 7 ** s
                    num = tp * thp * sp
                    if "0" not in str(num):
                        string = stringify(num)
                        d[string] = d.get(string, []) + [[num, (t, th, 0, s)]]

        # 3
        for t in range(start, end):
            tp = 2 ** t
            for th in range(0, start):
                thp = 3 ** th
                for s in range(start, end):
                    sp = 7 ** s
                    num = tp * thp * sp
                    if "0" not in str(num):
                        string = stringify(num)
                        d[string] = d.get(string, []) + [[num, (t, th, 0, s)]]

        # faces
        # 2
        for t in range(start, end):
            tp = 2 ** t
            for th in range(0, start):
                thp = 3 ** th
                for s in range(0, start):
                    sp = 7 ** s
                    num = tp * thp * sp
                    if "0" not in str(num):
                        string = stringify(num)
                        d[string] = d.get(string, []) + [[num, (t, th, 0, s)]]

        # 3
        for t in range(0, start):
            tp = 2 ** t
            for th in range(start, end):
                thp = 3 ** th
                for s in range(0, start):
                    sp = 7 ** s
                    num = tp * thp * sp
                    if "0" not in str(num):
                        string = stringify(num)
                        d[string] = d.get(string, []) + [[num, (t, th, 0, s)]]
        # 7
        for t in range(0, start):
            tp = 2 ** t
            for th in range(0, start):
                thp = 3 ** th
                for s in range(start, end):
                    sp = 7 ** s
                    num = tp * thp * sp
                    if "0" not in str(num):
                        string = stringify(num)
                        d[string] = d.get(string, []) + [[num, (t, th, 0, s)]]

        # --------------------------------------------------------------------------------------------------- #
        # cube: 5, 3, 7
        #     print('fives')
        beg_p = 1 if start == 0 else start

        # expanded_cube:
        for t in range(beg_p, end):
            tp = 5 ** t
            for th in range(start, end):
                thp = 3 ** th
                for s in range(start, end):
                    sp = 7 ** s
                    num = tp * thp * sp
                    if "0" not in str(num):
                        string = stringify(num)
                        d[string] = d.get(string, []) + [[num, (0, th, t, s)]]

        # dim-longs
        # 7
        for t in range(beg_p, end):
            tp = 5 ** t
            for th in range(start, end):
                thp = 3 ** th
                for s in range(0, start):
                    sp = 7 ** s
                    num = tp * thp * sp
                    if "0" not in str(num):
                        string = stringify(num)
                        d[string] = d.get(string, []) + [[num, (0, th, t, s)]]

        # 2
        for t in range(1, start):
            tp = 5 ** t
            for th in range(start, end):
                thp = 3 ** th
                for s in range(start, end):
                    sp = 7 ** s
                    num = tp * thp * sp
                    if "0" not in str(num):
                        string = stringify(num)
                        d[string] = d.get(string, []) + [[num, (0, th, t, s)]]

        # 3
        for t in range(beg_p, end):
            tp = 5 ** t
            for th in range(0, start):
                thp = 3 ** th
                for s in range(start, end):
                    sp = 7 ** s
                    num = tp * thp * sp
                    if "0" not in str(num):
                        string = stringify(num)
                        d[string] = d.get(string, []) + [[num, (0, th, t, s)]]

        # faces
        # 2
        for t in range(beg_p, end):
            tp = 5 ** t
            for th in range(0, start):
                thp = 3 ** th
                for s in range(0, start):
                    sp = 7 ** s
                    num = tp * thp * sp
                    if "0" not in str(num):
                        string = stringify(num)
                        d[string] = d.get(string, []) + [[num, (0, th, t, s)]]

        # 3
        for t in range(1, start):
            tp = 5 ** t
            for th in range(start, end):
                thp = 3 ** th
                for s in range(0, start):
                    sp = 7 ** s
                    num = tp * thp * sp
                    if "0" not in str(num):
                        string = stringify(num)
                        d[string] = d.get(string, []) + [[num, (0, th, t, s)]]
        # 7
        for t in range(1, start):
            tp = 5 ** t
            for th in range(0, start):
                thp = 3 ** th
                for s in range(start, end):
                    sp = 7 ** s
                    num = tp * thp * sp
                    if "0" not in str(num):
                        string = stringify(num)
                        d[string] = d.get(string, []) + [[num, (0, th, t, s)]]

        json_file = pjoin(self.output_dir, f"{start}-{end}.json")

        with open(json_file, "w") as f:
            json.dump(d, f, indent=4)

        print(f"{json_file} saved")
        print(
            f"Searching from {start} to {end} took {time.time() - tic} seconds to complete."
        )


@app.command()
def collapse_json(
    output_dir: int = typer.Option(
        "output",
        "--output-dir",
        "-d",
        help="Collapse search JSON from given directory",
    )
):
    # TODO: Given list of JSON, collapse into a full search.
    #  Double check that there are no gaps in the search.
    json_files = [x for x in os.listdir(output_dir) if x.endswith(".json")]


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
    mpe = MPExplorer()
    mpe.expand_dict(start, end)


if __name__ == "__main__":
    app()
