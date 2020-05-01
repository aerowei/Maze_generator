import pygame   
import random

# Colors

WHITE = (255, 255, 255)
GREEN = (0, 255, 0,)
BLUE = (0, 0, 255)
YELLOW = (255 ,255,0)
BLACK = (0, 0, 0)

# Pygame initialization

pygame.init()
screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("Maze generator")
clock = pygame.time.Clock()
screen.fill((WHITE))
pygame.display.update()

x = 20 # Start point on X-Axis
y = 20 # Start point on Y-Axis
w = 20 # Width of a cell
visited = [] # List of all cells visited
stack = []   # Stack used for the generation algorithm
grid = []    # List containing x,y coordinated of all cells

# Build the grid

def build_grid(x,y,w):
    for j in range (x):
        x = 20
        y += 20

        for i in range (x):
            pygame.draw.line(screen, BLACK, (x,y),(x+w,y),1) # Horizontal UP Line
            pygame.draw.line(screen, BLACK, (x,y),(x,y+w),1) # Vertical RIGHT Line 
            pygame.draw.line(screen, BLACK, (x,y+w),(x+w,y+w),1) # Horizontal DOWN Line
            pygame.draw.line(screen, BLACK, (x+w,y),(x+w,y+w),1) # Vertical LEFT Line
            pygame.display.update()
            grid.append((x,y))
            x += 20

def cover_down(x,y,w):
    pygame.draw.rect(screen, WHITE, (x+1,y+1,w-1,2*w-1), 0)     # Destroys horizontal wall down
    pygame.display.update()

def cover_right(x,y,w):
    pygame.draw.rect(screen, WHITE, (x+1,y+1,2*w-1,w-1), 0)     # Destroys vertical wall to the right
    pygame.display.update()

def cover_left(x,y,w):
    pygame.draw.rect(screen, WHITE, (x-w+1,y+1,2*w-1,w-1), 0)  # Destroys vertical wall to the left
    pygame.display.update()

def cover_up(x,y,w):
    pygame.draw.rect(screen, WHITE, (x+1,y-w+1,w-1,2*w-1), 0)  # Destroys horizontal wall up
    pygame.display.update()

# Function that solves maze

def solve_grid(x,y,w):

    visited.append((x,y))
    stack.append((x,y))

    while len(stack) > 0:
        
        neighbors = []

        if (x+20,y) in grid and (x+20,y) not in visited:
            neighbors.append("RIGHT")
        if (x,y+20) in grid and (x,y+20) not in visited:
            neighbors.append("DOWN")
        if (x,y-20) in grid and (x,y-20) not in visited:
            neighbors.append("UP")
        if (x-20,y) in grid and (x-20,y) not in visited:
            neighbors.append("LEFT")

        if len(neighbors) > 0:
            check = random.choice(neighbors)

            if check == "RIGHT":
                cover_right(x,y,w)
                visited.append((x+20,y))
                stack.append((x+20,y))
                x = x + w

            if check == "LEFT":
                cover_left(x,y,w)
                visited.append((x-20,y))
                stack.append((x-20,y))
                x = x - w

            if check == "UP":
                cover_up(x,y,w)
                visited.append((x,y-20))
                stack.append((x,y-20))
                y = y - w

            if check == "DOWN":
                cover_down(x,y,w)
                visited.append((x,y+20))
                stack.append((x,y+20))
                y = y + w

        else:
            x,y = stack.pop()
            

# Calling the functions

build_grid(x,y,w)
solve_grid(x,y,w)
cover_right(400,420,w)

# Check if the Quit button has been pressed

done = True
while done:
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = False