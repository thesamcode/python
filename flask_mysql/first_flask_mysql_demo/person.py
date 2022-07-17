class Person:
    def __init__(self, data):
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.fullname = f"{self.first_name} {self.last_name}"

    def info(self):
        print(f"fullname: {self.fullname}")


all_users = [

    {
        'first_name': 'tyler',
        'last_name': 'tbo',
        'age': 34
    }
    {
        'first_name': 'joe',
        'last_name': 'schmoe',
        'age': 37
    }
    {
        'first_name': 'john',
        'last_name': 'smith',
        'age': 38
    }

]





employees = []

for worker in all_users:
    employees.append( Person(worker))

for person in employees:
    person.info()