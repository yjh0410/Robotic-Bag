import numpy as np


class Robot(object):
    def __init__(self, name="cat", rotation=np.diag(3,3), position=np.zeros([3,1])):
        self.name = name
        self.pose = np.concatenate([np.concatenate([rotation, position], axis=1), np.array([[0,0,0,1]])], axis=0)
    
    def getMyPose(self):
        return self.pose

    def getMyRotation(self):
        return self.pose[:3,:3]

    def getMyPosition(self):
        return self.pose[:3,3]

    def rotation(self, theta=0, axis=None):
        if axis == 'x':
            T_rot_x = np.array([[1, 0, 0],
                                [0, np.cos(theta), -np.sin(theta)],
                                [0, np.sin(theta),  np.cos(theta)]])
            return T_rot_x
        
        elif axis == 'y':
            T_rot_y = np.array([[np.cos(theta), 0, np.sin(theta)],
                                [0, 1, 0],
                                [-np.sin(theta),0, np.cos(theta)]])
            return T_rot_y

        elif axis == 'z':
            T_rot_z = np.array([[np.cos(theta), -np.sin(theta), 0],
                                [np.sin(theta),  np.cos(theta), 0],
                                [0, 0, 1]])
            return T_rot_z

    def translation(self, trans_x=0, trans_y=0, trans_z=0):
        return np.array([[trans_x],[trans_y],[trans_z]])

    def rotate(self, theta=0, axis=None, ref_coordinate=None):
        if axis == None and ref_coordinate != None:
            print("Please tell me the rotataion axis!!!")
            return

        if axis != None and ref_coordinate == None:
            print("Please tell me the reference coordinate!!!")
            return
        
        if axis == None and ref_coordinate == None:
            print("Please tell me the rotataion axis and the reference coordinate!!!")
            return

        if axis == 'x':
            rot_x = self.rotation(theta, axis)
            T = np.concatenate([np.concatenate([rot_x,np.zeros([3,1])],axis=1), np.array([[0,0,0,1]])], axis=0)
            if ref_coordinate == 'fixed':
                self.pose = np.dot(T, self.pose)
            if ref_coordinate == 'dynamic':
                self.pose = np.dot(self.pose, T)
            else:
                print("The ref_coordinate is fixed or dynamic!!!")
        
        elif axis == 'y':
            rot_y = self.rotation(theta, axis)
            T = np.concatenate([np.concatenate([rot_y,np.zeros([3,1])],axis=1), np.array([[0,0,0,1]])], axis=0)
            if ref_coordinate == 'fixed':
                self.pose = np.dot(T, self.pose)
            if ref_coordinate == 'dynamic':
                self.pose = np.dot(self.pose, T)
            else:
                print("The ref_coordinate is fixed or dynamic!!!")

        elif axis == 'z':
            rot_z = self.rotation(theta, axis)
            T = np.concatenate([np.concatenate([rot_z,np.zeros([3,1])],axis=1), np.array([[0,0,0,1]])], axis=0)
            if ref_coordinate == 'fixed':
                self.pose = np.dot(T, self.pose)
            if ref_coordinate == 'dynamic':
                self.pose = np.dot(self.pose, T)
            else:
                print("The ref_coordinate is fixed or dynamic!!!")
        
        else:
            print("The axis is x / y / z !!!")
            return

    def translate(self, trans_x=0, trans_y=0, trans_z=0, ref_coordinate=None):
        if ref_coordinate == None:
            print("Please tell me the reference coordinate!!!")
        else:
            trans = self.translation(trans_x=0, trans_y=0, trans_z=0)
            T = np.concatenate([np.concatenate([np.diag(3,3),trans],axis=1), np.array([[0,0,0,1]])], axis=0)
            if ref_coordinate == 'fixed':
                self.pose = np.dot(T, self.pose)
            if ref_coordinate == 'dynamic':
                self.pose = np.dot(self.pose, T)
            else:
                print("The ref_coordinate is fixed or dynamic!!!")

    def transform(self, theta=0, trans_x=0, trans_y=0, trans_z=0, axis=None, ref_coordinate=None):
        rot = self.rotation(theta, axis)
        trans = self.translation(trans_x=0, trans_y=0, trans_z=0)
        T = np.concatenate([np.concatenate([rot,trans],axis=1), np.array([[0,0,0,1]])], axis=0)
        if ref_coordinate == 'fixed':
            self.pose = np.dot(T, self.pose)
        if ref_coordinate == 'dynamic':
            self.pose = np.dot(self.pose, T)
        else:
            print("The ref_coordinate is fixed or dynamic!!!")