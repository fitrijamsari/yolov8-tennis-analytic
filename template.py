from pathlib import Path

list_of_files = [
    f"src/__init__.py",
    f"src/logging_conf.yaml",
    f"src/main.py",
    f"src/utils/__init__.py",
    f"src/utils/common.py",
    "config/__init__.py",
    "config/config.yaml",
    "img/.gitkeep",
    "input/.gitkeep",
    "output/.gitkeep",
    "models/.gitkeep",
    "training/.gitkeep",
    "logs/.gitkeep",
    "research/trials.ipynb",
    "research/test.py",
    ".gitignore",
    ".env",
    "requirements.txt",
    "setup.py",
    "README.md",
]


def create_file(list_of_files: list) -> None:
    for filepath in list_of_files:
        filepath = Path(filepath)
        if not filepath.exists() or filepath.stat().st_size == 0:
            filedir = filepath.parent
            if filedir != Path():
                filedir.mkdir(parents=True, exist_ok=True)
                print(f"Creating directory; {filedir} for the file: {filepath.name}")

            if not filepath.exists():
                filepath.touch()
                print(f"Creating empty file: {filepath}")
            else:
                print(f"{filepath.name} already exists")
        else:
            print(f"{filepath.name} is already exists")


def main():
    create_file(list_of_files)


if __name__ == "__main__":
    main()
