import pytest
import json
import os

from MultiplicativePersistence import MpNumberCollection, MpNumberVariant, MpNumber

FIXTURE_PATH = "tests/fixtures/5-10.json"
OUTPUT_PATH = "tests/output/5-10.json"


class TestMpNumberCollection:
    def test_init(self):
        collection = MpNumberCollection()
        assert collection.mp_numbers == {}

    def test_count(self):
        collection = MpNumberCollection()
        assert collection.count() == 0

    def test_read_json(self):
        collection = MpNumberCollection()
        collection.read_json(FIXTURE_PATH)

        assert collection.count() == 703

    def test_add(self):
        collection = MpNumberCollection()
        # Test add variant
        variant = MpNumberVariant(27648, (10, 3, 0, 0))
        collection.add(variant)
        assert variant.digit_count in collection.mp_numbers
        assert collection.get(variant.digit_count).variants == [variant]

        # Test when there is an existing mp_number
        variant2 = MpNumberVariant(84672, (6, 3, 0, 2))
        collection.add(variant2)
        assert variant2 in collection.get(variant.digit_count).variants
        assert collection.count() == 1

        # Ensure error is thrown when overwriting a mp_number

        # Test add number
        collection = MpNumberCollection()
        mp_number = MpNumber(variants=[variant])
        collection.add(mp_number)
        assert collection.count() == 1
        assert collection.mp_numbers == {mp_number.digit_count: mp_number}

        # Ensure that error is raised with unknown add type
        with pytest.raises(Exception):
            collection.add(1)

    def test_contains(self):
        collection = MpNumberCollection()
        assert not collection.contains("1,0,1,0,1,1,1,0")

        variant = MpNumberVariant(27648, (10, 3, 0, 0))
        collection.add(variant)
        assert collection.contains("1,0,1,0,1,1,1,0")

    def test_write_json(self):
        os.remove(OUTPUT_PATH)

        collection = MpNumberCollection()
        collection.read_json(FIXTURE_PATH)
        collection.write_json(OUTPUT_PATH)

        with open(FIXTURE_PATH, "r") as f:
            original_json = json.load(f)

        with open(OUTPUT_PATH, "r") as f:
            parsed_json = json.load(f)

        assert original_json == parsed_json
