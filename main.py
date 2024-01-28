from Functions import Inspector, Converter, Generator # The import functions from "Functions" folder, these are the important ones for the badge!

img_path = "TestBadges/test_3.jpg" # Here you have to put the path of the image to test it in console mode
menu_iteration = True # Variable that keeps the user in the menu

# Function that calls Inspector file to verify if the badge fulfills the requirements
def verify(img_path):
    print(f"\nValidating badge in path {img_path}...\n")
    result, message = Inspector.verify_badge(img_path)
    if result:
        print("Badge validation successful! Your badge meets requirements\n")
    else:
        print(f"Unsuccessful validation: {message}\n")

# This the menu for tests in console mode!
while menu_iteration:
    menu_option = int(input("Enter a menu option:\n1. Validate badge\n2. Use badge converter\n3. Generate a badge\n4. Exit\n"))
    match menu_option:
        #Case 1: verifies the badge in the img_path
        case 1:
            verify(img_path)
        # Case 2: calls Converter file, this has the function to convert a badge that meets the requirements and change img_path
        case 2: 
            print(f"\nConverting badge in path {img_path}...\n")
            img_path = Converter.convert(img_path)
            verify(img_path)
        # Case 3: this option gives the user the opportunity to auto-generate a type of badge
        case 3:
            generator_iteration = True
            while generator_iteration:
                generator_option = int(input("\nEnter a menu option:\n1. Generate avatar that fulfill requirements\n2. Generate avatar that not fulfill requirements\n3. Exit sub-menu\n"))
                match generator_option:
                    case 1:
                        img_path = Generator.generate_happy_avatar()
                        print(f"\nNew badge generated in {img_path}")
                        verify(img_path)
                        generator_iteration = False
                    case 2: 
                        img_path = Generator.generate_bad_avatar()
                        print(f"\nNew badge generated in {img_path}")
                        verify(img_path)
                        generator_iteration = False
                    case 3: 
                        generator_iteration = False
                    case _:
                        print("The input value is not valid or is not a number value, please try again\n")
        # Case 4: allows you to exit the menu
        case 4:
            menu_iteration = False
        # Default case: in case the user enters an invalid value1
        case _:
            print("The input value is not valid or is not a number value, please try again\n")
1