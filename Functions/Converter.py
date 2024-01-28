from PIL import Image

def convert(img_path):
    img = Image.open(img_path)
    img = img.resize((512, 512))

    if img.mode != 'RGBA':
        img = img.convert('RGBA')

    new_img_path = img_path.split(".",1)[0]+".png"
    img.save(new_img_path)

    return new_img_path