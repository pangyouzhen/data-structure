import numpy as np
import pysnooper


@pysnooper.snoop()
def one(number):
    mat = []
    while number:
        mat.append(np.random.normal(0, 1))
        number -= 1
    return mat


one(3)
