import pytest

from MultiplicativePersistence import Explorer


class TestExplorer:
    def test_init(self):
        explorer = Explorer(3, 5)
        assert explorer.start == 3
        assert explorer.end == 5

        # Expect an error to be raised if bad numbers are given
        with pytest.raises(Exception):
            # End is before beginning
            Explorer(3, 1)
        with pytest.raises(Exception):
            # Negative numbers
            Explorer(3, -1)
