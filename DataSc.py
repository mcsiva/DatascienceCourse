# import libraries
import pandas as pd
import numpy as np

def add_sq(range_val):
  for i in range(0, range_val):
    j = j + j**2
    print("iteration:", i , "sum square", j)
    j+1

add_sq(5)
