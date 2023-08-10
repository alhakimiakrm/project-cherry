#imports of outside libraries
import numpy as np
import matplotlib.pyplot as plt
import random 
#----------

# Blueprint for Sphere-like Particle 
class Particle:
    m= 0 #mass of particle (kg)
    g= 0 #gravitational acceleration (m/s^2)
    r= 0 #radius of particle (m)
    
    def weight(s): #weight of particle (kg m/s^2)
        return(s.m*s.g)
    
    def area(s): #Surface area of particle (m^2)
        return(4*(np.pi)*(s.r**2))
    
    def volume(s): #volume of particle (m^3)
        return((4/3)*np.pi*(s.r**3))
    
    def density(s): #density of particle (kg/m^3)
        return((s.m)/((4/3)*np.pi*(s.r**3)))
    
    


# Particle1-Cherry is her name :)
cherry=Particle()
cherry.m=32*10**-32 #kg
cherry.g=9.8 #m/s^2s
cherry.r=23*10**-20 #m
cherry.w=cherry.weight() #kg m/s^2
cherry.A=cherry.area() #m^2
cherry.V=cherry.volume() #m^3
cherry.D=cherry.density() #kg/m^3
print(f"Mass={cherry.m} kg,Weight={cherry.w} kg m/s^2,Area={cherry.A} m^2,Volume={cherry.V} m^3,Density={cherry.D} kg/m^3")