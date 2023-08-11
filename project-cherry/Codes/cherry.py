#imports of outside libraries
import numpy as np
import matplotlib.pyplot as plt
import random 
import pygame
#----------
#pygame colors
white =     (255, 255, 255)
blue =      (  0,   0, 255)
green =     (  0, 255,   0)
red =       (255,   0,   0)
black=      (0,0,0)
#-----------



#let's define a particle
# a particle is...
# a thing or several things that exist within a location 
# tends to move around
# is affected by time and other factors
# tends to disappear after a certain amount of time
# can also be expanded, changed (in shape and mass) and destroyed 
#-----------

# Blueprint for Sphere-like Particle 
class Particle:
    m= 0 #mass of particle (kg)
    g= 0 #gravitational acceleration (m/s^2)
    r= 0 #radius of particle (m)
    initx=0 #position in x-direction
    inity=0 #position in y-direction
    D=0
    t=0
    v=0
    f=0
    
    def weight(s): #weight of particle (kg m/s^2)
        return(s.m*s.g)

    def area(s): #Surface area of particle (m^2)
        return(4*(np.pi)*(s.r**2))
    
    def volume(s): #volume of particle (m^3)
        return((4/3)*np.pi*(s.r**3))
    
    def density(s): #density of particle (kg/m^3)
        return((s.m)/((4/3)*np.pi*(s.r**3)))
    
    def initposition(s):
        return(s.initx,s.inity)
    
    def finapositionx(s):
        return(s.initx+s.t*s.v) #return (x) final
          
    def finapositiony(s):
        return(s.inity + s.t*s.v)
    
    def xfinal(s):
        return((s.t**2)*s.f/s.m)
    


# Particle1-Cherry is her name :)
cherry=Particle()
cherry.m=1 #kg
cherry.g=9.8 #m/s^2s
cherry.initx=400
cherry.inity=400
cherry.t=2 #time 
cherry.D=3
cherry.v=1 
cherry.r=15 #m
#FORCES APPLIED ON CHERRY
cherry.f=3

#--------------------------
cherry.w=cherry.weight() #kg m/s^2
cherry.A=cherry.area() #m^2
cherry.V=cherry.volume() #m^3
cherry.D=cherry.density() #kg/m^3
cherry.iP=cherry.initposition() #initial position(x,y)
cherry.fPx=cherry.finapositionx() #final position(x,y)
cherry.fPy=cherry.finapositiony()
cherry.xf=cherry.xfinal()
#print(f"Mass={cherry.m} kg,Weight={cherry.w} kg m/s^2,Area={cherry.A} m^2,Volume={cherry.V} m^3,Density={cherry.D} kg/m^3")

#setup visualization via window
pygame.init ()
WIDTH, HEIGHT = 800, 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Simulation Project")
clock = pygame.time.Clock()
#setting loop to keep window open
def main():
    run = True 
    clock = pygame.time.Clock()
    
    
    while run:
        WIN.fill(black)
        pygame.draw.circle(WIN,white,(cherry.initx,cherry.inity),13,0)
        cherry.initx+=1

        
        clock.tick(60)
        pygame.display.update()
    
        
        
        for event in pygame.event.get():#initializing user input for when the window is closed out (x) 
            if event.type == pygame.QUIT:
                run = False 
            
                
    pygame.quit()
    
    
main()
#we call main which means this window can only be initialized within VScode, not outside. 
#-------------
