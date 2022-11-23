"""
Misc testing file (remember, ctrl + k ctrl + c for mass comment (ctrl + u for mass uncomment))
"""

import os
import pybullet
import pybullet_data
import time

#testing os.path functionality
var = '001'
urdf = '.urdf'
print(f'{os.path.join(pybullet_data.getDataPath(), "random_urdfs", var, var + urdf)}')
print(f'{os.path.join(pybullet_data.getDataPath(), "random_urdfs/001/001.urdf")}')