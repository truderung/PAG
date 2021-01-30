from pathlib import Path
from pgm_image import *
import copy
import re

  
class PGMReader():
  def __init__(self, filepath = ""):
    self.filepath = ""
    self.type = None
    self.width = 0
    self.height = 0
    self.maxVal = 0
    self.matrix = []

    if filepath is not "":
      self.__load_from_file(filepath)

  def __load_from_file(self, filepath):
    file = Path(filepath)
    if not file.exists():
      raise FileNotFoundError
    if not self.__is_pgm_file(file):
      raise Exception("Only pgm files are accepted")
    self.__parse_pgm(file)
    self.filepath = str(file)

  def __is_pgm_file(self, file):
    if file.suffix == '.pgm':
      return True
    return False

  def __parse_pgm(self, file):
    with file.open() as f:
      text = f.read()
    text = re.sub(r"#.*[\r|\n]", "", text)
    content_list = re.split(" |\t|\r|\n", text)
    content_list = list(filter(None, content_list))
    self.type = content_list.pop(0)
    self.width = int(content_list.pop(0))
    self.height = int(content_list.pop(0))
    self.maxVal = int(content_list.pop(0))
    if self.maxVal <= 0 or self.maxVal >= 65536:
      raise Exception("maximum gray value is not valid")
    
    self.matrix = []
    for _ in range(self.height):
      line = [int(a) for a in content_list[:self.width]]
      content_list = content_list[self.width:]
      self.matrix.append(line)

  def read_in(self, filepath):
    if filepath is not "":
      self.__load_from_file(filepath)

  def get_image(self):
    image = PGMImage(copy.deepcopy(self.matrix), tuple((self.width, self.height)))
    image.normalize()
    return image
