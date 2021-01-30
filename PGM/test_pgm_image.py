from reader import *
from pgm_image import *
import pytest


def test_construction():
  a = PGMImage()
  assert a.data == []
  assert a.size == (0, 0)
  assert a.width == 0
  assert a.height == 0
  del a

  p = str(Path(__file__).resolve().parent)
  reader = PGMReader(p + "/images/image2.pgm")
  pgm_image = reader.get_image()
  assert type(pgm_image) == PGMImage
  assert reader.matrix == pgm_image.data # input image is already normalized
  assert reader.height == pgm_image.height
  assert reader.width == pgm_image.width
  del reader
  del pgm_image

  p = str(Path(__file__).resolve().parent)
  reader = PGMReader(p + "/images/fin.pgm")
  pgm_image = reader.get_image()
  assert reader.matrix != pgm_image.data # input image is not normalized
  del reader
  del pgm_image

  data = [[1,2,3,4],[5,6,7,8],[9,0,1,2],[3,4,5,6],[7,8,9,0]]
  pgm_image = PGMImage(data)
  assert pgm_image.data == data
  assert pgm_image.height == len(data)
  assert pgm_image.width == len(data[0])


def test_copy():
  p = str(Path(__file__).resolve().parent)
  reader = PGMReader(p + "/images/image2.pgm")
  pgm_image = reader.get_image()

  pgm_image_2 = pgm_image
  assert id(pgm_image_2) == id(pgm_image)
  
  pgm_image_2 = pgm_image.copy()
  assert id(pgm_image_2) != id(pgm_image)
  assert id(pgm_image_2.data) == id(pgm_image.data)
  assert id(pgm_image_2.size) != id(pgm_image.size) # tuple is not mutable -> always deepcopy
  
  pgm_image_2 = copy.copy(pgm_image)
  assert id(pgm_image_2) != id(pgm_image)
  assert id(pgm_image_2.data) == id(pgm_image.data)
  assert id(pgm_image_2.size) != id(pgm_image.size) # tuple is not mutable -> always deepcopy
  

def test_deepcopy():
  p = str(Path(__file__).resolve().parent)
  reader = PGMReader(p + "/images/image2.pgm")
  pgm_image = reader.get_image()

  pgm_image_2 = pgm_image
  assert id(pgm_image_2) == id(pgm_image)
  
  pgm_image_2 = pgm_image.deepcopy()
  assert id(pgm_image_2) != id(pgm_image)
  assert id(pgm_image_2.data) != id(pgm_image.data)
  assert id(pgm_image_2.size) != id(pgm_image.size)
  
  pgm_image_2 = copy.deepcopy(pgm_image)
  assert id(pgm_image_2) != id(pgm_image)
  assert id(pgm_image_2.data) != id(pgm_image.data)
  assert id(pgm_image_2.size) != id(pgm_image.size)
  

def test_normalize():
  data = [[1,2,3,4],[5,6,7,8],[9,0,1,2],[3,4,5,6],[7,8,9,0]]
  pgm_image = PGMImage(data)
  
  normal_data =  [[28,57,85,113],[142,170,198,227],[255,0,28,57],[85,113,142,170],[198,227,255,0]]
  pgm_image.normalize()
  assert pgm_image.data == normal_data
  del pgm_image

  data = [[1,2,3,4],[5,6,7,8],[9,0,1,2],[3,4,5,6],[7,8,9,0]]
  pgm_image = PGMImage(data)
  pgm_image.normalize(30, 39)
  assert pgm_image.data ==  [[31,32,33,34],[35,36,37,38],[39,30,31,32],[33,34,35,36],[37,38,39,30]]
  del pgm_image

  data = [[1,2,3,4],[5,6,7,8],[9,0,1,2],[3,4,5,6],[7,8,9,0]]
  pgm_image = PGMImage(data)
  pgm_image.normalize(30, 48)
  assert pgm_image.data ==  [[32,34,36,38],[40,42,44,46],[48,30,32,34],[36,38,40,42],[44,46,48,30]]
  del pgm_image

  data = [[1,2,3,4],[5,6,7,8],[9,0,1,2],[3,4,5,6],[7,8,9,0]]
  pgm_image = PGMImage(data)
  pgm_image.normalize(-46, 26)
  assert pgm_image.data ==  [[-38,-30,-22,-14],[-6,2,10,18],[26,-46,-38,-30],[-22,-14,-6,2],[10,18,26,-46]]


  data = [[100,200,300,400],[500,600,700,800],[900,0,100,200],[300,400,500,600],[700,800,900,0]]
  pgm_image = PGMImage(data)
  pgm_image.normalize(-46, 26)
  assert pgm_image.data ==  [[-38,-30,-22,-14],[-6,2,10,18],[26,-46,-38,-30],[-22,-14,-6,2],[10,18,26,-46]]
