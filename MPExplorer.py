import json
import time
from os.path import join as pjoin


class MPExplorer:
    """Object that can be used to explore a given range of integers for additions to the MP Tree"""

    def __init__(self, input_dict, output_dir="output"):
        self.input_dict = input_dict
        self.output_dir = output_dir

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

    def expand_dict(self, beg, end):
        """There are two cubes that need to be expanded: 2^x, 3^y, 7^z and 3^x, 5^y, and 7^z"""
        d = self.input_dict
        tic = time.time()
        # seven added shapes to a cube: 2, 3, 7

        # expanded_cube:
        for t in range(beg, end):
            tp = 2 ** t
            for th in range(beg, end):
                thp = 3 ** th
                for s in range(beg, end):
                    sp = 7 ** s
                    num = tp * thp * sp
                    if "0" not in str(num):
                        string = stringify(num)
                        d[string] = d.get(string, []) + [[num, (t, th, 0, s)]]

        # dim-longs
        # 7
        for t in range(beg, end):
            tp = 2 ** t
            for th in range(beg, end):
                thp = 3 ** th
                for s in range(0, beg):
                    sp = 7 ** s
                    num = tp * thp * sp
                    if "0" not in str(num):
                        string = stringify(num)
                        d[string] = d.get(string, []) + [[num, (t, th, 0, s)]]

        # 2
        for t in range(0, beg):
            tp = 2 ** t
            for th in range(beg, end):
                thp = 3 ** th
                for s in range(beg, end):
                    sp = 7 ** s
                    num = tp * thp * sp
                    if "0" not in str(num):
                        string = stringify(num)
                        d[string] = d.get(string, []) + [[num, (t, th, 0, s)]]

        # 3
        for t in range(beg, end):
            tp = 2 ** t
            for th in range(0, beg):
                thp = 3 ** th
                for s in range(beg, end):
                    sp = 7 ** s
                    num = tp * thp * sp
                    if "0" not in str(num):
                        string = stringify(num)
                        d[string] = d.get(string, []) + [[num, (t, th, 0, s)]]

        # faces
        # 2
        for t in range(beg, end):
            tp = 2 ** t
            for th in range(0, beg):
                thp = 3 ** th
                for s in range(0, beg):
                    sp = 7 ** s
                    num = tp * thp * sp
                    if "0" not in str(num):
                        string = stringify(num)
                        d[string] = d.get(string, []) + [[num, (t, th, 0, s)]]

        # 3
        for t in range(0, beg):
            tp = 2 ** t
            for th in range(beg, end):
                thp = 3 ** th
                for s in range(0, beg):
                    sp = 7 ** s
                    num = tp * thp * sp
                    if "0" not in str(num):
                        string = stringify(num)
                        d[string] = d.get(string, []) + [[num, (t, th, 0, s)]]
        # 7
        for t in range(0, beg):
            tp = 2 ** t
            for th in range(0, beg):
                thp = 3 ** th
                for s in range(beg, end):
                    sp = 7 ** s
                    num = tp * thp * sp
                    if "0" not in str(num):
                        string = stringify(num)
                        d[string] = d.get(string, []) + [[num, (t, th, 0, s)]]

        # --------------------------------------------------------------------------------------------------- #
        # cube: 5, 3, 7
        #     print('fives')
        beg_p = 1 if beg == 0 else beg

        # expanded_cube:
        for t in range(beg_p, end):
            tp = 5 ** t
            for th in range(beg, end):
                thp = 3 ** th
                for s in range(beg, end):
                    sp = 7 ** s
                    num = tp * thp * sp
                    if "0" not in str(num):
                        string = stringify(num)
                        d[string] = d.get(string, []) + [[num, (0, th, t, s)]]

        # dim-longs
        # 7
        for t in range(beg_p, end):
            tp = 5 ** t
            for th in range(beg, end):
                thp = 3 ** th
                for s in range(0, beg):
                    sp = 7 ** s
                    num = tp * thp * sp
                    if "0" not in str(num):
                        string = stringify(num)
                        d[string] = d.get(string, []) + [[num, (0, th, t, s)]]

        # 2
        for t in range(1, beg):
            tp = 5 ** t
            for th in range(beg, end):
                thp = 3 ** th
                for s in range(beg, end):
                    sp = 7 ** s
                    num = tp * thp * sp
                    if "0" not in str(num):
                        string = stringify(num)
                        d[string] = d.get(string, []) + [[num, (0, th, t, s)]]

        # 3
        for t in range(beg_p, end):
            tp = 5 ** t
            for th in range(0, beg):
                thp = 3 ** th
                for s in range(beg, end):
                    sp = 7 ** s
                    num = tp * thp * sp
                    if "0" not in str(num):
                        string = stringify(num)
                        d[string] = d.get(string, []) + [[num, (0, th, t, s)]]

        # faces
        # 2
        for t in range(beg_p, end):
            tp = 5 ** t
            for th in range(0, beg):
                thp = 3 ** th
                for s in range(0, beg):
                    sp = 7 ** s
                    num = tp * thp * sp
                    if "0" not in str(num):
                        string = stringify(num)
                        d[string] = d.get(string, []) + [[num, (0, th, t, s)]]

        # 3
        for t in range(1, beg):
            tp = 5 ** t
            for th in range(beg, end):
                thp = 3 ** th
                for s in range(0, beg):
                    sp = 7 ** s
                    num = tp * thp * sp
                    if "0" not in str(num):
                        string = stringify(num)
                        d[string] = d.get(string, []) + [[num, (0, th, t, s)]]
        # 7
        for t in range(1, beg):
            tp = 5 ** t
            for th in range(0, beg):
                thp = 3 ** th
                for s in range(beg, end):
                    sp = 7 ** s
                    num = tp * thp * sp
                    if "0" not in str(num):
                        string = stringify(num)
                        d[string] = d.get(string, []) + [[num, (0, th, t, s)]]

        json_file = pjoin(self.output_dir, f"dict_f{end}.json")
        with open(json_file, "wb") as f:
            json.dump(d, f, indent=4)

        print(f"{json_file} saved")
        print(
            f"Searching from {beg} to {end} took {time.time() - tic} seconds to complete."
        )


if __name__ == "__main__":
    beg = 475
    end = 476
    old = f"output/dict_f{beg}.json"

    with open(old, "rb") as f:
        d_o = json.load(f)

    mpe = MPExplorer(d_o)
    mpe.expand_dict(beg, end)
