from PIL import Image, ImageDraw #Library that helps image validation
import imghdr #Library to check the image format 

def verify_happy_colors(pixel):
    # Define a range of happy colors (adjust as needed)
    happy_color_range = [(240, 87, 108), (255, 195, 77), (0, 204, 204)]

    # Check if the pixel color is within the happy color range
    return any(all(abs(pixel[i] - color[i]) < 20 for i in range(3)) for color in happy_color_range)

def verify_badge(img_path):
    #Validate if the format of the image is .png
    try:
        if imghdr.what(img_path) != "png":
            return False, "Image format must be .png, try to use badge converter!"
    except:
        return False, "Image path does not exist"

    #Open the image in the given path "img_path"
    img = Image.open(img_path)
    
    #Validate if the image size is 512x512
    if img.size != (512, 512):
        return False, "Image size must be 512x512, try to use the badge converter!"
    
    #Validate if there are non-transparent pixels are within the circle
    width, height = img.size
    mask = Image.new("L", (width, height), 0) #Create a mask with a circle to verify pixels with avatar inside
    draw_mask = ImageDraw.Draw(mask)
    draw_mask.ellipse((0, 0, width, height), fill=255)
    non_transparent_pixels = img.convert("RGBA").getdata()
    #Check if alpha channel (transparency) 'pixel[3]' and mask mask_pixel is greater than 0, meaning it's non-transparent.
    if any(pixel[3] == 0 and mask_pixel == 255 for pixel, mask_pixel in zip(non_transparent_pixels, mask.getdata())):
        return False, "Image must not have transparent pixels within the circle , try to use the badge converter!"
    
    # Verify if the colors of the badge give a happy feeling
    if any(not verify_happy_colors(pixel[:3]) for pixel in img.getdata() if pixel[3] > 0):
        return False, "Colors of the badge must give a 'happy' feeling, try to use the badge converter!"
    
    #If everything looks good, return a successful verification
    return True, "Badge verification successful"