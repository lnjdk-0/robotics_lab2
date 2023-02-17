import numpy as np

def translate_x(tx):
    """
    Returns a homogeneous translation matrix for a 3D translation along x axes
   
    Parameters:
    - tx: Translation along x axis
   
    Returns:
    - A 4x4 homogeneous translation matrix
    """
    return np.array([[1, 0, 0, tx],
                     [0, 1, 0, 0],
                     [0, 0, 1, 0],
                     [0, 0, 0, 1]])
                     
def translate_y(ty):
    """
    Returns a homogeneous translation matrix for a 3D translation along y axes
   
    Parameters:
    - ty: Translation along y axis
   
    Returns:
    - A 4x4 homogeneous translation matrix
    """
    return np.array([[1, 0, 0, 0],
                     [0, 1, 0, ty],
                     [0, 0, 1, 0],
                     [0, 0, 0, 1]])

def translate_z(tz):
    """
    Returns a homogeneous translation matrix for a 3D translation along z axes
   
    Parameters:
    - tz: Translation along z axis
   
    Returns:
    - A 4x4 homogeneous translation matrix
    """
    return np.array([[1, 0, 0, 0],
                     [0, 1, 0, 0],
                     [0, 0, 1, tz],
                     [0, 0, 0, 1]])

def rotate_x(theta):
    """
    Returns a homogeneous rotation matrix for a 3D rotation about the x-axis
   
    Parameters:
    - theta: Angle of rotation in radians
   
    Returns:
    - A 4x4 homogeneous rotation matrix
    """
    cos, sin = np.cos(theta), np.sin(theta)
    return np.array([[1, 0, 0, 0],
                     [0, cos, -sin, 0],
                     [0, sin, cos, 0],
                     [0, 0, 0, 1]])

def rotate_y(theta):
    """
    Returns a homogeneous rotation matrix for a 3D rotation about the y-axis
   
    Parameters:
    - theta: Angle of rotation in radians
   
    Returns:
    - A 4x4 homogeneous rotation matrix
    """
    cos, sin = np.cos(theta), np.sin(theta)
    return np.array([[cos, 0, sin, 0],
                     [0, 1, 0, 0],
                     [-sin, 0, cos, 0],
                     [0, 0, 0, 1]])

def rotate_z(theta):
    """
    Returns a homogeneous rotation matrix for a 3D rotation about the z-axis
   
    Parameters:
    - theta: Angle of rotation in radians
   
    Returns:
    - A 4x4 homogeneous rotation matrix
    """
    cos, sin = np.cos(theta), np.sin(theta)
    return np.array([[cos, -sin, 0, 0],
                     [sin, cos, 0, 0],
                     [0, 0, 1, 0],
                     [0, 0, 0, 1]])
