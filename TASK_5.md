\*\*Explanation of the code\*\*

In the code we take inputs of the required coordinates we want to go.
After that we use inverse kinematics to detect the joint angles. For
finding the angles we transform the coordinate axis of each joint and
using transform matrix we get the rotational transformation and linear
transformation equation. Solving the equations we get the required
angles to rotate to get to that particular position.

In the code the minimum distance the foot can reach is difference
between the length of tibia and femur and maximum distance that the foot
can move is sum of the lengths of femur and tibia as the leg could
stretch due to femur and tibia.

The variable \'r\' represent the distance of femur joint to foot in
horizontal plane and the variable \'d represent straight line distance
from femur joint to foot joint.

Considering the stretch of the femur joint and the foot the required
condition for the reachable distance in the code have been set up.

The function test_inverse_kinematics runs test for five different cases
as given in the problem and outputs as per requirements.
