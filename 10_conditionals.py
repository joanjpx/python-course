x = 20

if x > 30:
    print("X is greater than 30")
else:
    print("x is lower than 30")

name = input('nombre:');
ln = input('apellido:');

if name=="Joan":
    if ln=="Perez":
        print(f"You are {name} {ln}");
    else:
        print("You're Joan but not Perez");
else:
    print("You're not Joan Perez");

number = input('Give me a number');

if float(number) < 10 and float(number) > 0:
    print("This number is between 10-0");
else:
    print("This number is out of 10-0");