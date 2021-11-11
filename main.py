from typing import List
import pandas as pd
from pathlib import Path

from src.util import load_yaml_file
from src.web_transform import download_csv_files, cleanup, tf_data_to_output


def main(
        config_file: str
):
    # Load config values
    config = load_yaml_file(config_file)

    root_url = config['root_url']
    download_dir = config['download_directory']
    transform_config = config['tf']
    outfile_name = config['outfile_csv']

    # Download all CSV files from <root_url>
    files: List[str] = download_csv_files(root_url, download_dir)

    print(f'Downloaded {len(files)} files!')

    # transform each csv file and add it to list of frames
    frames: List[pd.DataFrame] = list()

    for file in files:
        print(f"Processing {file}")
        result: pd.DataFrame = tf_data_to_output(
            Path(file),
            selected_columns=transform_config['columns'],
            index=transform_config['index']
        )
        frames.append(result)

    print(f"Combining {len(frames)} and writing to output file: {outfile_name}")
    # Combine all the dataframes into one big ol'frame
    output_dataframe = pd.concat(frames)
    # Create CSV file, ignore the index
    output_dataframe.to_csv(outfile_name, index=False)

    print(f'Cleaning up files in {download_dir}')
    # clean up everything we did
    cleanup(download_dir)


if __name__ == '__main__':
    # Run main with our config
    main('config.yaml')
