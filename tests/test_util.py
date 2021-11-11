import unittest
from unittest.mock import patch, MagicMock, mock_open
from pathlib import Path

import src.util


class TestUtils(unittest.TestCase):

    def setUp(self) -> None:
        self.url = 'http://foo.com/file.csv'
        self.out_file = Path('file.csv')

        self.opener = mock_open()

    def mocked_open(self, *args, **kwargs):
        return self.opener(self, *args, **kwargs)

    @patch('src.util.request')
    def test_download_file_from_url(self, *args):
        with patch.object(src.util.Path, 'open', self.mocked_open) as mock_file:
            src.util.download_file_from_url(self.url, self.out_file)

    @patch('src.util.request')
    def test_download_file_from_url_empty_params(self, *args):
        with self.assertRaises(TypeError) as context:
            src.util.download_file_from_url(self.url, 'file.csv')

        with self.assertRaises(TypeError) as context:
            src.util.download_file_from_url(None, Path(''))

    @patch("src.util.yaml.safe_load")
    def test_load_yaml_file(self, mock_safe_load):

        data: dict = {
            'foo': 'bar'
        }

        mock_safe_load.return_value = data
        with patch('builtins.open', new_callable=mock_open()) as m:
            result = src.util.load_yaml_file('foo.yaml')

        assert isinstance(result, dict)
        assert result == data

    def test_generate_file_paths(self):
        root_url: str = 'http://foo.com/'

        paths = src.util.generate_file_paths(root_url)

        assert len(paths) == 26
        assert paths[0] == f"{root_url}a.csv"
