"""
attributes
        MpNumbers = [MpNumber, ...]
        digit_counts = [MpNumber.digit_count, ...]

    methods
        max_tree_height
        read_json(json_path)
        to_flat_json(json_path)
        to_tree_json(json_path)
        to_tsv(path)
        get(int)
        add(MPNumber or int)
        contains(MPNumber or int)
"""

import json

from MultiplicativePersistence import MpNumber, MpNumberVariant


class MpNumberCollection:
    def __init__(self):
        self.MpNumbers = []

    def count(self):
        return len(self.MpNumbers)

    def read_json(self, path):
        with open(path, "r") as f:
            mp_numbers = json.load(f)

        for digit_count, variant_list in mp_numbers.items():
            number = MpNumber(
                digit_count=digit_count,
                variants=[MpNumberVariant(*variant_l) for variant_l in variant_list],
            )
            self.MpNumbers.append(number)

        # for digit_count, variant_list in mp_numbers.items():
        #     number = MpNumber(digit_count=digit_count)

        #     for variant_l in variant_list:
        #         variant = MpNumberVariant(*variant_l)
        #         print(number)
        #         print(variant.digit_count)
        #         number.add_variant(variant)

        #     # variants=[MpNumberVariant(*variant_l) for variant_l in variant_list],

        #     self.MpNumbers.append(number)

        # ODNT FORGET ABOUT ME
        # for digit_count, variant_list in mp_numbers.items():

        #     # for variant_l in variant_list:
        #     #     variant =
        #     #     number.add_variant(variant)
