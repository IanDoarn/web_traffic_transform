import os
from typing import Dict, List
from urllib import request
from pathlib import Path
import yaml


def download_file_from_url(
        url: str,
        file_name: Path
) -> None:
    """
    Download a file from a give url.

    Uses below implementation since relative size of each file being
    downloaded is below 500kb on average.

    Reference: https://stackoverflow.com/questions/7243750/download-file-from-web-in-python-3

    :param url: URL of the file to be downloaded
    :type url: str
    :param file_name: Name or Path/Name of the file to save
    :type file_name: Path
    :return: None
    """
    if url is None:
        raise TypeError('param (url) can not be None.')

    if not isinstance(file_name, Path):
        raise TypeError(f'param (file_name) must be {str(Path)} not {type(file_name)}')

    with request.urlopen(url) as response:
        data = response.read()

    with file_name.open(mode='wb') as file:
        file.write(data)


def load_yaml_file(file: str) -> Dict[str, str]:
    """
    Load a yaml file, return its value as a Dict

    :param file: File to open
    :type file: str
    :return: Dict[str, str]
    """
    # Read YAML file
    with open(file, 'r') as stream:
        data = yaml.safe_load(stream)
    return data


def generate_file_paths(root_url: str) -> List[str]:
    """
    Return list of all files to be downloaded

    :param root_url: base url where files are stored
    :type root_url: str
    :return: List of files
    :rtype: List[str]
    """
    return [
        os.path.join(root_url, f"{chr(x)}.csv") for x in range(ord('a'), ord('z') + 1)
    ]
