import os
import glob
import shutil

def find_S_images(path):
    files = []
    for folder in glob.glob(path+"\\*"):
        #print(folder)
        for name in glob.glob(folder + "\\*S.JPG"):
            files.append(name)
    return files

def copy_images(new_path, file_paths):
    if not os.path.exists(new_path):
        os.makedirs(new_path)
        
    #print(new_path)
    #print(file_paths[0])
    #print(os.path.basename(file_paths[0]))
    for src in file_paths:
        shutil.copyfile(src, new_path+os.path.basename(src))

if __name__ == "__main__":
    path = os.getcwd() + "\\KDEF_and_AKDEF\\KDEF"
    new_path = os.getcwd() + "\\KDEF_Straight\\"
    files = find_S_images(path)
    copy_images(new_path, files)
    
    