import shutil
import os
import config 

def cleanup_downloads(dir_path: str = config.DOWNLOAD_DIR):
    try:
        shutil.rmtree(dir_path)
        print(f"Directory and all contents at '{dir_path}' removed successfully.")
    except FileNotFoundError:
        print(f"Error: Directory '{config.DOWNLOAD_DIR}' not found.")
    except OSError as e:
        print(f"Error: {e}")