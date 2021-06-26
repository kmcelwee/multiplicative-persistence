from MultiplicativePersistence import MpNumberVariant, MpNumber


class TestMpNumber:
    def test_init(self):
        variant = MpNumberVariant(27648, (10, 3, 0, 0))
        number = MpNumber(variant)
        assert number.variants == [variant]
        assert number.digit_count == variant.digit_count

    def test_add_variant(self):
        # Ensure that only variants with identical digit counts can be added
        variant = MpNumberVariant(27648, (10, 3, 0, 0))
        number = MpNumber(variant)

        variant2 = MpNumberVariant(84672, (6, 3, 0, 2))
        number.add_variant(variant2)

        assert variant2 in number.variants
        assert len(number.variants) == 2

        variant3 = MpNumberVariant(5, (0, 0, 1, 0))
        assert variant3 not in number.variants
