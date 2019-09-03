#FUNCTIONS

def hello(parm="User"):
    print(f"Hello World {parm}");

hello("");

def add(numberOne=0,numberTwo=0):
    return(numberOne+numberTwo);

print(add(1,2));


#Lambda Functions
plus = lambda One,Two : One+Two

print(plus(100,30))