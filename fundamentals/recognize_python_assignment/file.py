# variable declaration
"""
multiline
comment
"""
#data type number
num1 = 42
num2 = 2.3
#data type boolean
boolean = True
#data type string
string = 'Hello World'
#initialize a list
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives']
#initialize a dictionary
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False}
#initialize a tuple
fruit = ('blueberry', 'strawberry', 'banana')
#log statement
#access values of tuple
print(type(fruit))
#access a list value
print(pizza_toppings[1])
#add a value to a list
pizza_toppings.append('Mushrooms')
#log statement
print(person['name'])
#change dictionary value
person['name'] = 'George'
#add a dictionary value
person['eye_color'] = 'blue'
#access value and log
print(fruit[2])

if num1 > 45:
    print("It's greater")
else:
    print("It's lower")

#length check
if len(string) < 5:
    print("It's a short word!")
#else if
elif len(string) > 15:
    print("It's a long word!")
else:
    print("Just right!")

for x in range(5):
    print(x)
for x in range(2,5):
    print(x)
for x in range(2,10,3):
    print(x)
x = 0
while(x < 5):
    print(x)
    x += 1

#remove last item and then remove item in position 1 from the list 
pizza_toppings.pop()
pizza_toppings.pop(1)

print(person)
person.pop('eye_color')
print(person)

for topping in pizza_toppings:
    if topping == 'Pepperoni':
        continue
    print('After 1st if statement')
    if topping == 'Olives':
        break
#function parameter
def print_hello_ten_times():
#function argument
    for num in range(10):
        print('Hello')

#function return
print_hello_ten_times()

def print_hello_x_times(x):
    for num in range(x):
        print('Hello')

print_hello_x_times(4)

def print_hello_x_or_ten_times(x = 10):
    for num in range(x):
        print('Hello')

print_hello_x_or_ten_times()
print_hello_x_or_ten_times(4)


"""
Bonus section
"""

# print(num3)
# num3 = 72
# fruit[0] = 'cranberry'
# print(person['favorite_team'])
# print(pizza_toppings[7])
#   print(boolean)
# fruit.append('raspberry')
# fruit.pop(1)