import pygame
from math import floor
import sort

# initialize game engine
pygame.init()

# set screen width/height and caption
screenWidth = 600
screenHeight = 600
size = [screenWidth, screenHeight]
backgroundColor = (255, 255, 255)

screen = pygame.display.set_mode(size)
pygame.display.set_caption('My Program')

# initialize clock. used later in the loop.
clock = pygame.time.Clock()

# initialize variables and game logic
listLength = 128
listToSort = sort.shuffledRange(listLength, listLength)

sortHistory = sort.mergeSort(listToSort)
currentStep = -1
stepSize = 2

unitWidth = screenWidth / listLength
unitHeight = screenHeight / listLength

# Loop until the user clicks close button
while True:
    # write event handlers here
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            break

    # write game logic here
    if currentStep + stepSize < len(sortHistory) - 1:
        currentStep += stepSize
    else:
        currentStep = len(sortHistory) - 1

    # clear the screen before drawing
    screen.fill(backgroundColor)

    # write draw code here
    for i in range(listLength):
        pygame.draw.rect(
            pygame.display.get_surface(),
            (
                floor(i * 255 / listLength),
                100,
                floor(sortHistory[currentStep][i] * 255 / listLength)
                ),
            pygame.Rect(
                i * unitWidth,
                screenHeight - sortHistory[currentStep][i] * unitHeight,
                unitWidth,
                sortHistory[currentStep][i] * unitHeight
                )
            )

    # display what’s drawn. this might change.
    pygame.display.update()

    # run at 20 fps
    clock.tick(20)

# close the window and quit
pygame.quit()
