
# This subroutine will get the triangle sides from the user
# It will return those sides as a list of strings
def getTriangleSides():

    # Inititalise sides as an empty list
    sides = []

    print("Enter the three sides lengths of the triangle")
    print("Use positive integer values\n")
    for i in range(3):
        sides.append(input("Enter a side length: "))

    return sides

    # for sideLength in sides:
    #     print(sideLength)

    # for i in range(3):
    #     print(sides[i])

# This function will take a list of sides (as strings)
# And validate them as positive intgers
def validateSides(sides):

    valid = True

    # Use a try/except to convert to integer and catch error if that fails
    try:
        for sideLength in sides:
            intSideLength = int(sideLength)
            if intSideLength <= 0:
                valid = False
    except ValueError:
        valid = False

    return valid

# This subroutine will display the type of triangle
# It will cover:
#  - Equilateral
#  - Scalene
#  - Isoscelles
#  - Right-angled
#  - Impossible Triangle
# It will accept a list of three sides of type integer
def classifyTriangle(sides):

    # Sort sides in ascending order
    sides.sort()

    # Check for impossible
    if sides[0] + sides[1] <= sides[2]:
        print("This is an impossible triangle")

    elif sides[0] == sides[1] and sides[0] == sides[2]:
        print("This is an equilateral triangle")

    # It must be scalene or isoscelles
    # These can also be right-angled 
    else:
        if (sides[0] == sides[1] or
            sides[0] == sides[2] or
            sides[1] == sides[2]):
            print("This is an isoscelles triangle")

        else:
            print("This is a scalene triangle")

        # Now check for right angled
        if (sides[0] ** 2) + (sides[1] ** 2) == sides[2] ** 2:
            print("This is also a right-angled triangle")
        




# This subroutine controls the Identify Triangles Module
# It will allow the user to identify multiple triangles
#  Or they can return to the main menu
def identifyTrianglesModule():

    # Get the triangle sides
    sides = getTriangleSides()

    valid = validateSides(sides)
    if valid:
        # Convert to integers
        for i in range(3):
            sides[i] = int(sides[i])

        classifyTriangle(sides)
    else:
        print("Please enter valid sides as positive integers")

    
# This is the mainline
# It will control the main menu, and then use subroutines
# for each module
def main():
    
    identifyTrianglesModule()


# This code is a Python convention to call the main subroutine
#   if this file is directly run
# If the file is imported instead, the main subroutine will not be called
if __name__ == '__main__':
    main()
