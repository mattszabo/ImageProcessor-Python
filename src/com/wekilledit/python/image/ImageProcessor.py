
'''
Created on 12 Nov 2015

@author: matt
'''
from PIL import Image

def __init__(self):
    '''
    Constructor
    '''
        
def displayImage(aFilename):
    image = Image.open(aFilename)
    image.show()
        
displayImage('/Users/matt/Documents/workspace/ImageProcessor-Python/src/com/wekilledit/python/image/resources/jimi_bitmap_full.jpg');