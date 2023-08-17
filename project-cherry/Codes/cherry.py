#IMPORTS OF OUTSIDE LIBRARIES----------
import numpy as np
import matplotlib.pyplot as plt
import random 
import pygame
import pymunk
import pymunk.pygame_util
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


# Functions defined

def create_cherry(space, radius, mass): #I created cherry within a function so that we can call this function when we add new elements to the simulation later on as opposed to rewriting hr attributes each time 
    cherry = pymunk.Body()
    cherry.position = (400, 400) 
    shape = pymunk.Circle(cherry, radius)
    shape.mass = mass 
    shape.elasticity = 1
    shape.friction = 0.5 
    shape.color = (255, 0, 0, 75)
    space.add(cherry, shape)
    return shape

def create_cherry2(space, radius, mass):
    cherry2 = pymunk.Body()
    cherry2.position = (600, 600)  
    shape = pymunk.Circle(cherry2, radius)
    shape.mass = mass
    shape.elasticity = 1
    shape.friction = 0.5
    shape.color = (255, 255, 255, 75)  
    space.add(cherry2, shape)
    return shape

def boundary_set(space, width, height): #same output of code, different format for more precise addition and change of code
    rects = [
        [(width/2, height - 10), (width, 20)],
        [(width/2, 10), (width, 20)],
        [(10, height/2), (20, height)],
        [(width - 10, height/2), (20, height)]
    ]
    
    for pos, size in rects: #we create a "body" for the border that is static so we can also add things to the border that may affect the particles state (such as the elasticity and friction of it)
        body = pymunk.Body(body_type=pymunk.Body.STATIC)
        body.position = pos
        shape = pymunk.Poly.create_box(body, size)
        shape.elasticity = 0.5  #less elasticity on border will result in a drop off in "bounciness"
        shape.friction = .5
        space.add(body, shape)
        
def draw(space, window, draw_options): #defining our draw options within our space so we can utilize pygame within pymunk and vice versa
    window.fill("black")
    space.debug_draw(draw_options)
    pygame.display.update()  



pygame.init()

WIDTH, HEIGHT = 800, 800
window = pygame.display.set_mode((WIDTH, HEIGHT))


def run (window, width, height): #just redid our main loop 
    run = True
    clock = pygame.time.Clock()
    fps = 60
    dt = 1 / fps

    space = pymunk.Space()
    space.gravity = (0, 0) #9.81 m/s gravitational constant
    
    cherry = create_cherry(space, 50, 10)
    cherry2 = create_cherry2(space, 20, 5)  

    boundary_set(space, width, height)
    
    draw_options = pymunk.pygame_util.DrawOptions(window)
    
    
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
            
            
        cherry2.position = (random.uniform(0, WIDTH), random.uniform(0, HEIGHT))
        
        collisions = space.shape_query(cherry2)  
        for collision in collisions:
            shape, point = collision
            if shape == cherry.shape:
                
                pass
   
            
        draw(space, window, draw_options)
        space.step(dt)
        clock.tick(fps)
        
    pygame.quit()
    
if __name__ == "__main__":
    run(window, WIDTH, HEIGHT)