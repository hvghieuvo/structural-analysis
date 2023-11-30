from indeterminatebeam import *
import os
from pathlib import Path
import kaleido

def create_beam(l, E = 200 * 10**9, I = 9.05 * 10**-6, A = 0.23):
    # E is "Young's Modulus" and default = 200 * 10**9
    # A is "Second Moment of Area" and default = 9.05 * 10**-6
    # I is "Cross-Sectional Area" and default = 0.23
    
    beam = Beam(l, E, I, A)
    
    return beam

def add_sp(x, type):
    #Pin = (1,1,0)
    #Roller = (0,1,0)
    #Fixed = (1,1,1)
    
    if type == "pin":
        return beam.add_supports(Support(x, (1,1,0)))
    if type == "roller":
        return beam.add_supports(Support(x, (0,1,0)))
    if type == "fixed":
        return beam.add_supports(Support(x, (1,1,1)))
    
def add_load(x1, magnitude, type, x2 = None):
    
    if type == "pload":
        return beam.add_loads(PointLoadV(magnitude, x1))
    if type == "dlv":
        return beam.add_loads(DistributedLoadV(magnitude, (x1, x2)))
    if type == "ptorque":
        return beam.add_loads(PointTorque(magnitude, x1))
    
def plot_diagram(x=0):
    beam.analyse()
    
    if x == 0:
        #PLot beam schematic
        fig_beam = beam.plot_beam_diagram()
        fig_beam.write_image("./images/fig_beam.png",format='png',engine='kaleido')
    else:
        #PLot beam schematic
        fig_reac = beam.plot_reaction_force()
        fig_reac.write_image("./images/fig_reac.png",format='png',engine='kaleido')

        #PLot normal force
        fig_normal = beam.plot_normal_force()
        fig_normal.write_image("./images/fig_normal.png",format='png',engine='kaleido')

        #PLot shear force
        fig_shear = beam.plot_shear_force()
        fig_shear.write_image("./images/fig_shear.png",format='png',engine='kaleido')

        #PLot bending moment
        fig_moment = beam.plot_bending_moment()
        fig_moment.write_image("./images/fig_moment.png",format='png',engine='kaleido')

        #Plot deflection
        fig_deflection = beam.plot_deflection()
        fig_deflection.write_image("./images/fig_deflection.png",format='png',engine='kaleido')

beam = create_beam(10)
add_sp(0, "fixed")
add_sp(10, "pin")
add_sp(5, "roller")
add_load(2, -10, "pload")
add_load(7, -15, "dlv", 10)
add_load(5, 20, "ptorque")

plot_diagram(1)