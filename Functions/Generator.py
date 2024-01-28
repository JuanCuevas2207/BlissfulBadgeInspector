from PIL import Image, ImageDraw
import random

def is_happy_color(pixel):
    # Define a range of happy colors, you can customize this based on your preference
    happy_color_range = [(240, 87, 108), (255, 195, 77), (0, 204, 204)]
    
    # Check if the pixel color is within the happy color range
    return any(all(abs(pixel[i] - color[i]) < 20 for i in range(3)) for color in happy_color_range)

def generate_happy_avatar():
    # Create a 512x512 image with a white background
    img = Image.new("RGBA", (512, 512), (255, 255, 255, 255))
    draw = ImageDraw.Draw(img)

    # Draw a circle for the avatar
    draw.ellipse((50, 50, 462, 462), fill=(255, 255, 255, 255))

    # Fill the circle with random happy colors
    for x in range(50, 462):
        for y in range(50, 462):
            if (x - 256)**2 + (y - 256)**2 <= 200**2:  # Check if the pixel is within the circle
                color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255), 255)
                if is_happy_color(color[:3]):
                    img.putpixel((x, y), color)

    img.save("TestBadges/happy_avatar.png")

def draw_happy_face():
    # Create a 512x512 image with a white background
    img = Image.new("RGBA", (512, 512), (255, 255, 255, 255))
    draw = ImageDraw.Draw(img)

    # Draw a circle for the face
    draw.ellipse((50, 50, 462, 462), fill=(255, 255, 255, 255), outline=(0, 0, 0, 255))

    # Draw eyes
    draw.ellipse((150, 150, 200, 200), fill=(0, 0, 0, 255))  # Left eye
    draw.ellipse((312, 150, 362, 200), fill=(0, 0, 0, 255))  # Right eye

    # Draw a smiling mouth
    draw.arc((150, 250, 362, 400), start=0, end=180, fill=(0, 0, 0, 255), width=5)

    img.save("TestBadges/happy_face.bmp")

def yellow():
    # Create a drawing object
    img = Image.new("RGBA", (512, 512), (255, 255, 255, 255))
    draw = ImageDraw.Draw(img)

    # Get image dimensions
    width, height = img.size

    # Set circle properties
    circle_radius = min(width, height) 
    circle_center = (width // 2, height // 2)
    circle_color = ((0, 204, 204))  # Yellow color with full opacity

    # Draw the yellow circle
    draw.ellipse((circle_center[0] - circle_radius, circle_center[1] - circle_radius,
                    circle_center[0] + circle_radius, circle_center[1] + circle_radius),
                    fill=circle_color, outline=None)
    
    img.save("TestBadges/yellow.png")

# Generate and save the happy avatar
draw_happy_face()
generate_happy_avatar()
yellow()