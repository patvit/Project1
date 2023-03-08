#задача 1 и 2

from pprint import pprint
cook_quantity = {}
def get_shop_list_by_dishes(dishes, person_count):
    for dish in dishes:
        parts_num = len(cook_book[dish])
        name = cook_book[dish]
        index = 0
        for index in range(parts_num):
            ingredient_name = name[index]['ingredient_name']
            quantity = int(name[index]['quantity']) * person_count
            measure = name[index]['measure']

            if ingredient_name in cook_quantity:
                cook_quantity[ingredient_name]['quantity'] += quantity
            else:
                cook_quantity[ingredient_name] = {
                   'measure' : measure,
                    'quantity': quantity
                }

with open('recipes.txt', 'rt') as file:
    cook_book = {}
    for line in file:
        cook_name = line.strip()
        parts_num = int(file.readline())
        ingredients = []
        for _ in range(parts_num):
            ingredient_name, quantity, measure = file.readline().split(' | ')
            ingredients.append({
            'ingredient_name' :  ingredient_name,
            'quantity' : quantity,
            'measure' : measure
            })
        file.readline()
        cook_book[cook_name] = ingredients

get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)
pprint(cook_quantity)


#Задача 3
files = {}
with open('1.txt', 'rt') as file:
    num1 = len(file.readlines())
    files[num1]= 1
    file.close()

with open('2.txt', 'rt') as file:
    num2 = len(file.readlines())
    files[num2] = 2
    file.close()

with open('3.txt', 'rt') as file:
    num3 = len(file.readlines())
    files[num3] = 3
    file.close()

number = [num1, num2, num3]
cur_file = min(number)
#file = str(files[cur_file])+'.txt'

with open('4.txt', 'w') as document:
    while len(number) > 0:
        with open(str(files[cur_file])+'.txt', 'rt') as file:
            document.write(str(files[cur_file])+'.txt')
            document.write(str('\n'))
            document.write(str(cur_file)+str('\n'))

            for line in file:
                document.write(line)
            document.write(str('\n'))
            file.close()
            if len(number) > 1:
                number.remove(cur_file)
                cur_file = min(number)
            else:
                cur_file = number[0]
                number.remove(cur_file)
document.close()


