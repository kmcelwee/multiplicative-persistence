from MultiplicativePersistence import Tree, MpNumberCollection


class TestTree:
    def test_init(self):
        collection = MpNumberCollection(json_path="tests/fixtures/5-10.json")
        tree = Tree(collection)
        assert tree.collection == collection
