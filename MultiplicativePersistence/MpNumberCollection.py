"""
attributes
        MpNumbers = [MpNumber, ...]
        digit_counts = [MpNumber.digit_count, ...]

    methods
        max_tree_height
        to_flat_json(json_path)
        to_tree_json(json_path)
        to_tsv(path)
"""

import json

from MultiplicativePersistence import MpNumber, MpNumberVariant


class MpNumberCollection:
    def __init__(self, json_path=None):
        self.mp_numbers = {}
        if json_path:
            self.read_json(json_path)

    def count(self):
        return len(self.mp_numbers.keys())

    def get(self, digit_count):
        return self.mp_numbers.get(digit_count)

    def contains(self, digit_count):
        return not self.mp_numbers.get(digit_count) is None

    def add(self, variant_or_mp_number):
        if type(variant_or_mp_number) == MpNumberVariant:
            mp_number = self.get(variant_or_mp_number.digit_count)
            if mp_number:
                mp_number.add_variant(variant_or_mp_number)
            else:
                new_mp_number = MpNumber(variants=[variant_or_mp_number])
                self.mp_numbers[variant_or_mp_number.digit_count] = new_mp_number
        elif type(variant_or_mp_number) == MpNumber:
            if self.get(variant_or_mp_number.digit_count):
                raise Exception("Warning: you're overwriting a MpNumber!")
            self.mp_numbers[variant_or_mp_number.digit_count] = variant_or_mp_number
        # TODO: elif type == int
        else:
            raise Exception("Unknown type being added to collection.")

    def all_variants(self):
        """Return all the number variants contained within the collection"""
        variants = []
        for digit_count, mp_number in self.mp_numbers.items():
            variants.extend(mp_number.variants)
        return variants

    def read_json(self, path):
        with open(path, "r") as f:
            mp_numbers = json.load(f)

        for digit_count, variant_list in mp_numbers.items():
            for variant_l in variant_list:
                self.add(MpNumberVariant(*variant_l))

    def write_json(self, path):
        output_json = {}
        for digit_count, mp_number in self.mp_numbers.items():
            output_json[digit_count] = [
                variant.to_list() for variant in mp_number.variants
            ]

        with open(path, "w") as f:
            json.dump(output_json, f, indent=4)
