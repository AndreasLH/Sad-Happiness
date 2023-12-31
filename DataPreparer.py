import os
import glob
import shutil
from tqdm import tqdm
import cv2

def find_S_images(path):
    files = []
    for folder in glob.glob(os.path.expanduser(path+os.sep + "*")):
        for name in glob.glob(folder + os.sep + "*S.JPG"):
            files.append(name)
    return files

def copy_images(new_path, file_paths, generate_pca=False):
    if not os.path.exists(new_path):
        os.makedirs(new_path)
    print("Copying images...")  
    for src in tqdm(file_paths):
        shutil.copyfile(src, new_path+os.path.basename(src)) # Copy original image for presentation
        if generate_pca:
            img_rgb = cv2.imread(src) # Save another copy for PCA analysis
            img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY) # Convert copy to grayscale
            scale_percent = 50 # percent of original size
            width = int(img_gray.shape[1] * scale_percent / 100)
            height = int(img_gray.shape[0] * scale_percent / 100)
            dim = (width, height)
            img_reduced = cv2.resize(img_gray, dim, interpolation = cv2.INTER_AREA) # Reduce image size by half

            cv2.imwrite(new_path+os.path.basename(src)[:-4]+"_pca.JPG", img_reduced)
        
        
def prune_images(new_path):
    '''
    OBS: This method is hard-coded to remove certain images.
    If the files are renamed after copying, this will not work!
    '''
    
    to_remove = [
        'BM29SUS.JPG', 'BM29NES.JPG', 'BM27SAS.JPG',
        'BM26AFS.JPG', 'BM24DIS.JPG', 'BM22SAS.JPG',
        'BM20SAS.JPG', 'BM20NES.JPG', 'BM20ANS.JPG',
        'BM20AFS.JPG', 'BM19NES.JPG', 'BM19ANS.JPG',
        'BM18NES.JPG', 'BM17NES.JPG', 'BM15SUS.JPG',
        'BM15NES.JPG', 'BM15HAS.JPG', 'BM04AFS.JPG',
        'BM02ANS.JPG', 'BM01DIS.JPG', 'BM01HAS.JPG',
        'BM01DIS.JPG', 'BF18SUS.JPG', 'BF18SAS.JPG',
        'BF18DIS.JPG', 'BF11SUS.JPG', 'BF08SAS.JPG',
        'BF08DIS.JPG', 'AM30SAS.JPG', 'AM28HAS.JPG',
        'AM26DIS.JPG', 'AM26AFS.JPG', 'AM24NES.JPG',
        'AM20SAS.JPG', 'AM20NES.JPG', 'AM19NES.JPG',
        'AM16NES.JPG', 'AM15ANS.JPG', 'AM12SAS.JPG',
        'AM12NES.JPG', 'AM12ANS.JPG', 'AM03SAS.JPG',
        'AF18SUS.JPG', 'AF18SAS.JPG', 'AF18DIS.JPG',
        'AF18AFS.JPG', 'AF08SAS.JPG', 'AF08DIS.JPG'
    ]
    print("Pruning images...")
    for file in tqdm(os.listdir(new_path)):
        if file in to_remove:
            os.remove(os.path.join(new_path, file))
            try:
                os.remove(os.path.join(new_path, file[:-4]+"_pca.JPG"))
            except:
                continue
    
if __name__ == "__main__":
    path = os.getcwd() + os.sep + "KDEF_and_AKDEF"+ os.sep + "KDEF"
    new_path = os.getcwd() + os.sep + "KDEF_Straight" + os.sep
    print(f"new_path: {new_path}")
    files = find_S_images(path)
    copy_images(new_path, files)
    prune_images(new_path)
    print("Done!")
    