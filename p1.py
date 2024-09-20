import zipfile
import os

def backup_folder_to_zip(folder_path, zip_filename):
    # Check if the folder exists
    if not os.path.exists(folder_path):
        print(f"The folder '{folder_path}' does not exist.")
        return

    # Create a ZIP file for backup
    with zipfile.ZipFile(zip_filename, 'w', zipfile.ZIP_DEFLATED) as backup_zip:
        # Walk through each folder, subfolder, and file in the directory tree
        for foldername, subfolders, filenames in os.walk(folder_path):
            # Add the current folder to the ZIP archive
            backup_zip.write(foldername, os.path.relpath(foldername, folder_path))
            # Add all files in this folder to the ZIP archive
            for filename in filenames:
                file_path = os.path.join(foldername, filename)
                backup_zip.write(file_path, os.path.relpath(file_path, folder_path))
    print(f"Backup of '{folder_path}' created as '{zip_filename}'.")

if _name_ == "_main_":
    # Specify the folder to be backed up and the name of the ZIP file
    folder_to_backup = r'E:\Desktop\Sem 2 2023-2027 batch\programs\New folder'  # Replace 'your_folder_path' with the actual path to the folder you want to back up
    backup_filename = 'backup.zip'

    # Call the backup function
    backup_folder_to_zip(folder_to_backup, backup_filename)
