from convolver import *
from pgm_image import *
from math import sqrt

class SobelFilter():
  @staticmethod
  def run(pgm_image, operator_x, operator_y):
    g_x = Convolver.run(pgm_image, operator_x)
    g_y = Convolver.run(pgm_image, operator_y)
    
    for i in range(0, pgm_image.height-1):
      for j in range(0, pgm_image.width-1):
        g_x[i][j] = abs(g_x[i][j]) + abs(g_y[i][j])
    
    return g_x