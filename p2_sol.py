import numpy as np

def translate(tx, ty):
    """
    Returns a homogeneous translation matrix for a 2D translation along x and y axes
    
    Parameters:
    - tx: Translation along x axis
    - ty: Translation along y axis
    
    Returns:
    - A 3x3 homogeneous translation matrix
    """
    return np.array([[1, 0, tx],
                     [0, 1, ty],
                     [0, 0, 1]])

def rotate(theta):
    """
    Returns a homogeneous rotation matrix for a 2D rotation about the origin
    
    Parameters:
    - theta: Angle of rotation in radians
    
    Returns:
    - A 3x3 homogeneous rotation matrix
    """
    cos, sin = np.cos(theta), np.sin(theta)
    return np.array([[cos, -sin, 0],
                     [sin, cos, 0],
                     [0, 0, 1]])

def transform(tx, ty, theta):
    """
    Returns a homogeneous transformation matrix for a 2D translation followed by a 2D rotation
    
    Parameters:
    - tx: Translation along x axis
    - ty: Translation along y axis
    - theta: Angle of rotation in radians
    
    Returns:
    - A 3x3 homogeneous transformation matrix
    """
    return np.matmul(translate(tx, ty), rotate(theta))


