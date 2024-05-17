import argparse
import os

def load_files_in_folder(folder_path):
    try:
        # List all files in the directory
        files = os.listdir(folder_path)
        
        # Filter out directories, only keep files
        files = [f for f in files if os.path.isfile(os.path.join(folder_path, f))]
        
        if files:
            print(f"Files in '{folder_path}':")
            for file in files:
                print(file)
        else:
            print(f"No files found in '{folder_path}'.")

    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    # Create argument parser
    parser = argparse.ArgumentParser(description='Load all files in a specified folder.')
    parser.add_argument('folder', type=str, help='Path to the folder')

    # Parse arguments
    args = parser.parse_args()

    # Call the function to load files
    load_files_in_folder(args.folder)

if __name__ == '__main__':
    main()