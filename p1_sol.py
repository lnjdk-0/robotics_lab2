import numpy as np
import rbm

# define rotation values
roll = np.pi / 2
pitch = np.pi / 2
yaw = np.pi / 2

# Output format
np.set_printoptions(precision = 3, suppress = True)

# rotation matrix about x-axix: roll
R_x = rbm.rot_x(roll)
# rotation matrix about y-axis: pitch
R_y = rbm.rot_y(pitch)
# rotation matrix about z-axis: yaw
R_z = rbm.rot_z(yaw)
# final rotation matrix
rot = np.matmul(R_z, R_y, R_x)

print("Roll rotation matrix:\n", R_x)
print("Pitch rotation matrix:\n", R_y)
print("Yaw rotation matrix:\n", R_z)
print("Final rotation matrix:\n", rot)

