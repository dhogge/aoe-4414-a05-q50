# ray_ellipsoid_intersection.py
# Text explaining script usage
# Parameters:

# ...
# output:
# ecef x y z coords
#
# Written by Dylan Hogge
# Other contributors: None
#
# Optional license statement, e.g., See the LICENSE file for the license.
# import Python modules
import sys  # argv
import math  # mathematical functions

#constants
R_E_KM = 6378.137
E_E = 0.081819221456

# initialize script arguments
d_l_x = float('nan')
d_l_y = float('nan')
d_l_z = float('nan')
c_l_x = float('nan')
c_l_y = float('nan')
c_l_z = float('nan')

# parse script arguments
if len(sys.argv)==7:
  d_l_x = float(sys.argv[1])
  d_l_y = float(sys.argv[2])
  d_l_z = float(sys.argv[3])
  c_l_x = float(sys.argv[4])
  c_l_y = float(sys.argv[5])
  c_l_z = float(sys.argv[6])
else:
  print(\
   'Usage: '\
   'python3 ray_ellipsoid_intersection.py d_l_x d_l_y d_l_z c_l_x c_l_y c_l_z'\
  )
  exit()
  
a = d_l_x**2+d_l_y**2+(d_l_z**2)/(1-E_E**2)
b = 2*(d_l_x*c_l_x+d_l_y*c_l_y+(d_l_z*c_l_z/(1-E_E**2)))
c = c_l_x**2+c_l_y**2+(c_l_z**2)/(1-E_E**2)-R_E**2

disc = b**2-(4*a*c)
if disc > 0:
    d = (-b-math.sqrt(disc))/(2*a)
    if d<0:
         d= (-b+math.sqrt(disc))/(2*a)
         l_x = d*d_l_x+c_l_x
         l_y = d*d_l_y+c_l_y
         l_z = d*d_l_z+c_l_z
    if d>=0:
        l_x = d*d_l_x+c_l_x
        l_y = d*d_l_y+c_l_y
        l_z = d*d_l_z+c_l_z

l_d = [l_x, l_y, l_z]

#Print
print(l_d[0]) # x-component of intersection point
print(l_d[1]) # y-component of intersection point
print(l_d[2]) # z-component of intersection point
