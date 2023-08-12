#IMPORTS OF OUTSIDE LIBRARIES----------
import numpy as np
import matplotlib.pyplot as plt
import random 
import pygame
import pymunk
#PYGAME COLORS-------------------------
white =     ( 255, 255, 255 )
blue =      ( 0, 0, 255 )
green =     ( 0, 255, 0 )
red =       ( 255, 0, 0 )
black=      ( 0, 0, 0 )

#LET'S DEFINE A PARTICLE----------------------------------------
# a particle is...
# a thing or several things that exist within a location 
# tends to move around
# is affected by time and other factors
# tends to disappear after a certain amount of time
# can also be expanded, changed (in shape and mass) and destroyed

#---------------------------------------------------------------

#OUR WINDOW (SIZE & COORDINATES)--------------------------------
WIDTH, HEIGHT = 800, 800
botleft=0,0             #these coordinates are based of Pymunk's coordinates
botright=WIDTH,HEIGHT    
topleft=0,HEIGHT 
topright=WIDTH,0

#PHYSICS SPACE--------------------------------------------------
space=pymunk.Space() #All the physics will be inside this 'space'
space.gravity=0,-200 #this gives gravity to our space in the negative y direction

#PARTICLE1-CHERRY-----------------------------------------------
cherry=pymunk.Body() #creating Cherry's body, no argument is added which gives us a dynamic body that reactes to forces,collisions etc.
cherry.position=400,400 #Initial position of Cherry
cherry_shape=pymunk.Circle(cherry,12) # second argument is the radius
cherry_shape.mass=1
cherry_shape.density=1
cherry_shape.elasticity=1 # '1' is perfect elasticity
space.add(cherry,cherry_shape) # we must add out body and shape to our physics space (body,shape)

#CONVERSION OF COORDINATES-------------
def convert_coordinates(point):
    return point[0], HEIGHT-point[1]

#WINDOW BARRIER-------------------------------------------------
#Bottom---------
barrier_body_bottom=pymunk.Body(body_type=pymunk.Body.STATIC) #This creates a static body 
barrier_shape_bottom=pymunk.Segment(barrier_body_bottom,(0,0),(800,0),0) #This defines the shape of our body to be a Segment from point (0,0) to (800,0). 3rd argument is the width of the Segment
barrier_shape_bottom.elasticity=1 #This gives our shape elasticity,'1' being perfectly elastic 
space.add(barrier_body_bottom,barrier_shape_bottom)#Then we MUST add our body and its shape to our physics space (body,shape)
#Top------------
barrier_body_top=pymunk.Body(body_type=pymunk.Body.STATIC) 
barrier_shape_top=pymunk.Segment(barrier_body_top,(0,800),(800,800),0)  
barrier_shape_top.elasticity=1 
space.add(barrier_body_top,barrier_shape_top) 
#Left-----------
barrier_body_left=pymunk.Body(body_type=pymunk.Body.STATIC)
barrier_shape_left=pymunk.Segment(barrier_body_left,(0,0),(0,800),0)
barrier_shape_left.elasticity=1
space.add(barrier_body_left,barrier_shape_left)
#Right----------
barrier_body_right=pymunk.Body(body_type=pymunk.Body.STATIC)
barrier_shape_right=pymunk.Segment(barrier_body_left,(800,0),(800,800),0)
barrier_shape_right.elasticity=1
space.add(barrier_body_right,barrier_shape_right)
#----------------------------------------------------------------

#SETUP VISUALIZATION VIA WINDOW----------------------------------
pygame.init ()
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Simulation Project")
BORDER = pygame.Rect(WIDTH/2 - 5, 0, 10, HEIGHT)
#CLOCKS----------------------
clock = pygame.time.Clock()
FPS=60
#-----------------------------

def main():
    run = True

    while run:
        WIN.fill(black)
        x,y=convert_coordinates(cherry.position)
        pygame.draw.circle(WIN,white,(int(x),int(y)),12)
        
       
    
        
        clock.tick(FPS)
        space.step(1/FPS)
        pygame.display.update()
    
        
        
        for event in pygame.event.get():#initializing user input for when the window is closed out (x) 
            if event.type == pygame.QUIT:
                run = False 
            
                
    pygame.quit()
    
    
main()
#we call main which means this window can only be initialized within VScode, not outside. 
#-------------

