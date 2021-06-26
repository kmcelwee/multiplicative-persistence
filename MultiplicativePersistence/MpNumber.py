class MpNumber:
    """The number as understood in MP analysis, meaning the only salient feature is digit count. As new base 10 variants are found, store them here."""

    def __init__(self, MpNumberVariant):
        self.digit_count = MpNumberVariant.digit_count
        self.variants = [MpNumberVariant]

    # NOTE: We do not check for duplicates.
    def add_variant(self, MpNumberVariant):
        assert (
            MpNumberVariant.digit_count == self.digit_count
        ), "Only MpNumberVariants with identical digit counts can be added as a variant"
        self.variants.append(MpNumberVariant)
