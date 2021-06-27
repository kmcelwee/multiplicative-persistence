class MpNumber:
    """The number as understood in MP analysis, meaning the only salient feature is digit count. As new base 10 variants are found, store them here."""

    def __init__(self, variants=[], digit_count=None):
        self.digit_count = digit_count
        self.variants = variants

        if variants:
            self.digit_count = variants[0].digit_count

    def __str__(self):
        return f"{self.digit_count}: {self.variants}"

    def __repr__(self):
        return str(self)

    # NOTE: We do not check for duplicates.
    def add_variant(self, variant):
        if self.digit_count is None:
            self.digit_count = variant.digit_count

        assert (
            variant.digit_count == self.digit_count
        ), f"Only variants with identical digit counts can be added as a variant. {variant.digit_count} != {self.digit_count}"

        self.variants.append(variant)
