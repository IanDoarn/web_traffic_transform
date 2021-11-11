from typing import List
from pandas import DataFrame
from pathlib import Path

from src.util import load_yaml_file
from src.web_transform import download_csv_files, cleanup, tf_data_to_output


def main(
        config_file: str
):
    # Load config
    config = load_yaml_file(config_file)

    root_url = config['root_url']
    download_dir = config['download_directory']
    transform_config = config['tf']

    # clean up before we start
    cleanup(download_dir)

    # Download all CSV files from <root_url>
    files: List[str] = download_csv_files(root_url, download_dir)

    print(f'Downloaded {len(files)} into {download_dir}!')

    # transform each csv file
    for file in files:
        result: DataFrame = tf_data_to_output(
            Path(file),
            selected_columns=transform_config['columns'],
            index=transform_config['index']
        )
        print(result)

    print(f'Cleaning up files in {download_dir}')
    # clean up everything we did
    cleanup(download_dir)



if __name__ == '__main__':
    main('config.yaml')
