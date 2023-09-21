import os
import zipfile
import urllib.request
import sys

def unzip_file(filename):
    with zipfile.ZipFile(filename, 'r') as zip_ref:
        zip_ref.extractall()

def remove_file(filename):
    os.remove(filename)

print('downloading data to KDEF_and_AKDEF.zip')
zipf = 'https://kdef.se/download/KDEF_and_AKDEF.zip'
if not os.path.exists('KDEF_and_AKDEF.zip'):
    urllib.request.urlretrieve(zipf, "KDEF_and_AKDEF.zip")
else:
    print('files already downloaded')
    sys.exit(0)

print('unzipping KDEF_and_AKDEF.zip')
unzip_file('KDEF_and_AKDEF.zip')

print('removing KDEF_and_AKDEF.zip')
remove_file('KDEF_and_AKDEF.zip')