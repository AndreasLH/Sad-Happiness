import os
import glob
import shutil
from tqdm import tqdm

def find_S_images(path):
    files = []
    for folder in glob.glob(path+os.sep+"*"):
        #print(folder)
        for name in glob.glob(folder + os.sep+"*S.JPG"):
            files.append(name)
    return files

def copy_images(new_path, file_paths):
    if not os.path.exists(new_path):
        os.makedirs(new_path)
        
    for src in tqdm(file_paths):
        shutil.copyfile(src, new_path+os.path.basename(src))

if __name__ == "__main__":
    path = os.getcwd() + os.sep+"KDEF_and_AKDEF" +os.sep +"KDEF"
    new_path = os.getcwd() + os.sep + "KDEF_Straight" + os.sep
    files = find_S_images(path)
    copy_images(new_path, files)
    
    