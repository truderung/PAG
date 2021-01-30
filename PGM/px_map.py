# install graphics using 'pip install http://bit.ly/csc161graphics'
# follow the link for some help: https://www.cs.swarthmore.edu/~richardw/classes/cs21/s13/using-graphics.html

import graphics as g
from pgm_image import *
from pathlib import Path

class PxMap():
  # screen_size = self.width, self.height
  def __init__(self, screen_size = [500, 500]):
    self.size = self.width, self.height = screen_size
    self.screen = g.GraphWin('PGM Viewer', self.width, self.height, autoflush=False) # give title and dimensions

  def show(self, image = [], resize = True, pause=True):
    if image != [] and type(image) == PGMImage:
      if resize:
        self.scale = [self.width // image.width, self.height // image.height]
      else:
        self.scale = [1.0, 1.0]

      self.data = image.data
      self.__render(resize)

      if pause:
        message = g.Text(g.Point(self.screen.getWidth()/2, 20), 'Click anywhere to quit.')
        message.setTextColor("white")
        message.draw(self.screen)
        self.screen.getMouse()
      

  def __color_grey(self, value):
    return g.color_rgb(value, value, value)

  def __render(self, resize):
    for y in range(len(self.data)):
      for x in  range(len(self.data[0])):
        color = self.__color_grey(self.data[y][x])
        if not resize:
          elem = g.Point(x*self.scale[0], y*self.scale[1])
        else:
          elem = g.Rectangle(g.Point(x*self.scale[0], y*self.scale[1]), g.Point((x+1)*self.scale[0], (y+1)*self.scale[1]))
          elem.setOutline(color)        

        elem.setFill(color)
        elem.draw(self.screen)
    self.screen.update()

  def __exit__(self, exc_type, exc_value, traceback):
    self.screen.close()

  def clear(self):
    for item in self.screen.items[:]:
        item.undraw()
    self.screen.update()
