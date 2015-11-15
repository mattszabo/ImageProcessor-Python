
'''
Created on 12 Nov 2015

@author: matt
'''

import com.wekilledit.python.image.models.ImageModel as ImageModel

myImage = ImageModel.MyImage('/Users/matt/Documents/workspace/ImageProcessor-Python/src/com/wekilledit/python/image/resources/jimi_bitmap_full.jpg');
myImage.displayImage()
myImage.convertToBlackAndWhite()
myImage.displayImage()