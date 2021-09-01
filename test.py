# import mantid algorithms, numpy and matplotlib
from mantid.simpleapi import *
import matplotlib.pyplot as plt
import numpy as np

data_x = np.array([[1, 2, 3, 4, 5],[1, 2, 3, 4, 5],[1, 2, 3, 4, 5],[1, 2, 3, 4, 5]])
data_y= np.array([[0, 1, 10, 100],[-1, 0, 1, 10],[-10, -1, 0, 1],[-100, -10, -1, 0]])
# data_y= -np.ones((4,4))
ws = CreateWorkspace(DataX=data_x, DataY=data_y, NSpec=4)
ws_pos = CreateWorkspace(DataX=data_x, DataY=data_y, NSpec=4)
mdws = CreateMDWorkspace(Dimensions=3, Extents='-10,10,-10,10,-10,10', Names='A,B,C', Units='U,U,U')
