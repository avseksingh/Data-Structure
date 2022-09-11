class Person:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

    def __str__(self):
        name = self.name
        age = self.age
        address = self.address
        return "Name={0}, Age={1}, Address={2},".format(name, age, address)


class Employee(Person):
    def __init__(self, name, age, address, post, salary):
        Person.__init__(self, name, age, address)
        self.post = post
        self.salary = salary

    def __str__(self):
        return "{0}, Salary={1}, Post={2},".format(Person.__str__(self), self.salary, self.post)

class Manager(Employee):
    def __init__(self, name, age, address, post, salary, branch):
        Employee.__init__(self, name, age, address, post, salary)
        self.branch = branch

    def __str__(self):
        return "{0}, Branch={1}".format(Employee.__str__(self), self.branch)

o = Person("Amit", 30, "Varanasi")
emp = Employee("Abhi", 29, "Ghazipur", "Software Eng", 10000)
mng = Manager("Abhi", 29, "Ghazipur", "Software Eng", 10000, "Saidpur")
print(mng)
