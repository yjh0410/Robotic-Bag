import numpy as np

def rotation(theta=0, axis=None):
	"""input: theta--rotation angle"""
	"""input: axis -- ['x','y','z'],rotation axis"""
	"""output: 3x3 rotation matrix"""
	assert axis != None
	
	if axis == 'x':
		rot = np.array([[1,0,0,0],
						[0,np.cos(theta),-np.sin(theta),0],
						[0,np.sin(theta), np.cos(theta),0],
						[0,0,0,1]])
		
	elif axis == 'y':
		rot = np.array([[np.cos(theta),0,np.sin(theta),0],
						[0,1,0,0],
						[-np.sin(theta),0,np.cos(theta),0],
						[0,0,0,1]])
										
	elif axis == 'z':
		rot = np.array([[np.cos(theta),-np.sin(theta),0,0],
						[np.sin(theta), np.cos(theta),0,0],
						[0,0,1,0],
						[0,0,0,1]])
										
	else:
		print("The axis is x / y / z !!!")
		return
	return rot
	
def translation(trans_x=0, trans_y=0, trans_z=0):
	"""input: tran_x/y/z -- translation"""
	"""output: translation vector"""
	return np.array([[1,0,0,trans_x],
					 [0,1,0,trans_y],
					 [0,0,1,trans_z],
					 [0,0,0,1]])
	
def gridTransformation(theta=0, axis=None, trans_x=0, trans_y=0, trans_z=0):
	"""input: rotation angle and translation"""
	"""output: grid transformation matrix"""
	assert axis != None
	T = rotation(theta, axis)
	T[0,3] = trans_x
	T[1,3] = trans_y
	T[2,3] = trans_z
	return T
	
if __name__ == '__main__':
	print(translation(30, 0, 0))
	print(gridTransformation(30,'x',30,0,0))

