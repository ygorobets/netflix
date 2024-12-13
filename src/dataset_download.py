import os
import shutil
import kagglehub

path = kagglehub.dataset_download('shivamb/netflix-shows')

current_dir = os.getcwd()
project_path = os.path.join(current_dir, '../data')

expected_file = 'netflix_titles.csv'
file_to_move = os.path.join(path, expected_file)

if os.path.exists(os.path.join(project_path, expected_file)):
    os.remove(os.path.join(project_path, expected_file))
    shutil.move(file_to_move, project_path)
    print(f'File {expected_file} successfully overwritten in {project_path}')
else:
    shutil.move(file_to_move, project_path)
    print(f'File {expected_file} successfully moved to {project_path}')
