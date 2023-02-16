import numpy as np

# define rotation values
roll = np.pi / 2
pitch = np.pi / 2
yaw = np.pi / 2

# rotation matrix about x-axix: roll
R_x = np.array([[1, 0, 0],
                [0, np.cos(roll), -np.sin(roll)],
                [0, np.sin(roll), np.cos(roll)]])

# rotation matrix about y-axis: pitch
R_y = np.array([[np.cos(pitch), 0, np.sin(pitch)],
                [0, 1, 0],
                [-np.sin(pitch), 0, np.cos(pitch)]])

# rotation matrix about z-axis: yaw
R_z = np.array([[np.cos(yaw), -np.sin(yaw), 0],
                [np.sin(yaw), np.cos(yaw), 0],
                [0, 0, 1]])

# final rotation matrix
rot = np.matmul(np.matmul(R_z, R_y), R_x)

print("Rotation:\n", rot)
