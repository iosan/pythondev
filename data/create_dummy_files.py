import os


def create_dummy_files(base_folder: str):
    """
    Create dummy files with timestamp substrings in their names for testing date_parser.
    """
    os.makedirs(base_folder, exist_ok=True)
    subfolders = ["sub1", "sub2"]
    filenames = [
        "report_2024_10_15_12_34_56.txt",
        "backup_15_10_2024_12_34_56.log",
        "data_2023_05_01_08_00_00.csv",
        "log_01_05_2023_08_00_00.txt",
        "no_timestamp.txt",
    ]
    for sub in subfolders:
        sub_path = os.path.join(base_folder, sub)
        os.makedirs(sub_path, exist_ok=True)
        for fname in filenames:
            with open(os.path.join(sub_path, fname), "w") as f:
                f.write("dummy content\n")


if __name__ == "__main__":
    create_dummy_files("data")
