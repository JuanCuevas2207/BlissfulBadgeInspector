from PIL import Image, ImageDraw

def verify_badge(img_path):

    #Open the image in the given path "img_path"
    img = Image.open(img_path)

    #Validate if the image size is 512x512
    if img.size != (512, 512):
        return False, "Image size must be 512x512, try to use the image converter!"
    
    #If everything looks good, return a successful verification
    return True, "Badge verification successful"


img_path = "TestBadges\happy_face.png"

result, message = verify_badge(img_path)

if result:
    print("Verified")
else:
    print(f"Failed: {message}")