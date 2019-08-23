## STRINGS
myString = "hello world";

## Dir para saber lo que se puede hacer con un string // Get Strings Functions

#print(dir(myString));
print(myString.upper());
print(myString.lower());
print(myString.swapcase());
print(myString.capitalize());

## CHAINED METHODS
print(myString.replace('hello','bye').upper());

print(myString.count('o'));

print(myString.startswith('hello'));