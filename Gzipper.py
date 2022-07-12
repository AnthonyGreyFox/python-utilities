import shutil
import easygui
import gzip
import pathlib
import os


def nav():
    path = easygui.diropenbox()
    return path


def gzipper():
    target_dir = pathlib.Path(nav())
    for file in target_dir.iterdir():
        # Skip directories
        if file.is_dir():
            continue
        ext = os.path.splitext(file)[-1].lower()
        with file.open('rb') as f_in:
            with gzip.open(str(file.with_suffix(f"{ext}.gz")), 'wb') as f_out:
                shutil.copyfileobj(f_in, f_out)


if __name__ == '__main__':
    gzipper()
