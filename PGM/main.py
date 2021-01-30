from pgm_reader import *
from px_map import *
from convolver import *
from sobel_filter import * 


p = str(Path(__file__).resolve().parent)
pgm_image = PGMReader(p + "/images/land.pgm").get_image()
scale = 2
screen = PxMap([pgm_image.width*scale, pgm_image.height*scale])
screen.show(pgm_image, True, False)

# se := structuring element
# se = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]  # Identität (abgesehen von Randbehandlung)
# se = [[0, 0, 0], [0, -1, 0], [0, 0, 0]]  # Inverse (abgesehen von Randbehandlung)
# se = [[1, 0, 1], [0, 1, 0], [1, 0, 1]] 
# se = [[-1, -1, -1], [-1, 1.5, 0], [-1, 0, 1]]
se_x = [[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]] #Sobel Sx
se_y = [[-1, -2, -1], [0, 0, 0], [1, 2, 1]] #Sobel Sy

# res_image = Convolver.run(pgm_image, se)
res_image = SobelFilter.run(pgm_image, se_x, se_y)
res_image.normalize()

screen_2 = PxMap([res_image.width*scale, res_image.height*scale])
screen_2.show(res_image, True, True)
