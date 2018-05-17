import numpy as np
import math


def Relu(array):
    array[array < 0] = 0
    return array

def ReluArray(array):
    assert type(array) == type(list())
    return [Relu(x)  for x in array]

if __name__=="__main__":
    ...
