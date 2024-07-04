import os
import shutil
import sys
from datetime import datetime

def backup_files(source_dir, destination_dir):
    # Check if the source directory exists
    if not os.path.exists(source_dir):
        print(f"Error: Source directory '{source_dir}' does not exist.")
        return

    # Check if the destination directory exists, create it if it doesn't
    if not os.path.exists(destination_dir):
        try:
            os.makedirs(destination_dir)
        except OSError as e:
            print(f"Error: Could not create destination directory '{destination_dir}'. {e}")
            return

    # Iterate over all files in the source directory
    for filename in os.listdir(source_dir):
        source_file = os.path.join(source_dir, filename)
        destination_file = os.path.join(destination_dir, filename)

        if os.path.isfile(source_file):
            # If the file already exists in the destination directory, append a timestamp
            if os.path.exists(destination_file):
                timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
                name, ext = os.path.splitext(filename)
                destination_file = os.path.join(destination_dir, f"{name}_{timestamp}{ext}")

            # Copy the file
            try:
                shutil.copy2(source_file, destination_file)
                print(f"Copied '{source_file}' to '{destination_file}'")
            except IOError as e:
                print(f"Error: Could not copy '{source_file}' to '{destination_file}'. {e}")

def main():
    if len(sys.argv) != 3:
        print("Usage: python backup.py /path/to/source /path/to/destination")
        return

    source_dir = sys.argv[1]
    destination_dir = sys.argv[2]

    backup_files(source_dir, destination_dir)

if __name__ == "__main__":
    main()
