import skimage
import skimage.io
import skimage.color
import skimage.transform

fname = "frame10"
im = skimage.io.imread(fname + ".jpg")
im = skimage.color.rgb2gray(im)
im = skimage.transform.resize(im, (384, 512))
skimage.io.imsave(fname + ".png", im)
