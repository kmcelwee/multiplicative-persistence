import pytest

from MultiplicativePersistence import MpNumberVariant, MpNumber


class TestMpNumber:
    def test_init(self):
        variant = MpNumberVariant(27648, (10, 3, 0, 0))
        number = MpNumber(variants=[variant])
        assert number.variants == [variant]
        assert number.digit_count == variant.digit_count

        # Test blank init
        empty_number = MpNumber()
        assert empty_number.digit_count == None
        assert empty_number.variants == []

    def test_str(self):
        variant = MpNumberVariant(27648, (10, 3, 0, 0))
        number = MpNumber(variants=[variant])
        assert str(number) == "1,0,1,0,1,1,1,0: [2^10 * 3^3 * 5^0 * 7^0]"

        variant2 = MpNumberVariant(84672, (6, 3, 0, 2))
        number.add_variant(variant2)
        assert (
            str(number)
            == "1,0,1,0,1,1,1,0: [2^10 * 3^3 * 5^0 * 7^0, 2^6 * 3^3 * 5^0 * 7^2]"
        )

    def test_add_variant(self):
        # Ensure that only variants with identical digit counts can be added
        variant = MpNumberVariant(27648, (10, 3, 0, 0))
        number = MpNumber(variants=[variant])

        variant2 = MpNumberVariant(84672, (6, 3, 0, 2))
        number.add_variant(variant2)

        assert variant2 in number.variants
        assert len(number.variants) == 2

        variant3 = MpNumberVariant(5, (0, 0, 1, 0))
        with pytest.raises(Exception):
            number.add_variant(variant3)
