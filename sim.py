"""
Simulator setup for robot performance visualiser
"""
import os
import pybullet as p
import pybullet_data
import time
#note: need to keep python script running so it doesnt just close the sim when it finishes the main file
#can this be accomplished with rospy.spin()..?
def main():
    #general setup
    var = '905'
    urdf = '.urdf'
    physicsClient = p.connect(p.GUI) #boots up graphical interface
    p.setAdditionalSearchPath(pybullet_data.getDataPath())

    #object setup
    #print(f'path:{pybullet_data.getDataPath()}\n') # path is in a hidden folder in home(.../.local/...)
    planeID = p.loadURDF("plane.urdf") #not necessary just nicer to look at
    #pandaUid = p.loadURDF(os.path.join(pybullet_data.getDataPath(), "franka_panda/panda.urdf"),useFixedBase=True)
    pandaUid = p.loadURDF(os.path.join(pybullet_data.getDataPath(), "franka_panda/panda.urdf"), basePosition=[0.,0.,0.1])
    objectUid = p.loadURDF(os.path.join(pybullet_data.getDataPath(), "random_urdfs", var, var + urdf), basePosition=[0.7,0.,1.])
    #print(f'object path: {os.path.join(pybullet_data.getDataPath(), "random_urdfs/001/001.urdf")}')

    #camera setup
    #p.resetDebugVisualizerCamera(cameraDistance=2, cameraYaw=0, cameraPitch=-40, cameraTargetPosition=[0.,0.,0.])
    p.resetDebugVisualizerCamera(cameraDistance=0.25, cameraYaw=0, cameraPitch=-40, cameraTargetPosition=[0.7,0.,1.])
    p.resetBaseVelocity(objectUniqueId=pandaUid, linearVelocity = [1.,0.,0.])

    while 1: #keeping the program running forever
        p.configureDebugVisualizer(p.COV_ENABLE_SINGLE_STEP_RENDERING)
        p.stepSimulation() #this must be last in the loop; modify timestep via setTimeStep(dt)
    
    p.disconnect() #nicer shutdown method


if __name__ == "__main__":
    main()