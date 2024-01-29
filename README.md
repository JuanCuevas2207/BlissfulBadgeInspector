# BlissfulBadgeInspector
BlissfulBadgeInspector is an application that validates the loading of avatars before they are uploaded. Developed by Juan Cuevas!

## Table of content
**[Overview](#overview)**<br>
**[Prerequisites](#prerequisites)**<br>
**[Console run](#console-run)**<br>
**[Change the test image](#change-the-test-image)**<br>
**[Functions](#functions)**<br>
**[Run an example](#run-an-example)**<br>

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

## Run an example

Using Visual studio code (https://code.visualstudio.com/docs/python/python-tutorial), follow next steps:

1. Run the python file using the button in the upper right of the interface (as shown below)

   ![image](https://github.com/JuanCuevas2207/BlissfulBadgeInspector/assets/67801108/24747f3e-b2c2-4f9c-96bd-629cfde46aa4)

2. This will open a terminal in where the menu will be displayed
3. A test badge already exists in the folder, [we can change it whenever we want](#change-the-test-image), so we will run the first option for validate the badge changing the img_path for TestBadges/test_2.jpg (we can use the test_3.jpg, but the test_2.jpg have more details so we will used it for this example).

   ![image](https://github.com/JuanCuevas2207/BlissfulBadgeInspector/assets/67801108/6412685a-9db7-43b6-8989-73f3f493cd56)

4. As you can see, the validation is unsuccessful cause due to format not being png
5. We have two options here
   1. Run option two which will transform the badge we have in the ideal format (changing image format, file size, removing transaparent pixels inside the circle and changing to bright colors), this will save a new file in the "TestBadges" folder with the same name of the file + "_valid.png". Also, it will re-run the badge validation automatically with the new badge path.

      ![image](https://github.com/JuanCuevas2207/BlissfulBadgeInspector/assets/67801108/503189ab-0ea5-4649-9fa3-e0d86b72ba66)
      ![image](https://github.com/JuanCuevas2207/BlissfulBadgeInspector/assets/67801108/265b596a-a178-4305-94e3-26b4114af496)

   3. Run option three and then option one, which will create a new random badge that meets the specifications.

      ![image](https://github.com/JuanCuevas2207/BlissfulBadgeInspector/assets/67801108/2a4863d4-7ddd-480e-be13-2f611f6d80ba)
      ![image](https://github.com/JuanCuevas2207/BlissfulBadgeInspector/assets/67801108/41ac8cc0-7af8-40f0-94a6-925536af34d7)

      
6. Enter option 4 to exit the menu, or you can try any other function if you wish to do so 
