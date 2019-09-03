array = list(range(1,100));

#print(array);

for item in array:
    print(f"Number is:{item}");
    if item == 10:
        print("He llegado a 10");
        break;