import time

from MultiplicativePersistence import MpNumberCollection, MpNumberVariant


class SpeedyExplorer:
    def __init__(self):
        self.collection = MpNumberCollection()
        self.run_time = None

    def explore(self, start, end):
        """There are two cubes that need to be expanded: 2^x, 3^y, 7^z and 3^x, 5^y, and 7^z"""
        assert start < end, "start value must be less than end value"
        assert 0 <= start < end, "start and end values must be greater than 0"

        tic = time.time()

        # The 2, 3, 7 search space.
        prisms = [
            # [2 range, 3 range, 7 range],
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
                            self.collection.add(MpNumberVariant(num, [t, th, 0, s]))

        ##
        # The 5, 3, 7 search space.
        # We've already searched when 5 to the zeroeth power, so we can skip it here.
        for prism in prisms:
            # If the five line (first index 0) starts (second index 0) at zero, set it to 1.
            if prism[0][0] == 0:
                prism[0][0] = 1

        for prism in prisms:
            for t in range(*prism[0]):
                tp = 5 ** t
                for th in range(*prism[1]):
                    thp = 3 ** th
                    for s in range(*prism[2]):
                        sp = 7 ** s
                        num = tp * thp * sp
                        if "0" not in str(num):
                            self.collection.add(MpNumberVariant(num, [0, th, t, s]))

        self.run_time = round(time.time() - tic, 2)
