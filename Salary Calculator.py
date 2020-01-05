"""
SYNOPSIS: This Program Was Rewritten From C On My Learning Journey Of Python.
"""

print("\nThis Program Is Designed To Calculate Your Net Pay & Overtime")

hours = int(input("\nEnter Your Hours Worked This Week:- "))

rop = int(input("Enter Your Rate Of Pay:- $"))

if hours > 40:
    regularpay = hours*rop
    overtime = (hours-40)*1.5
    netpay = regularpay + overtime

    print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~\nYour Overtime Pay Is ${}".format(overtime))
    print("Your Regular Pay Is ${}".format(regularpay))
    print("Your Net Pay Is ${}".format(netpay))

elif hours <= 40:
    regularpay = hours*40
    print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~\nYour Regular Pay Is {}".format(regularpay))
