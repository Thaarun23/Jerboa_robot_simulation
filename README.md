# Jerboa_robot_simulation
Jerboa Robot simulation using Mujoco

1. INTRODUCTION

The Jerboa is a small bipedal mouse like mammal. These creatures
have elongated limbs and switch between various gaits. Our aim is to develop a foldable
robot that mimics the jerboa's short hopping mechanism. Our primary objective is to design
a robotic system capable of performing short hops like jerboa legs, potentially using foldable
mechanisms like four-bar linkage and over centering mechanisms in both the legs of the
robot.

2.MANUFACTURING

The prototyping and manufacturing process of the robot body has been done using
LibreCAD and laser cutting techniques. We used cardstock for the links and a flexible plastic
materical for the joint hinges.
We also ran simulations of the robot body in Solidworks, and also designed the mounts for
the four servo motors that we used in the construction and movement of the robot within it.
We have made the link between the first servo and second servo to be rigid so we 3D print
the joint from servo 1 to servo 2.
For the connection from servo to 4bar we have made a very small slit in the 3D printed part
where the laminated cardstock can fit into.

![image](https://github.com/user-attachments/assets/94ebbeaa-1038-4bac-84e3-0396be2194fa)

3.BODY DESIGN

The body of the robot is designed in such a way that it has a tail at the back that would help
the robot in stability and balance of the robot while the main body would stay flat where the
servos and the wires are mounted that would actuate the motors in desired direction and
degree.
The optimization of the links lengths, joint stiffness and thickness has been done through
mutilple iteration of Solidworks and Mujoco simulations.
The dimenisons of the body design are as follows:

![image](https://github.com/user-attachments/assets/409313d2-f647-40db-aab3-03d42f20cdb6)

4.VALID CONFIGURATIONS FOR LINK LENGTH AND
OPTIMIZATION


A simplified version of the kinematic model is made in order to sweep the possible joint
lenghts which would result in the highest end effector velocity and would result in the robot
having enough velocity to jump.
In order to see which lengths would give the best results we used a python code to plot the
possible lengths. We have selected two parameters where we would keep the length of link 2
which is the actuaing link in the 4 bar fixed and we would change the length of link l3 and l4
would be equal to l2*m where we were trying to find the value of m which would give us the
best result.
In order to achive the overcentering affect in out 4 bar mechaism we would need the link 4
to be longer than link2 and the m value would give us the optimum value of m.
from the plot we can see the place where we have high velocity in the link but these are not
possible to achive as in this configuration the mechanism would just pivot and not have any
strength and the configurations where the mechanism is not possible the velocity is given as
0 an is depicted by the purple region in the plot.

MUJOCO SIMULATION

The code involves a body and two seperate four bar mechanism mimicking our design of the
legs . the link 1 is attached to the body and leg link 2 is our primary link making contact with
the ground (green) the effect that the link length has in the height and displacemnet of the
robot is studied in this simulation. the optimal link lengths are presented above with l1,l2,l3
being the links needed to control leglink4 and the leg link4 being tested. the xml code below
is a template which can be used to vary any of the link lenghts without affecting the
structure of the leg. 2 motors are attached to both leglink1 and leglink3. all the links are
connected to each other using a hinge joint except for leglin4 and leglink2 which is welded
together.


![yes](https://github.com/user-attachments/assets/82e30c79-90e1-495d-9393-10052adad1c9)
