import pygame
import os

#Classs Object - Player
  #Sprite
  #Location 
  #PLayer Health

  #Jump Script

#Class Object - Hazard
  #Sprite
  #Location

  #Movement

  #DoHit Player?

#Class Object - AbstractGameRunner
  #Holds Hazard

  #Make A Hazard

  #Timer 
    #Make a Hazard



#While Loop if Player Health > 0 
  #On AbstractGameRunner. Timer spawn Hazard
  #Player - Jump Movement
  #For each Hazard do "DoHit Player?"

  

pygame.init()
win = pygame.display.set_mode((500,500))
pygame.display.set_caption("Jumpstacles")

x = 50
y = 50
width = 50
height = 50
vel = 5

isJump = False
jumpCpint = 10

run = True 
while run:
  pygame.time.delay(50)

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      run = False

keys = pygame.key.get_pressed()

if keys[pygame.K_LEFT] and x > vel: 
  x -= vel 
if keys[pygame.K_RIGHT] and x < 500 - width - vel:
  x += vel
if not(isJump):  
  if keys[pygame.K_UP] and y > vel:
    y -= vel
  if keys[pygame.K_DOWN] and y < 500 - height - vel:
    y += vel
  if keys[pygame.K_SPACE]:
    isJump = True 
else:
  if jumpCount >= -10:
    neg = 1
    if jumpCount < 0:
      neg = -1
    y == (jumpCount ** 2) * 0.5 * neg
    jumpCount == 1 
  else:
    isJump = False
    jumpCount = 10     

win.fill((0,0,0))
pygame.draw.rect(win, 255, 0, 0), (x, y, width, height))
pygame.display.update() 

pygame.quit() 