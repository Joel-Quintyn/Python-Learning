"""
SYNOPSIS: This Program Was Some Practice Of The For Loop In Python.
"""

for i in range(1, 13):
    line = ""
    for j in range(1, 13):
        line = line + str(i * j) + "\t"
    print(line)