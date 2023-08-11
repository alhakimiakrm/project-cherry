#imports of outside libraries
import numpy as np
import matplotlib.pyplot as plt
import random 
#----------

#setup visualization via window
import pygame 
pygame.init ()

WIDTH, HEIGHT = 800, 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Simulation Project")

#setting loop to keep window open
def main():
    run = True 
    clock = pygame.time.Clock()
    
    while run:
        clock.tick(60)
        
        for event in pygame.event.get():#initializing user input for when the window is closed out (x) 
            if event.type == pygame.QUIT:
                run = False 
            
                
    pygame.quit()
    
    
main()
#we call main which means this window can only be initialized within VScode, not outside. 
#-------------




#let's define a particle
# a particle is...
# a thing or several things that exist within a location 
# tends to move around
# is affected by time and other factors
# tends to disappear after a certain amount of time
# can also be expanded, changed (in shape and mass) and destroyed 



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