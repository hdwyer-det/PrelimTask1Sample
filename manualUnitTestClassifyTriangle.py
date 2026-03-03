import main_full_sample as main

print("This is a harness for the Classify Triangles subroutine which can be used to run a manual unit test")
print("This subroutine is designed to accept a list of three sides that are positive integers in ascending order, so when testing the subroutine")
print("  only valid data should be entered\n")


cont = "y"
while cont == "y":
    sides = []
    for i in range(3):
        sides.append(int(input("Enter a triangle side: ")))
    main.classifyTriangle(sides)

    print("")
    cont = input("Enter 'y' to continue, or any other key to exit: ")
