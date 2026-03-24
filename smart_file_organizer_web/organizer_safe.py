import os
import shutil
import sys
from file_types import file_types

path=input("Enter folder that is to be organized")
if not os.path.exists(path):
    print("Folder does not exist!!!!!!!")
    sys.exit()
files=os.listdir(path)
#print("Files detected:", files)
count = 0
for f in files:
    file_path=os.path.join(path,f)
    #If it is a folder just skip it
    if not os.path.isfile(file_path):
        continue
    ext=os.path.splitext(f)[1].lower()
    #print("Checking:", f, "Extension:", ext)
    moved=False
    for folder,extensions in file_types.items():
        if ext in extensions:
            folder_path=os.path.join(path, folder)
            os.makedirs(folder_path, exist_ok=True)
            destination=os.path.join(folder_path, f)
            # Prevent overwrite
            if os.path.exists(destination):
                print(f"Skipped {f} (already exists)")
                continue
            shutil.move(file_path, destination)
            print(f"Moved {f} → {folder}")
            count+=1
            moved=True
            break
    if not moved:
        other_path = os.path.join(path,"Others")
        os.makedirs(other_path,exist_ok=True)
        destination=os.path.join(other_path, f)
        if os.path.exists(destination):
            print(f"Skipped {f} (already exists)")
            continue
        shutil.move(file_path, destination)
        print(f"Moved {f} → Others")
        count+= 1
print("\nTotal files moved:", count)

    