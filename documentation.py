"""
Pybullet documentation can be tedious to read through (and not very helpful at times) so this script documents some important functions and their syntax
"""
import os
import pybullet as p
import pybullet_data
import time

#notes
"""
vec3 refers to a 1x3 list which pybullet interprets (not sure how exactly)

"""

#moving robot
pandaUid = p.loadURDF(os.path.join(pybullet_data.getDataPath(), "franka_panda/panda.urdf"), basePosition=[0.,0.,0.1])
p.resetBaseVelocity(objectUniqueId=pandaUid, linearVelocity = [1.,0.,0.])

#changing timestep
dt = 1./240. #240hz simulation (this is default); note that changing timestep may make physics unrealistic (some calcualtions 
#do not scale linearly with the timestep change)
p.stepSimulation() #this must be last in the loop; modify timestep via setTimeStep(dt)

#camera positioning
p.resetDebugVisualizerCamera(cameraDistance=0.25, cameraYaw=0, cameraPitch=-40, cameraTargetPosition=[0.7,0.,1.])

