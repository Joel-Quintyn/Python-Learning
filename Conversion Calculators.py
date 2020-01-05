"""
SYNOPSIS: This Program Was Rewritten From C On My Learning Journey Of Python.
"""


def opt_error():
    print("\nNot A Valid Option, Exit & Try Again")


print("<-------------Converter------------->\n")

# Conversion Rates #
con_rate_usd: float = 208.48
con_rate_cad: float = 157.10
con_rate_wght: float = 2.20462

print("  Please Choose A Conversion Method\n")
print("    ~ Currency Conversion => 1")
print("    ~ Time Conversion     => 2")
print("    ~ Weight Conversion   => 3")

choice = int(input("\n	   Input Choice: "))

if choice == 1:

    print("\n<--------Currency Conversion-------->\n")

    print("       Choose Conversion Type:")
    print("        ~ GYD -> USD => 1")
    print("        ~ USD -> GYD => 2")
    print("        ~ GYD -> CAD => 3")
    print("        ~ CAD -> GYD => 4")

    curr_choice = int(input("\n	   Input Choice: "))

    if curr_choice == 1:
        gyd = float(input("\nEnter Amount (GYD): $"))
        usd: float = gyd / con_rate_usd
        print("\nConversion:\nGYD - ${}\nUSD - ${}".format(gyd, usd))

    elif curr_choice == 2:
        usd = float(input("\nEnter Amount (USD): $"))
        gyd: float = usd * con_rate_usd
        print("\nConversion:\nUSD - ${}\nGYD - ${}".format(usd, gyd))

    elif curr_choice == 3:
        gyd = float(input("\nEnter Amount (GYD): $"))
        cad: float = gyd / con_rate_cad
        print("\nConversion:\nGYD - ${}\nCAD - ${}".format(gyd, cad))

    elif curr_choice == 4:
        cad = float(input("\nEnter Amount (CAD): $"))
        gyd: float = cad * con_rate_cad
        print("\nConversion:\nCAD - ${}\nGYD - ${}".format(cad, gyd))

    elif curr_choice > 4 or curr_choice < 0:
        opt_error()


elif choice == 2:
    print("\n<--------Time Conversion-------->\n")

    print("       Choose Conversion Type:")
    print("        ~ HRS -> MINS => 1")
    print("        ~ MINS -> HRS => 2")

    time_choice = int(input("\n	   Input Choice: "))

    if time_choice == 1:
        hrs = int(input("\nEnter Time (HRS): "))
        mins: float = hrs * 60
        print("\nConversion\nHRS - {}\nMINS - {}".format(hrs, mins))

    elif time_choice == 2:
        mins = int(input("\nEnter Time (MINS): "))
        hrs: float = mins / 60
        print("\nConversion\nMINS - {}\nHRS - {}".format(mins, hrs))

    elif time_choice > 2 or time_choice < 0:
        opt_error()


elif choice == 3:
    print("\n<--------Weight Conversion-------->\n")

    print("       Choose Conversion Type:")
    print("        ~ LBS -> KG => 1")
    print("        ~ KG -> LBS => 2")

    wght_choice = int(input("\n	   Input Choice: "))

    if wght_choice == 1:
        lbs = float(input("\nEnter Weight (LBS): "))
        kg: float = lbs / con_rate_wght
        print("\nConversion\nLBS - {}\nKG - {}".format(lbs, kg))

    elif wght_choice == 2:
        kg = float(input("\nEnter Weight (LBS): "))
        lbs: float = kg * con_rate_wght
        print("\nConversion\nKG - {}\nLBS - {}".format(kg, lbs))

    elif wght_choice > 2 or wght_choice < 0:
        opt_error()

else:
    opt_error()
