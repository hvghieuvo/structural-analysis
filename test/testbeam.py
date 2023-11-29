from indeterminatebeam import *
import os
from pathlib import Path
import kaleido

#========== Step 1: Create a beam 

# Create 7 m beam with E, I, A as defaults
beam = Beam(7)                          
# Create 9 m beam with E, I, and A assigned by user
beam_2 = Beam(9, E=2000, I=10**6, A=3000)     

#========== End step 1 

#========== Step 2: Define supports 

# Defines a pin support at location x = 5 m  
a = Support(5, (1,1,0))      
# Defines a roller support at location x = 0 m
b = Support(0, (0,1,0))      
# Defines a fixed support at location x = 7 m
c = Support(7, (1,1,1))      
# Assign the support objects to a beam object created earlier
beam.add_supports(a,b,c)    

#========== End step 2 

#========== Step 3: Define loads 

# Create a 1000 N point load at x = 2 m
load_1 = PointLoadV(1000, 2)
# Create a 2000 N/m UDL from x = 1 m to x = 4 m
load_2 = DistributedLoadV(2000, (1, 4))
# Defines a 2 kN.m point torque at x = 3.5 m
load_3 = PointTorque(2*10**3, 3.5)
# Assign the load objects to the beam object
beam.add_loads(load_1,load_2,load_3)

#========== End step 3

#========== Step 4: Solve and plot result

beam.analyse()  

#PLot internal force diagram
fig = beam.plot_beam_diagram()
#PLot normal force
fig = beam.plot_normal_force()

#Show the input and free body diagram
fig_1 = beam.plot_beam_external()

#Show the axial, shear, bending moment, deflection
fig_2 = beam.plot_beam_internal()

#Save result as png file
fig_1.write_image("./images/fig1.png",format='png',engine='kaleido')
fig_2.write_image("./images/fig2.png",format='png',engine='kaleido')

# fig_2.write_image("./example_internal.png")

#========== End step 4 

# query for the data at a specfic point (note units are not provided)
print("bending moments at 3 m: " + str(beam.get_bending_moment(3)))
print("shear forces at 1,2,3,4,5m points: " + str(beam.get_shear_force(1,2,3,4,5)))
print("normal force absolute max: " + str(beam.get_normal_force(return_absmax=True)))
print("deflection max: " + str(beam.get_deflection(return_max = True)))  

#Update units
# beam.update_units(key='length', unit='mm')
# beam.update_units('force', 'kN')
# beam.update_units('distributed', 'kN/m')
# beam.update_units('moment', 'kN.m')
# beam.update_units('E', 'kPa')
# beam.update_units('I', 'mm4')
# beam.update_units('deflection', 'mm')