import unittest

from src.util import load_yaml_file


class TestConfig(unittest.TestCase):

    def setUp(self) -> None:
        self.file = 'config.yaml'

        self.dummy_config = {
            "foo": "bar",
            "dummy": False,
            "abc": 123,
        }

    def test_load_config_file(self):
        config = load_yaml_file(self.file)

        assert isinstance(config, dict)
        assert len(config.keys()) > 0

        with self.assertRaises(FileNotFoundError) as context:
            load_yaml_file('xyz')

    def test_config_value_types(self):
        assert isinstance(self.dummy_config['foo'], str)
        assert self.dummy_config['foo'] == 'bar'

        assert isinstance(self.dummy_config['dummy'], bool)
        assert self.dummy_config['dummy'] is False

        assert isinstance(self.dummy_config['abc'], int)
        assert self.dummy_config['abc'] == 123
