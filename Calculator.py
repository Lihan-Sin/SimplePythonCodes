ask = input("Do you want to calculate?\n").lower()

if ask != "yes":
    print("Okay")
    quit()
else:
    print("Okay. Let's start!")
    print("If you want to leave the calculator press \"Q\".")

while True:
    x = input("\nEnter calculation:- ")
    if x.lower() == "q":
        exit()
    
    c = eval(x)

    print("Calculation of", x, "is:-", c)
    print("*==========================================*")
    