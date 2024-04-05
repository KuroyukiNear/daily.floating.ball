import pygame
import os

# Initialize pygame
pygame.init()

# Set the dimensions of the image
width, height = 180, 180

# Set up colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Set up the circle parameters
radius = 60
circle_color = RED

# Create a surface with an alpha channel for the image (RGBA)
image_surface = pygame.Surface((width, height), pygame.SRCALPHA)

# Set the background color with alpha value of 0 (transparent)
image_surface.fill((0, 0, 0, 0))

# Calculate the center of the image
center_x = width // 2
center_y = height // 2

# Draw the circle in the center of the image
pygame.draw.circle(image_surface, circle_color, (center_x, center_y), radius)

# Save the image to a file
image_file = f"./img/ball_{width}x{height}.png"
pygame.image.save(image_surface, image_file)

# Print the path to the saved image file
print("Image saved:", os.path.abspath(image_file))

# Quit pygame
pygame.quit()
