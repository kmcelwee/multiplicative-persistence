import time

from MultiplicativePersistence import MpNumberCollection, MpNumberVariant


class ExplorerRefactor:
    def __init__(self):
        self.collection = MpNumberCollection()

    def explore(self, start, end):
        """There are two cubes that need to be expanded: 2^x, 3^y, 7^z and 3^x, 5^y, and 7^z"""
        assert start < end, "start value must be less than end value"
        assert 0 <= start < end, "start and end values must be greater than 0"

        tic = time.time()

        # The 2, 3, 7 search space.
        prisms = [
            # expanded cube
            [[start, end], [start, end], [start, end]],
            # longs
            [[start, end], [start, end], [0, start]],
            [[0, start], [start, end], [start, end]],
            [[start, end], [0, start], [start, end]],
            # faces
            [[start, end], [0, start], [0, start]],
            [[0, start], [start, end], [0, start]],
            [[0, start], [0, start], [start, end]],
        ]

        for prism in prisms:
            for t in range(*prism[0]):
                tp = 2 ** t
                for th in range(*prism[1]):
                    thp = 3 ** th
                    for s in range(*prism[2]):
                        sp = 7 ** s
                        num = tp * thp * sp
                        if "0" not in str(num):
                            self.collection.add(MpNumberVariant(num, (t, th, 0, s)))

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
                        self.collection.add(MpNumberVariant(num, (0, th, t, s)))

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
                        self.collection.add(MpNumberVariant(num, (0, th, t, s)))

        # 2
        for t in range(1, start):
            tp = 5 ** t
            for th in range(start, end):
                thp = 3 ** th
                for s in range(start, end):
                    sp = 7 ** s
                    num = tp * thp * sp
                    if "0" not in str(num):
                        self.collection.add(MpNumberVariant(num, (0, th, t, s)))

        # 3
        for t in range(beg_p, end):
            tp = 5 ** t
            for th in range(0, start):
                thp = 3 ** th
                for s in range(start, end):
                    sp = 7 ** s
                    num = tp * thp * sp
                    if "0" not in str(num):
                        self.collection.add(MpNumberVariant(num, (0, th, t, s)))

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
                        self.collection.add(MpNumberVariant(num, (0, th, t, s)))
        # 3
        for t in range(1, start):
            tp = 5 ** t
            for th in range(start, end):
                thp = 3 ** th
                for s in range(0, start):
                    sp = 7 ** s
                    num = tp * thp * sp
                    if "0" not in str(num):
                        self.collection.add(MpNumberVariant(num, (0, th, t, s)))
        # 7
        for t in range(1, start):
            tp = 5 ** t
            for th in range(0, start):
                thp = 3 ** th
                for s in range(start, end):
                    sp = 7 ** s
                    num = tp * thp * sp
                    if "0" not in str(num):
                        self.collection.add(MpNumberVariant(num, (0, th, t, s)))
