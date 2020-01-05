"""
SYNOPSIS: This Program Was Rewritten From C On My Learning Journey Of Python.
"""

print("\nThis Program Is Designed To Tell You If A Number Is A Odd Number Or An Even Number.\n");

num = int(input("Enter Your Number: "))

print("\n\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

if num % 2 == 0:
    print("The Number {} Is An Even Number.".format(num))

else:
    print("The Number {} Is A Odd Number.".format(num))

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
