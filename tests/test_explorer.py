import pytest
import json
import os

from MultiplicativePersistence import Explorer, MpNumberCollection


class TestExplorer:
    def test_init(self):
        explorer = Explorer()

    def test_explore(self):
        # Expect an error to be raised if bad numbers are given
        with pytest.raises(Exception):
            # End is before beginning
            Explorer().explore(3, 1)
        with pytest.raises(Exception):
            # Negative numbers
            Explorer().explore(3, -1)

        former_json_path = "tests/fixtures/5-10.json"
        collection_former = MpNumberCollection(json_path=former_json_path)

        new_json_path = "tests/output/t5-10.json"
        os.remove(new_json_path)
        explorer = Explorer()
        explorer.explore(5, 10)
        collection = explorer.collection
        collection.write_json(new_json_path)

        with open(former_json_path) as f:
            former_json = json.load(f)
        with open(new_json_path) as f:
            new_json = json.load(f)

        assert former_json == new_json
