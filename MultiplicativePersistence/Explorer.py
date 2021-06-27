class Explorer:
    def __init__(self, start, end):
        assert start < end, "start value must be less than end value"
        assert 0 <= start < end, "start and end values must be greater than 0"

        self.start = start
        self.end = end
