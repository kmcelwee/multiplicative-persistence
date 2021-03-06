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

    def test_to_list(self):
        variant = MpNumberVariant(5, (0, 0, 1, 0))
        assert variant.to_list() == [5, (0, 0, 1, 0)]

    def test_prime_factor(self):
        assert MpNumberVariant.prime_factor(n=27648) == [
            2,
            2,
            2,
            2,
            2,
            2,
            2,
            2,
            2,
            2,
            3,
            3,
            3,
        ]
        assert MpNumberVariant.prime_factor(n=27648, collapse=True) == [10, 3, 0, 0]

        assert MpNumberVariant.prime_factor(n=4723) == []

    def test_collapse_prime_factor(self):
        prime_factorization = MpNumberVariant.prime_factor(27648)
        assert MpNumberVariant._collapse_prime_factor(prime_factorization) == [
            10,
            3,
            0,
            0,
        ]
