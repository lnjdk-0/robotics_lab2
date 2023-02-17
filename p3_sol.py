import numpy as np
import p2_sol as ht

# Output format
np.set_printoptions(precision = 3, suppress = True)

# Transformation 1: A translation of 2.5 units along the current x-axis, 
# followed by a translation of 0.5 units along the current z-axis,
# followed by a translation of -1.5 units along the current y-axis
H_1 = np.matmul(ht.translate_x(2.5), np.matmul(ht.translate_z(0.5), ht.translate_y(-1.5)))

# Transformation 2: A translation of 0.5 units along the current z-axis, 
# followed by a translation of 2.5 units along the current x-axis, 
# followed by a translation of -1.5 units along the current y-axis
H_2 = np.matmul(ht.translate_z(0.5), np.matmul(ht.translate_x(2.5), ht.translate_y(-1.5)))

# Transformation 3: Transformation 1 but in the fixed frame
H_3 = np.linalg.inv(H_1) # Compute the (multiplicative) inverse of a matrix

# Transformation 4: Transformation 2 but in the fixed frame
H_4 = np.linalg.inv(H_2) # Compute the (multiplicative) inverse of a matrix

# Transformation 5: A rotation by angle pi/2 about the current x-axis, 
# followed by a translation of 3 units along the current x-axis,
# followed by a translation of -3 units along the current z-axis,
# followed by a rotation by angle -pi/2 about the current z-axis
H_5 = np.matmul(ht.rotate_x(np.pi/2), np.matmul(ht.translate_x(3), np.matmul(ht.translate_z(-3), ht.rotate_z(-np.pi/2))))

print("H_1:")
print(H_1)
print("H_2:")
print(H_2)
print("H_3:")
print(H_3)
print("H_4:")
print(H_4)
print("H_5:")
print(H_5)
