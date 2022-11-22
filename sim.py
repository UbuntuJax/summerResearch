"""
Simulator setup for robot performance visualiser
"""
import pybullet
import pybullet_data
import time
#note: need to keep python script running so it doesnt just close the sim when it finishes the main file
def main():
    physicsClient = pybullet.connect(pybullet.GUI)
    pybullet.setAdditionalSearchPath(pybullet_data.getDataPath())
    planeID = pybullet.loadURDF("plane.urdf")

    while(1):
        pass
        #keeping the program running forever
    


if __name__ == "__main__":
    main()