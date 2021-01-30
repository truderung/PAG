from pgm_image import *

class Convolver():
  @staticmethod
  def run(pgm_image, operator):
    res_image = pgm_image.deepcopy()
    
    #Randbehandlung: wird 0 gesetzt
    res_image[0] = [0] * pgm_image.width
    res_image[-1] = [0] * pgm_image.width
    
    for i in range(1, pgm_image.height-2):
      for j in range(1, pgm_image.width-2):
        #Randbehandlung: wird 0 gesetzt
        res_image[i][0] = 0
        res_image[i][-1] = 0
        
        res_image[i][j] = pgm_image[i-1][j-1]*operator[0][0] + \
                          pgm_image[i][j-1]*operator[1][0] + \
                          pgm_image[i+1][j-1]*operator[2][0] + \
                          pgm_image[i-1][j]*operator[0][1] + \
                          pgm_image[i][j]*operator[1][1] + \
                          pgm_image[i+1][j]*operator[2][1] + \
                          pgm_image[i-1][j+1]*operator[0][2] + \
                          pgm_image[i][j+1]*operator[1][2] + \
                          pgm_image[i+1][j+1]*operator[2][2]
    
    return res_image