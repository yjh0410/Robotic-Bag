import numpy as np


class Robot(object):
    
def rotation(theta, axis=None):
    if axis == None:
        print("Please input rotataion axis!!!")
        return

    if axis == 'x':
        R_x = np.array([[1,             0,              0],
                        [0, np.cos(theta), -np.sin(theta)],
                        [0, np.sin(theta),  np.cos(theta)]])
        return R_x