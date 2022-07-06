import random
print(random.randint(2,5)) # provides a random number between 2 and 5

name = "Zen"
print("My name is", name)

name = "Zen"
print("My name is " + name)

first_name= "Tyler"
last_name = "Thibault"
age = 34

print(f"Hi my name is {first_name} {last_name} and I am {age} years old.")

print(first_name.upper())

print(True)
print(False)

if first_name == tyler:
    print("yes")

# an empty string is considered a false value

first_name = 1
last_name = "Thibault"
age = 36

if first_name:
    print("yes")
else 

# any number except zero will be a yes, 0 will make it a no because it is considered falsey

# arrays are called lists

brothers = ['tyler', 'curtis', 'joe']

print(brothers[1])
# gets curtis

brothers[1] = "bob"
# that will change curtis to bob

brothers.append("bob")
# this adds it to end of array

# objects use {} vs [] or ()
# in python the key vale needs to be in quotes

person = {
    'first_name' : 'tyler',
    'last_name' : 'tbo',
    'age' : 34
}

print(person['last_name'])

brothers = [ 
    {
    'first_name' : 'tyler',
    'last_name' : 'tbo',
    'age' : 34
    }
    {
    'first_name' : 'joe',
    'last_name' : 'tbo',
    'age' : 36
    }
    {
    'first_name' : 'curtis',
    'last_name' : 'tbo',
    'age' : 38
    }
]

# to get joe...

print(brothers[1]['first_name'])

person2 = ('tyler', 'tbo')
print(person2[0])
# that gets you tyler

# this type of list cannot be changed. Is a tuple. 

person3 = [person2[0], person2[1]]
person3[1]
print(person3)

brothers = ['tyler', 'curtis', 'joe']
# this will give the names
for brother in brothers:
    print(brother)

i=0
while (i<len(brothers)):
    print(brothers)
    i += 1

while (i<len(brothers)):
    if i % 2 == 0
        print(brothers)
    i +=1


brothers = ['tyler', 'curtis', 'joe', 'bob']

def randomize_list(new_list):
    return_list = []
    for item in new_list:
        random_num = random.randint(0, len(new_list)-1)
        item = new_list[random_num]
        return_list.append(item)

    return return_list

print(randomize_list(brothers))

def run_times(num, new_list):
    for indx in range(num):
        print(randomize_list(new_list))

run_times(5, brothers)

print(run_times(5, brothers))

#there will be a "none" at the end because the function returns nothing unless yopu give a return and a a word or something for it to return

def add(num1, num2=10):
    return num1 + num2

print(add(5,5))

#if it is print(add(5)) then it will use the 10 as the second num...

def add(num1, num2=10, num3=3):
    return (num1 + num2) * num3

print(add(5, num3=7, num2=2))
