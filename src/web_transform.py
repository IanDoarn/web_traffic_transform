import os
from typing import List, Any
from pathlib import Path
import pandas as pd

from src.util import download_file_from_url, generate_file_paths


def download_csv_files(
        root_url: str,
        directory: str,
        create_directory_if_missing: bool = True
) -> List[str]:
    """
    Download a set of CSV files into a directory.

    If a directory is not supplied use the default directory

    :param root_url: Root URL where files are stored
    :type root_url: str
    :param directory: Directory to use for files
    :type directory: str
    :param create_directory_if_missing: Whether or not to make the directory for downloading if
                                        is it missing
    :type create_directory_if_missing: bool
    :return: List of files (path/to/file) downloaded
    :rtype: List[str]
    """

    file_urls: List[str] = generate_file_paths(root_url)
    downloaded_files: List[str] = list()

    # make sure working directory exists
    if not os.path.isdir(directory):
        if create_directory_if_missing:
            os.mkdir(directory)
        else:
            raise NotADirectoryError(f'{directory} does not exist')

    for url in file_urls:
        out_file = Path(directory) / url.split('/')[-1]
        print(f'Downloading {url} into {out_file}')
        download_file_from_url(url, out_file)
        downloaded_files.append(str(out_file))

    return downloaded_files


def cleanup(directory: str) -> None:
    """
    Remove all files downloaded

    :param directory: Directory we downloaded files into
    :return: None
    """
    for file in os.listdir(directory):
        _file = os.path.join(directory, file)
        if os.path.isfile(_file):
            os.remove(_file)
    os.rmdir(directory)


def tf_data_to_output(
    csv_file: Path,
    selected_columns: List[str],
    index: str
) -> pd.DataFrame:
    """
    Transform data into the required output format.

    Per requirements:

    Output contains one row for each user_id and has columns populated
     with the length of time each user spent on each path.

    :param csv_file: File to transform
    :type csv_file: Path
    :param selected_columns: Columns to use in initial grouping
    :type selected_columns: List[str]
    :param index: index column to use for pivot
    :type index: str
    :return: Transformed data
    :rtype: pd.DataFrame
    """

    df = pd.read_csv(str(csv_file))
    grouped = df[selected_columns].groupby(by=["user_id", "path"]).sum()

    # https://stackoverflow.com/questions/49405336/pivoting-pandas-with-removal-of-some-headers-and-renaming-of-some-indexes
    result = pd.pivot_table(
        grouped,
        index=index,
        columns='path',
        aggfunc=sum,
        values='length'
    )

    # Remove the extra headers from pivot table, rename axis to nothing
    # to ensure output is correct
    return result.reset_index().rename_axis(None)
