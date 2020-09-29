import ctypes
import py2exe

from distutils.core import setup
from os import listdir
from os.path import isfile, join


# gallery of photos directory file path
gallery = r"C:\Users\admin\Pictures\Backgrounds"
# creates an array of all documents in that directory
onlyfiles = [f for f in listdir(r"C:\Users\admin\Pictures\Backgrounds") if isfile(join(gallery, f))]

print(gallery+"\\"+onlyfiles[0])
# sets the background to a particular photo
ctypes.windll.user32.SystemParametersInfoW(20, 0, gallery+"\\"+onlyfiles[0], 0)