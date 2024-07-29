import pygame
import time

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
RECT_WIDTH = 200
RECT_HEIGHT = 100
RECT_COLOR = (0, 128, 255)
BACKGROUND_COLOR = (255, 255, 255)
BLINK_INTERVAL = 0.5  # seconds

# Create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Blinking Rectangle Animation")

# Rectangle Position
rect_x = (SCREEN_WIDTH - RECT_WIDTH) // 2
rect_y = (SCREEN_HEIGHT - RECT_HEIGHT) // 2

# Main loop
running = True
visible = True
last_blink_time = time.time()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill(BACKGROUND_COLOR)

    # Draw the rectangle if it is visible
    if visible:
        pygame.draw.rect(screen, RECT_COLOR, (rect_x, rect_y, RECT_WIDTH, RECT_HEIGHT))

    # Update the display
    pygame.display.flip()

    # Check if it's time to blink
    current_time = time.time()
    if current_time - last_blink_time >= BLINK_INTERVAL:
        visible = not visible
        last_blink_time = current_time

    # Control the frame rate
    pygame.time.Clock().tick(60)

# Quit Pygame
pygame.quit()
