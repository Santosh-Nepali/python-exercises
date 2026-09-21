# class_inheritance

class Employee:
    total_employees=0
    def __init__(self, first_name, last_name):
        Employee.total_employees+=1
        self.employee_number=Employee.total_employees
        self.first_name=first_name
        self.last_name=last_name
    
    def print_information(self):
        print(f"{self.employee_number}: {self.first_name} {self.last_name}")
class HourlyPaid(Employee):
    def __init__(self, first_name, last_name, hourly_paid):
        super().__init__(first_name, last_name)
        self.hourly_paid=hourly_paid
        
    def print_information(self):
        super().print_information()
        print(f" Hourly pay: {self.hourly_paid}")
        
class MonthlyPaid(Employee):
    def __init__(self, first_name, last_name, monthly_paid):
        super().__init__(first_name, last_name)
        self.monthly_paid=monthly_paid
    
    def print_information(self):
        super().print_information()
        print(f" Monthly pay: {self.monthly_paid}")
        
employees=[]
employees.append(Employee("santosh", "Nepali"))
employees.append(Employee("Parbati", "Joshi"))
employees.append(HourlyPaid("Paru", "Joshi", 12.45))
employees.append(MonthlyPaid("Ram", "karki", 2250))

for employee in employees:
    employee.print_information()