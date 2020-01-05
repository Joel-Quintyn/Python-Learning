"""
SYNOPSIS: This Program Was Rewritten From C On My Learning Journey Of Python, It Is A Name Counter Using While Loop.
"""

i = 0

while True:
    name = str(input("Enter A Name: "))
    i = i + 1

    x = int(input("\nPress 1 To Enter Another Name\nPress 0 To Finish\n"))

    if x == 0:
        break

print("You Entered {} Names".format(i))
