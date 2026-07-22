# Create a class Employee with attributes name and company_name = "TechCorp".
# Add a class method change_company(cls, new_name) to update the company name for all employees.
# Demonstrate how this change affects all instances.
class Employee:
    company_name="TechCorp"
    def __init__(self,n):
        self.name=n
    @classmethod
    def change_company(cls,new_name):
        cls.company_name=new_name
e1=Employee("Idris")
print(e1.name)
print(e1.company_name)
e1.change_company("Google")
print(e1.name)
print(e1.company_name)