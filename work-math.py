@@ -0,0 +1,28 @@
# Maths Stuff with Python
# Author: Ubial
# 12 November 2025

import math

# Machines are good at crunching numbers -
# faster and more accurately than most humans!
# Create a small program that calculates
# something useful to you (making you smile
# is useful). It should take user input, at
# use at least one of the number operators we
# saw in class: + / * -. You may modify one
# of your previous exercises to include
# calculations, if you wish.

def main():
    print("What are two short sides of a triangle?")
    a = int(input("Side 1: "))
    b = int(input("Side 2: "))

    hyp = math.sqrt(a ** 2 + b ** 2)

    print(f"The hypotenuse is: {hyp}")


if __name__ == "__main__":
    main()
