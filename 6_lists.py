demo_list = [1,"Hola",True,[4,5,6,1,9],12.3];

colors = ["red", "green", "blue", "yellow"];


number_list = list([1,2,3,4]);
#print(type(number_list));

range_list = list(range(1,100));
#print(range_list);

## GET ALL METHODS 
#print(dir(colors));
#print(len(colors));
#print(colors[1]);
#print('red' in colors); True || False

## ADD ITEMS
colors.append('purple');
colors.extend(['cyan','magent']);
colors.extend(['pink','black']);
colors.insert(len(colors),'violet');

print(colors)

##REMOVE ITEMS
#colors.pop(0);
#colors.remove('pink');
#colors.clear()

print(colors)

## SORTING ITEMS
colors.sort()
#colors.sort(reverse=True)

## GETTING INDEX
#print(colors.index('red'));

## COUNTING ITEM
print(colors.count('red'))