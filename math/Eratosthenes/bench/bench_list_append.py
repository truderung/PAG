from os import path
import sys
sys.path.append(path.join(path.dirname(__file__), '..', '..', '..'))

from benchmark import Bench

n = 10000000
ref = [i for i in range(1,n+1)]

#############  append to list #######################################
def test_list_append():
  a = []
  with Bench():
    for i in range(1,n+1):
      a.append(i)
  assert ref == a

def test_list_plus():
  a = []
  with Bench():
    for i in range(1,n+1):
      a += [i]
  assert ref == a

def test_list_for_comprehension():
  a = []
  with Bench():
    a = [i for i in range(1,n+1)]
  assert ref == a

def test_list_multiple_comprehension():
  a = []
  divisor = 100
  with Bench():
    block = n // 100
    for h in range(1,block+1):
      a += [i for i in range((h-1)*divisor+1,h*divisor+1)]
  assert ref == a

def test_list_cast():
  a = []
  with Bench():
    a = list(range(1,n+1))
  assert ref == a

def test_list_multiple_cast():
  a = []
  divisor = 100
  with Bench():
    block = n // 100
    for h in range(1,block+1):
      a += list(range((h-1)*divisor+1,h*divisor+1))
  assert ref == a

def test_list_numpy_arange():
  import numpy
  a = []
  with Bench():
    a = numpy.arange(1,n+1).tolist()
  assert ref == a