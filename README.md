# BlissfulBadgeInspector
BlissfulBadgeInspector is an application that validates the loading of avatars before they are uploaded. Developed by Juan Cuevas!

## Overview

This project validates the loading of an avatar that must have the following features:
1. The format must be in png
2. The avatar must be inside a circle.
3. The image must have size 512x512 pixels.
4. The pixels inside the circle must not be transparent.
5. The colors of the avatar should give a feeling of happiness. :)

It also has functions to test in real time if the avatar is valid, to generate a random avatar in case you don't have one and even to change the current format.

## Prerequisites

> [!IMPORTANT]
> 
> Project BlissfulBadgeInspector requires Python 3.7 or later. If you don't have Python installed, you can download it from the official website: [Python Downloads](https://www.python.org/downloads/).
> During the installation process, make sure to check the box that says "Add Python to PATH" to easily run Python from the command line. 
> 
> There are different libraries to be installed before you can run the following steps, please validate the following instructions before continue [instructions](prerequisites_instructions.md).

## Console run

After everything is correctly installed, you can perform tests from console by running the [main.py](main.py) file, it will run a menu that allows:

1. Validate if the badge fulfills the specifications
2. Convert the badge to the correct format
3. Generate a badge (Option that has another submenu):
   1. Generate a random avatar that meets the specifications
   2. Generate an avatar that does not meet the specifications (for testing)
4. Exit menu
> **_NOTE:_**  In case of entering an erroneous entry, it prompts again to enter a new value.

![image](https://github.com/JuanCuevas2207/BlissfulBadgeInspector/assets/67801108/f8321dd6-d2bd-4a7c-8d2c-867b543afde6)

Just enter the value of the function you want to use.

## Change the test image

Currently the project points to the image "test_3.jpg", which is a test badge located in the [TestBadges](TestBadges) folder, to test with a different image you must make the change in the [main.py](main.py) file in line 3 as follows 

![image](https://github.com/JuanCuevas2207/BlissfulBadgeInspector/assets/67801108/50e11165-99ce-4016-ba50-ad595473498d)

## Functions

The most important files used are the following: 
* [Converter](converter.md): used to convert the badge to the requested specifications
* [Generator](generator.md): used to create random avatars that fulfill or not the requirements
* [Inspector](inspector.md): **Main file** this contains the main requested function that is responsible for validating the badge
> **_NOTE:_**  For more details of each file (functions), click on the file title .
