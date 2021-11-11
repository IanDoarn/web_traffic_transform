from src.util import load_yaml_file


def main(
        config_file: str
):
    config = load_yaml_file(config_file)


if __name__ == '__main__':
    main()