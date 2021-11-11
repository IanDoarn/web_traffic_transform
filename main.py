from src.util import load_yaml_file
from src.web_transform import download_csv_files, cleanup


def main(
        config_file: str
):
    # Load config
    config = load_yaml_file(config_file)

    root_url = config['root_url']
    download_dir = config['download_directory']

    # clean up before we start
    cleanup(download_dir)

    # Download all CSV files from <root_url>
    files = download_csv_files(root_url, download_dir)

    print(f'Downloaded {len(files)} into {download_dir}!')

    print(f'Cleaning up files in {download_dir}')
    # clean up everything we did
    cleanup(download_dir)



if __name__ == '__main__':
    main('config.yaml')
