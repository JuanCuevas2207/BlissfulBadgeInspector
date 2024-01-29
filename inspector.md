# Badge Verification
This Python script uses the Pillow (PIL) library, the color_range function, and the imghdr library to verify whether a badge image meets certain requirements. The script performs the following operations:

## 1. verify_happy_colors Function
This function checks if a given pixel color is within the range of "happy colors." It compares the pixel color with a predefined range of happy colors and returns True if the color is considered happy.
>**NOTE:** to add or change colors go to the [colors file](colors.py), there you will find the list. These colors were chosen according to the color psychology (https://www.color-meanings.com/happy-colors-boost-mood/), which is summarized in the following diagram.
>
>![WhatsApp Image 2024-01-28 at 1 53 15 PM](https://github.com/JuanCuevas2207/BlissfulBadgeInspector/assets/67801108/c67f1544-18c7-4ef9-8657-261b5b1d78ca)


## 2. verify_badge Function
This function performs several checks to verify if a badge image meets specified requirements.

**Checks:**
1. Image Format Check:
* Uses the imghdr library to verify if the image format is PNG.
* If the format is not PNG or the image path is invalid, returns an error message.

2. Image Size Check:
* Verifies if the image size is 512x512 pixels.
* If the size is incorrect, returns an error message.

3. Non-Transparent Pixels Check:
* Creates a mask with a circular shape to define the area where non-transparent pixels should be.
* Checks if any non-transparent pixels exist outside the circular area.
* Returns an error message if transparent pixels are found outside the circle.

4. Happy Colors Check:
* Counts the number of pixels within the image that have colors considered "happy."
* If the count is less than half of the total pixels (131,072 out of 262,144), returns an error message.
* The threshold of 131,072 pixels is defined based on the assumption that at least half of the pixels should be happy colors.
