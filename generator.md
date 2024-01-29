# Avatar Generator
This Python script utilizes the Pillow (PIL) library to create two types of avatars: one that does not fulfill certain requirements (generate_bad_avatar) and another that fulfills the requirements (generate_happy_avatar). The script performs the following operations:

## 1. 'generate_bad_avatar' Function
This function creates an avatar that does not fulfill the specified requirements. The avatar is saved as a bitmap (.bmp) image.

Steps:

1. Image Initialization:
* Creates a 512x512 image with a white background using Image.new.

2. Drawing Operations:
* Draws a white ellipse (face) on the image.
* Draws black ellipses for the eyes.
* Draws a black arc to represent a smiling mouth.
  
3. Image Saving:
* Saves the image to the path specified by new_badge_path.

4. Return:
* Returns the path where the avatar is saved.
## 2. generate_happy_avatar Function
This function creates an avatar that fulfills certain requirements. The avatar is saved as a PNG (.png) image.

Steps:

1. Image Initialization:
* Creates a 512x512 image with a transparent background using Image.new.

2. Drawing Operations:
* Draws a circle (face) as background, the color is randomly chosen from the predefined happy colors obtained from the color_range function.
* Draws black ellipses for the eyes.
* Draws a black arc to represent a smiling mouth.

3. Image Saving:
* Saves the image to the path specified by new_badge_path.

4. Return:
* Returns the path where the avatar is saved.
