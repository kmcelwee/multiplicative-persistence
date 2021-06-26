import pytest

from MultiplicativePersistence import MpNumberVariant


class TestMpNumberVariant:
    def test_base_10(self):
        variant = MpNumberVariant(5, (0, 0, 1, 0))
        assert variant.base_10 == 5
        assert variant.two_power == 0
        assert variant.three_power == 0
        assert variant.five_power == 1
        assert variant.seven_power == 0

    def test_str(self):
        variant = MpNumberVariant(5, (0, 0, 1, 0))
        assert str(variant) == "2^0 * 3^0 * 5^1 * 7^0"

    def test_digit_count(self):
        assert MpNumberVariant.digit_count(1) == "0,0,0,0,0,0,0,0"
        assert MpNumberVariant.digit_count(3268642167) == "2,1,1,0,3,1,1,0"

        variant = MpNumberVariant(27648, (10, 3, 0, 0))
        variant.digit_count == "1,0,1,0,1,1,1,0"
