#IMPORTS OF OUTSIDE LIBRARIES----------
import numpy as np
import matplotlib.pyplot as plt
import random 
import pygame
import pymunk
import pymunk.pygame_util
import math
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

pygame.init()

WIDTH, HEIGHT = 800, 800
window = pygame.display.set_mode((WIDTH, HEIGHT))

def calc_distance(p1, p2):
    return math.sqrt((p1[1] - p1[1])**2 + (p2[0] - p1[0])**2)

def calc_angle(p1, p2):
    return math.atan2(p2[1] - p1[1], p2[0] - p1[0])

def draw(space, window, draw_options, line): #defining our draw options within our space so we can utilize pygame within pymunk and vice versa
    window.fill("black")
    
    if line:
        pygame.draw.line (window, "white", line[0], line[1], 2)
        
    space.debug_draw(draw_options)
    
    pygame.display.update()
    
    
    
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
        
        
    
    
def create_cherry(space, radius, mass, pos): #I created cherry within a function so that we can call this function when we add new elements to the simulation later on as opposed to rewriting her attributes each time 
    cherry = pymunk.Body(body_type=pymunk.Body.STATIC)
    cherry.position = pos 
    shape = pymunk.Circle(cherry, radius)
    shape.mass = mass 
    shape.elasticity = 1
    shape.friction = .5 
    shape.color = (255, 0, 0, 75)
    space.add(cherry, shape)
    return shape 
    

def run (window, width, height): #just redid our main loop 
    run = True
    clock = pygame.time.Clock()
    fps = 60
    dt = 1 / fps

    space = pymunk.Space()
    space.gravity = (0, 981) #9.81 m/s gravitational constant
    
    
    boundary_set(space, width, height)
    
    draw_options = pymunk.pygame_util.DrawOptions(window)
    
    pressed_pos = None 
    cherry = None 
    
    
    while run:
        line = None
        if cherry and pressed_pos:
            line = [pressed_pos, pygame.mouse.get_pos()]
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
            
            if event.type == pygame.MOUSEBUTTONDOWN: 
                if not cherry:
                    pressed_pos = pygame.mouse.get_pos()
                    cherry = create_cherry(space, 30, 10, pressed_pos)
                elif pressed_pos:
                    cherry.body.body_type = pymunk.Body.DYNAMIC
                    angle =  calc_angle(*line)
                    force = calc_distance(*line) * 75 # This is where we can change the force in which the ball is being launched 
                    fx = math.cos(angle) * force
                    fy = math.sin(angle) * force
                    cherry.body.apply_impulse_at_local_point((fx, fy) , (0, 0)) #when mouse is clicked, force is being applied to x (10000) however, no force is being applied to y (0) 
                    pressed_pos = None
                else:
                    space.remove(cherry, cherry.body)
                    cherry = None 
            
            
        draw(space, window, draw_options, line)
        space.step(dt)
        clock.tick(fps)
        
    pygame.quit()
    
if __name__ == "__main__":
    run(window, WIDTH, HEIGHT)
            



#I'm assuming you meant to leave this as just a reference so I commented them out but I don't know
#botleft=0,0            #these coordinates are based of Pymunk's coordinates 
#botright=WIDTH,HEIGHT    
#topleft=0,HEIGHT 
#topright=WIDTH,0

