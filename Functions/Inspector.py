from PIL import Image, ImageDraw # Library that helps image validation
from colors import color_range # Import the colors consider as happy
import imghdr # Library to check the image format 

# Function that checks if the colors are within the range of "happy colors"
def verify_happy_colors(pixel):
    # Define a range of happy colors (adjust as needed)
    happy_color_range = color_range()

    # Check if the pixel color is within the happy color range
    if len(set(pixel[:3])) == 1 and pixel[:3] != (0,0,0):
        return True
    else:
        return any(all(abs(pixel[i] - color[i]) < 40 for i in range(3)) for color in happy_color_range)

# Function that checks badge requirements
def verify_badge(img_path):
    # Validate if the format of the image is .png
    try:
        if imghdr.what(img_path) != "png":
            return False, "Image format must be .png, try to use badge converter!"
    except:
        return False, "Image path does not exist"

    # Open the image in the given path "img_path"
    img = Image.open(img_path)
    
    # Validate if the image size is 512x512
    if img.size != (512, 512):
        return False, "Image size must be 512x512 pixels, try to use the badge converter!"
    
    # Validate if there are non-transparent pixels are within the circle
    width, height = img.size
    mask = Image.new("L", (width, height), 0) # Create a mask with a circle to verify pixels with avatar inside
    draw_mask = ImageDraw.Draw(mask)
    draw_mask.ellipse((0, 0, width, height), fill=255)
    non_transparent_pixels = img.convert("RGBA").getdata()
    # Check if alpha channel (transparency) 'pixel[3]' is greater than 0, meaning it's non-transparent
    if any(pixel[3] == 0 and mask_pixel == 255 for pixel, mask_pixel in zip(non_transparent_pixels, mask.getdata())):
        return False, "Image must not have transparent pixels within the circle , try to use the badge converter!"
    
    # Verify if the colors of the badge give a happy feeling
    happiness_counter = 0 # Counter value to count how many pixels are inside the range of happy colors
    for pixel in img.getdata():
        if pixel[3]>0:
            if verify_happy_colors(pixel[:3]):
                happiness_counter += 1
    # Verify if counter is greater than 131072 which is the 1/2 of the total pixels of the image that must be inside color range
    if(happiness_counter < 131072): 
        return False, "Colors of the badge must give a 'happy' feeling, try to use the badge converter!"
    
    # If everything looks good, return a successful verification
    return True, "Badge verification successful"