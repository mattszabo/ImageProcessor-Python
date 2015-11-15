
'''
Created on 15 Nov 2015

@author: matt
'''
from PIL import Image

class MyImage:
    def __init__(self, aImageFullPath):
        self.image = Image.open(aImageFullPath)
        
    def displayImage(self):
        self.image.show()
    
    def convertToBlackAndWhite(self):
        self.image = self.image.convert(mode="1", matrix=None, dither=None, palette=0, colors=256)
