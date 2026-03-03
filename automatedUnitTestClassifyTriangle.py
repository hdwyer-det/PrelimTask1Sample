import main_full_sample as main

print("Running automated unit test using a harness for the Classify Triangles subroutine")
print("This subroutine is to accept a list of three sides that are positive integers in ascending order")

# Test 1
# Impossible: sum of two short sides is equal to longest
print("\nTest 1: Impossible: sum of two short sides is equal to longest. 3, 3, 6")
main.classifyTriangle([3, 3, 6])

# Test 2
# Impossible: sum of two short sides is shorter to longest
print("\nTest 2: Impossible: sum of two short sides is shorter to longest. 2, 3, 6")
main.classifyTriangle([2, 3, 6])

# Test 3
# Equilateral
print("\nTest 3: Equilateral. 3, 3, 3")
main.classifyTriangle([3, 3, 3])

# Test 4
# Isoscelles, two short sides equal
print("\nTest 4: Isoscelles. 3, 3, 5")
main.classifyTriangle([3, 3, 5])

# Test 5
# Isoscelles, two long sides equal
print("\nTest 5: Isoscelles. 3, 5, 5")
main.classifyTriangle([3, 5, 5])

# Test 6
# Scalene
print("\nTest 6: Scalene. 3, 5, 7")
main.classifyTriangle([3, 5, 7])

# Test 7
# Scalene and Right Angled
print("\nTest 7: Scalene and right-angled. 6, 8, 10")
main.classifyTriangle([6, 8, 10])
