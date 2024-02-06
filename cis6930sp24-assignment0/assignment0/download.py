import urllib.request
import os

def fetchincidents(url):
    file_path, _ = urllib.request.urlretrieve(url, filename=os.path.basename(url))
    return file_path
