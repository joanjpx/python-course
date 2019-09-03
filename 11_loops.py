array = list(range(1,100));

#print(array);

## FOR BASIC
for i in range(1,10):
    print (i);

##Example 2
for item in array:
    print(f"Number is:{item}");
    if item == 10:
        print("He llegado a 10");
        break;

## Working with strings
for letter in "Hello World":
    print(letter);



## WHILE LOOP
count = 1;

while count <= 10:
    count = count+1;
    print(count);