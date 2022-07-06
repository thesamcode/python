
x = [ [5,2,3], [10,8,9] ] 
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

x[1][0] = 15
print(x)

students[0]['last_name'] = 'Bryant'
print(students)

sports_directory['soccer'][0] = 'Andres'
print(sports_directory)

z[0]['y'] = 30
print(z)

students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name': 'John', 'last_name' : 'Rosales'},
        {'first_name': 'Mark', 'last_name' : 'Guillen'},
        {'first_name': 'KB', 'last_name' : 'Tonel'}
    ]

# def iterateDictionary(students):
#     for i in range(0, len(students)):
#         print(each_key[i])

# iterateDictionary(students)

def iterateDictionary(students):
    for i in range(0, len(students)):
        print('first_name','-',students[i]['first_name'],',','last_name','-',students[i]['last_name'])

iterateDictionary(students)


def iterateDictionary2(key, some_list):
    for i in range(0, len(some_list)):
        print(some_list[i][key])

iterateDictionary2('first_name', students)

iterateDictionary2('last_name', students)

dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

# def printInfo(some_dict):
#     for key,value in some_dict.items():
#         print(len(some_dict),key)
#         for i in range(0, len(some_dict)):
#         # for key,value in some_dict.items():
        

# printInfo(dojo)

# def printInfo(some_dict):
#     for i in range(0, len(some_dict)):
#         for key in some_dict.keys():
#             print(key)
#             # for i in range(0, len(key)):
#             #     for value in some_dict.values():
#             #         print(value)
        
# printInfo(dojo)

# def printInfo(some_dict):
#     for i in range(0, len(some_dict)):
#         # for key in some_dict.keys():
#         print(key in some_dict[i])

# printInfo(dojo)

# def printInfo(some_dict):
#     # for i in range(0, len(some_dict)):
#     for key, value in some_dict.items():
#         print(some_dict.index(key),key)
#         for i in range(0, len(some_dict)):
#             print(value[i])

# printInfo(dojo)

def printInfo(some_dict):
    for key, value in some_dict.items():
        print(len(some_dict.get(key)),key.upper())
        for i in value:
            print(i)

printInfo(dojo)
