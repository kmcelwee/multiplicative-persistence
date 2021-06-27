from MultiplicativePersistence import MpNumberCollection

FIXTURE_PATH = "tests/fixtures/5-10.json"


class TestMpNumberCollection:
    def test_init(self):
        collection = MpNumberCollection()
        assert collection.MpNumbers == []

    def test_count(self):
        collection = MpNumberCollection()
        assert collection.count() == 0

    def test_read_json(self):
        collection = MpNumberCollection()
        collection.read_json(FIXTURE_PATH)

        assert collection.count() == 703
