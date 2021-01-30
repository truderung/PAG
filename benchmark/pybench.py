import time

class Bench():
  def __init__(self):
    self.start = time.time()
 
  def __enter__(self):
    return self

  def __exit__(self, exc_type, exc_val, exc_tb):
    print('The function took %f seconds to complete' % (time.time() - self.start))

