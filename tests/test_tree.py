from anytree import Node, RenderTree

from MultiplicativePersistence import Tree, MpNumberCollection


class TestTree:
    def test_init(self):
        collection = MpNumberCollection(json_path="tests/fixtures/5-10.json")
        tree = Tree(collection)
        assert tree.collection == collection

    def test_get_number_child(self):
        assert Tree.get_number_child(81) == 8
        assert Tree.get_number_child(2231) == 12
        assert Tree.get_number_child(88341) == 768

    def test_get_mp_list(self):
        assert Tree.get_mp_list(18432) == [8, 18, 192, 18432]
        assert Tree.get_mp_list(0) == [0]

    def test_add_child(self):
        collection = MpNumberCollection(json_path="tests/fixtures/5-10.json")
        tree = Tree(collection)
        tree.add_child(15)
        five_root = tree.get_node(5)
        assert five_root.children[0].name == 15

        tree.add_child(1176)
        eight_root = tree.get_node(8)
        assert eight_root.children[0].name == 42

        tree.add_child(177147)

        implicit_node = tree.get_node(1372)
        assert implicit_node.name == 1372
        assert implicit_node.parent.name == 42

        root_42 = tree.get_node(42)
        assert len(root_42.children) == 2
