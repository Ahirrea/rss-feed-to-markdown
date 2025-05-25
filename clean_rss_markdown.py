import os
import shutil
import sys

def clean_folder_contents(folder_path):
    """
    Deletes all files and subdirectories within the given folder_path,
    but not the folder_path itself.
    """
    if not os.path.isdir(folder_path):
        print(f"Error: Folder '{folder_path}' not found. Current CWD: {os.getcwd()}")
        # Attempt to list CWD contents for debugging
        try:
            print(f"Contents of CWD ({os.getcwd()}): {os.listdir('.')}")
        except Exception as e:
            print(f"Could not list CWD contents: {e}")
        sys.exit(1) # Exit if folder not found

    print(f"Cleaning contents of '{folder_path}'...")
    for item_name in os.listdir(folder_path):
        item_path = os.path.join(folder_path, item_name)
        try:
            if os.path.isfile(item_path) or os.path.islink(item_path):
                os.remove(item_path)
                print(f"Deleted file: {item_path}")
            elif os.path.isdir(item_path):
                shutil.rmtree(item_path)
                print(f"Deleted directory: {item_path}")
        except Exception as e:
            print(f"Error deleting {item_path}: {e}")
    print(f"Finished cleaning contents of '{folder_path}'.")

if __name__ == "__main__":
    # Assuming the script is in /app and rss_markdown is also in /app
    script_dir = os.path.dirname(os.path.abspath(__file__))
    target_folder_name = "rss_markdown"
    # Construct the absolute path to the rss_markdown folder
    target_folder_path = os.path.join(script_dir, target_folder_name)
    
    clean_folder_contents(target_folder_path)
