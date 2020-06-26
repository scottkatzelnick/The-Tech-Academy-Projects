import os
import time

dir_path = input(
    "\nPlease either type out or copy and paste your directory path below:\n>>>:  "
)


def print_files():
    """
    This function will parse through a specific directory and
    return only the .txt file type absolute paths and their last
    modification time in local time.
    """
    dirs = os.listdir(dir_path)
    for files in dirs:
        os.path.join(dir_path, files)
        if files in dirs:
            catch = files.endswith("txt")
            while catch:
                txt_files = os.path.join(dir_path, files)
                time_files = time.ctime(os.path.getmtime(txt_files))
                print("\n{} @ {}".format(txt_files, time_files))
                catch = False


if __name__ == "__main__":
    print_files()
