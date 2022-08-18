from pathlib import Path
import os
def create_file(file_name, extension):
    if os.path.isfile(f"{file_name}.{extension}"):
        return "File already exists"
    else:
        newfile = open(f"{file_name}.{extension}", 'w')
        newfile.close()
        return (Path(f"{file_name}.{extension}").absolute())
