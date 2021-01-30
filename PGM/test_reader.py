from reader import *
import pytest


def test_construction():
  a = PGMReader()
  assert a.filepath == ""
  del a

  p = str(Path(__file__).resolve().parent)
  a = PGMReader(p + "/images/fin.pgm")
  assert a.filepath == str(Path(p + "/images/fin.pgm"))
  del a

  with pytest.raises(FileNotFoundError):
    PGMReader("out/images/fin.pgm")

  with pytest.raises(Exception):
    PGMReader(p + "/reader.py")

def test_type():
  p = str(Path(__file__).resolve().parent)
  reader = PGMReader(p + "/images/fin.pgm")
  assert reader.type == "P2"

def test_size():
  p = str(Path(__file__).resolve().parent)
  reader = PGMReader(p + "/images/fin.pgm")
  assert reader.width == 4
  assert reader.height == 5
   
def test_max_val():
  p = str(Path(__file__).resolve().parent)
  reader = PGMReader(p + "/images/fin.pgm")
  assert reader.maxVal == 9

def test_matrix():
  p = str(Path(__file__).resolve().parent)
  reader = PGMReader(p + "/images/fin.pgm")
  assert reader.matrix == [[1,2,3,4],[5,6,7,8],[9,0,1,2],[3,4,5,6],[7,8,9,0]]

def test_readin():
  reader = PGMReader()
  p = str(Path(__file__).resolve().parent)
  reader.read_in(p + "/images/fin.pgm")
  assert reader.filepath == str(Path(p + "/images/fin.pgm"))

def test_get_image():
  reader = PGMReader()
  p = str(Path(__file__).resolve().parent)
  reader.read_in(p + "/images/fin.pgm")
  res = [[28,57,85,113],[142,170,198,227],[255,0,28,57],[85,113,142,170],[198,227,255,0]]
  assert reader.get_image().data == res

  
