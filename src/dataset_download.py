import os
import shutil
import kagglehub


def download_and_move_dataset(dataset_name, destination_path, expected_file):
    """
    Downloads a dataset from Kaggle Hub, moves the specified file to the destination,
    and optionally removes the source directory from the cache.

    Args:
        dataset_name (str): Name of the Kaggle dataset.
        destination_path (str): Path to the destination directory.
        expected_file (str): Name of the file to be moved.
    """

    path = kagglehub.dataset_download(dataset_name)
    file_to_move = os.path.join(path, expected_file)

    if os.path.exists(file_to_move):
        destination_file = os.path.join(destination_path, expected_file)
        if os.path.exists(destination_file):
            os.remove(destination_file)
        shutil.move(file_to_move, destination_path)
        print(f"File {expected_file} successfully moved to {destination_path}")

        shutil.rmtree(path)
        print("Source directory in cache removed")
    else:
        print(f"File {expected_file} not found in the downloaded dataset.")


current_dir = os.getcwd()
project_path = os.path.join(current_dir, '../data')
download_and_move_dataset('shivamb/netflix-shows', project_path, 'netflix_titles.csv')