

# This subroutine will get three sides from the user
# These will be returned in a list of strings
def getTriangleSides():

    # Initialise the sides as an empty list
    sides = []

    print("\nEnter the three triangle sides as integers greater than zero")
    for i in range(3):
        sides.append(input("Enter a side length: "))
    print("")

    return sides


# This subroutine will accept a list of three side lengths of type string
# It will validate the sides and return whether or not the sides are valid
# Valid sides are positive integers
def validateSides(sides):

    valid = True

    # Attempt to convert the sides to integers in a "try"
    # If this fails it will be caught in the "except"
    try:
        for sideLength in sides:
            intSideLength = int(sideLength)

            # Check if positive
            if intSideLength <= 0:
                valid = False
    except ValueError:
        valid = False

    return valid


# This subroutine will accept a valid list of three side lengths of type
#    integer in ascending order
# It will determine and display the classification of the triangle
# The following classifications will be determined:
#  - Isoscelles
#  - Equilateral
#  - Scalene
#  - Right Angled (isoscelles and scalene triangles will be checked for this)
#  - Impossible triangle
def classifyTriangle(sides):

    # Check for impossible triangle
    if sides[0] + sides[1] <= sides[2]:
        print("This is an impossible triangle")

    # Check for equilateral triangle
    elif sides[0] == sides[1] and sides[0] == sides[2]:
        print("This is an equilateral triangle")

    # It will be scalene or isoscelles, These can also be right-angled
    else:

        # Check for isoscelles
        if (sides[0] == sides[1] or
            sides[0] == sides[2] or
            sides[1] == sides[2]):

            print("This is an isocelles triangle")
        else:
            print("This is a scalene triangle")

        # Check for right angled
        if (sides[0] ** 2) + (sides[1] ** 2) == sides[2] ** 2:
            print("This is also a right-angled triangle")


# This is the controlling module for the identify triangles feature
def identifyTrianglesModule():

    cont = "y"
    while cont == "y":

        sides = getTriangleSides()

        # If the sides are valid, convert to a sorted integer list
        #   and classify them
        # Otherwise print an error
        if validateSides(sides):
            for i in range(3):
                sides[i] = int(sides[i])
            sides.sort()
            classifyTriangle(sides)
        else:
            print("Please enter side lengths as positive integers")

        # Ask if user wants to continue
        print("")
        cont = input(("Enter 'y' to continue with triangle classifications. "
                      "Or any other key to return to the main menu: "))


# This is the mainline module
# It will control the main menu and call the other modules as requested
def main():

    print("Welcome the Maths Ed program")

    # This loop is for the main menu
    option = "99"
    while option != "0":

        print("\nSelect from the following options: ")
        print("  1: Identify Triangles")
        print("  2: Area Calculator")
        print("  3: Pythagoras' Theorem")
        print("  0: Quit")

        option = input("\nEnter your selection: ")

        # Call the user selected module
        if option == "1":
            identifyTrianglesModule()
        elif option == "2":
            pass
        elif option == "3":
            pass
        elif option == "4":
            pass
        elif option == "0":
            pass
        else:
            print("Please enter a valid option")


# This code is a Python convention to call the main subroutine
#   if this file is directly run
# If the file is imported instead, the main subroutine will not be called
if __name__ == '__main__':
    main()
