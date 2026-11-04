class Employee:
    def __init__(self, name, dept, salary):
        self.name = name
        self.dept = dept
        self.salary = salary

class Developer(Employee):
    def __init__(self, name, dept, salary, language):
        super().__init__(name, dept, salary)
        self.language = language

    def give_hike(self):
        self.salary = self.salary * 1.10

    def display(self):
        print(f"{self.name} ({self.dept}) earns {self.salary}, "
              f"codes in {self.language}")

dev = Developer("Neha", "IT", 70000, "Python")
dev.give_hike()
dev.display()