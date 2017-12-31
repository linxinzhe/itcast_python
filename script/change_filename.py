import os

dir="."

suffix=".txt"
new_suffix=".java"

for file in os.listdir(dir):
    file_path=os.path.join(dir,file)
    if os.path.isfile(file_path) and file.endswith(suffix):
        new_filename=file[:file.index(suffix)]+new_suffix
        os.rename(file_path,os.path.join(dir,new_filename))
