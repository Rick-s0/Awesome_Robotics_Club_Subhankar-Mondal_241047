import numpy as np

#PART A
def footPosition(x, y, z):
    L1 = 5                      #length of coxa
    L2 = 10                     #length of femur
    L3 = 15                     #length of tibia

   
    r = np.hypot(x,y) - L1
    d = np.hypot(r,z)

    min_reach = abs(L2 - L3)
    max_reach = L2 + L3

    if (d < min_reach) or (d > max_reach):
        return None
    
     # calculating the angle with z-axis for coxa
    alpha = np.arctan2(y,x)    
    
    #calculating angle gamma  w.r.t to the position of tibia
    cos_gamma = np.clip((L2**2 + L3**2 - d**2) / (2 * L2 * L3), -1.0, 1.0)
    gamma = np.arccos(cos_gamma)

    #calculating angle beta
    e1 = np.arctan2(z, d)                           
    e2 = np.arccos(np.clip((L2**2 + d**2  - L3**2) / (2 * L2 * d), 1.0, 1.0))
    beta = e1 - e2

    return np.degrees([alpha, beta, gamma])

#PART B


def test_inverse_kinematics():
 
    print("TEST1\n")
    angles1 = footPosition(8, 5, 12)
    if angles1 is not None:
        print("Input target coordinates are x = 8 , y= 5, z = 12 ")
        print("Output joint angles (degrees):\n alpha = {:.2f} \n beta = {:.2f} \n gamma = {:.2f}".format(*angles1),"\n")
        print("Point is reachable \n")
    else:
        print("Not Reachable")

    print("TEST2\n")
    angles2 = footPosition(3, 4, 5)
    if angles2 is not None:
        print("Input target coordinates are x = 3 , y= 4, z = 5 ")
        print("Output joint angles (degrees):\n alpha = {:.2f} \n beta = {:.2f} \n gamma = {:.2f}".format(*angles2),"\n")
        print("Point is reachable \n")
    else:
        print("Not Reachable")

    print("TEST3\n")
    angles3 = footPosition(20, 15, 15)
    if angles3 is not None:
        print("Input target coordinates are x = 20 , y= 15, z = 15 ")
        print("Output joint angles (degrees):\n alpha = {:.2f} \n beta = {:.2f} \n gamma = {:.2f}".format(*angles3),"\n")
        print("Point is reachable \n")
    else:
        print("Not Reachable")

    print("TEST4\n")
    angles1 = footPosition(25, 15, 25)
    if angles1 is not None:
        print("Input target coordinates are x = 8 , y= 5, z = 12 ")
        print("Output joint angles (degrees):\n alpha = {:.2f} \n beta = {:.2f} \n gamma = {:.2f}".format(*angles1),"\n")
    else:
        print("Not Reachable\n")

    print("TEST5\n")
    angles1 = footPosition(8, 10, -22)
    if angles1 is not None:
        print("Input target coordinates are x = 8 , y= 5, z = 12 ")
        print("Output joint angles (degrees):\n alpha = {:.2f} \n beta = {:.2f} \n gamma = {:.2f}".format(*angles1),"\n")
        print("Point is reachable \n")
    else:
        print("Not Reachable")


test_inverse_kinematics()