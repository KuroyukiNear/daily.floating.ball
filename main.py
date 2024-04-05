import pygame
import random
from math import cos, sin, radians
from moviepy.editor import VideoClip

# Initialize pygame
pygame.init()

# Set the dimensions of the screen (in portrait orientation)
width, height = 1280, 720
screen = pygame.display.set_mode((width, height))

# Set up colors
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Set up the circle parameters
radius = 50
circle_color = RED

# Set up the frame rate
FPS = 24

# Define the function to generate starting position and velocities based on the input string
def generate_start_and_velocities(input_string):
    random.seed(input_string)
    x = random.randint(radius, width - radius)
    y = random.randint(radius, height - radius)
    speed = 10
    angle = random.uniform(0, 360)  # Angle in degrees
    vx = speed * cos(radians(angle))
    vy = speed * sin(radians(angle))
    return x, y, vx, vy

# Define the function to draw each frame
def draw_frame(t):
    global x, y, vx, vy
    # Update the position of the circle
    x += vx
    y += vy

    # Bounce off the walls
    if x - radius < 0 or x + radius > width:
        vx = -vx
    if y - radius < 0 or y + radius > height:
        vy = -vy

    # Clear the screen
    screen.fill(BLACK)

    # Draw the circle
    pygame.draw.circle(screen, circle_color, (int(x), int(y)), radius)

    # Return the current frame as an array
    return pygame.surfarray.array3d(screen)

# Main function to create the video clip
def create_video(input_string, save_directory):
    global x, y, vx, vy
    x, y, vx, vy = generate_start_and_velocities(input_string)
    animation = VideoClip(draw_frame, duration=60)  # Set the duration of the video in seconds
    animation.write_videofile(save_directory + "Day_" + input_string + ".mp4", codec="libx264", fps=FPS, bitrate="5000k")

# Example input string and directory path (replace these with your desired values)
input_string = input("Input a number\n>>")
save_directory = "./balls/"

# Create the video with the specified input string and directory path
create_video(input_string, save_directory)

day = int(input_string)
while True:
    day += 1
    daylimit = day + 1
    if day == daylimit:
        break
    else:
        create_video(str(day), save_directory)

# Clean up
pygame.quit()
