import os
import shutil
import kagglehub

# Download latest version
path = kagglehub.dataset_download('shivamb/netflix-shows')

# Define target path
current_dir = os.getcwd()
project_path = os.path.join(current_dir, '../data')

# Check if any files were downloaded
downloaded_files = os.listdir(path)

if downloaded_files:
    # Move the downloaded file
    file_to_move = os.path.join(path, downloaded_files[0])
    shutil.move(file_to_move, project_path)
else:
    print('No files downloaded from KaggleHub')
