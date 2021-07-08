import json

from MultiplicativePersistence import Explorer, ExplorerRefactor, MpNumberCollection


class TestExplorerRefactor:
    def test_init(self):
        explorer = ExplorerRefactor()
        assert type(explorer.collection) == MpNumberCollection

    def test_explorer_refactor(self):
        explorer_og = Explorer()
        explorer_og.explore(5, 10)

        explorer_refactor = ExplorerRefactor()
        explorer_refactor.explore(5, 10)

        assert (
            explorer_refactor.collection.to_dict() == explorer_og.collection.to_dict()
        )
