# parent class
class Employee:
    def __init__(self, name, salary):
        self.name = name        # Store employee's name
        self.salary = salary    # Store employee's salary

    def __str__(self):
        return f"Name: {self.name}\nSalary: {self.salary}"  # Defines how to print an Employee

# child class
class Tester(Employee):  # Tester inherits from Employee
    def __init__(self, name, salary, tool):
        super().__init__(name, salary)  # Call Employee constructor to set name and salary
        self.tool = tool                # Add a new attribute specific to Tester

    def __str__(self):
        # Combine name, salary, and tool in a single string for printing
        return f"{self.name}\n{self.salary}\nTool: {self.tool}"

# Create a Tester object
tester1 = Tester("Dipendra", 50000, "Selenium")  # Create a Tester with name, salary, and tool

# Print details
print(tester1) 