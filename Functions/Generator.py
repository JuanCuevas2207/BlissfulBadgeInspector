from PIL import Image, ImageDraw #Library that helps with image creation
from colors import color_range #Import the colors consider as happy
import random

# Function that create an avatar that not fulfill the requirements
def generate_bad_avatar():
    new_badge_path = "TestBadges/happy_face.bmp" # Path where the avatar will save

    # Create a 512x512 image with a white background
    img = Image.new("RGBA", (490, 530), (255, 255, 255, 255))
    draw = ImageDraw.Draw(img)

    # Draw a circle for the face
    draw.ellipse((50, 50, 440, 480), fill=(255, 255, 255, 255), outline='black')

    # Draw eyes
    draw.ellipse((150, 150, 200, 200), fill='black') #Left eye
    draw.ellipse((312, 150, 362, 200), fill='black') #Right eye

    # Draw a smiling mouth
    draw.arc((150, 250, 362, 400), start=0, end=180, fill='black', width=5)

    img.save(new_badge_path)
    return new_badge_path

# Function that create an avatar that fulfill the requirements
def generate_happy_avatar():
    new_badge_path = "TestBadges/happy_avatar.png" #Path where the avatar will save

    # Create a drawing object
    img = Image.new("RGBA", (512, 512), (255, 255, 255, 255))
    draw = ImageDraw.Draw(img)

    # Get image dimensions
    width, height = img.size

    # Set circle properties
    circle_radius = min(width, height) // 2
    circle_center = (width // 2, height // 2)
    circle_color = (random.choice(color_range()))  # Yellow color with full opacity

    # Draw the yellow circle
    draw.ellipse((circle_center[0] - circle_radius, circle_center[1] - circle_radius,
                    circle_center[0] + circle_radius, circle_center[1] + circle_radius),
                    fill=circle_color, outline=None)
    
    # Draw eyes
    draw.ellipse((150, 150, 200, 200), fill=(0, 0, 0, 255))  # Left eye
    draw.ellipse((312, 150, 362, 200), fill=(0, 0, 0, 255))  # Right eye

    # Draw a smiling mouth
    draw.arc((150, 250, 362, 400), start=0, end=180, fill=(0, 0, 0, 255), width=5)
    
    img.save(new_badge_path)
    return new_badge_path