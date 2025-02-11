class EmployeeManagement:
    ID = 0

    def __init__(self):
        self.employees = []

    def add_employee(
        self, name: str, age: int, salary: int, department: str, position: str
    ) -> None:
        EmployeeManagement.ID += 1
        employee = {
            "id": EmployeeManagement.ID,
            "name": name,
            "age": age,
            "salary": salary,
            "department": department,
            "position": position,
        }
        self.employees.append(employee)

    def list_employees(self) -> list:
        return self.employees

    def find_employee(self, **kwargs) -> list:
        return [
            emp
            for emp in self.employees
            if all(emp.get(key) == value for key, value in kwargs.items())
        ]

    def update_employee_info(self, employee_id: int, new_info: dict) -> bool:
        for employee in self.employees:
            if employee["id"] == employee_id:
                employee.update(new_info)
                return True
        return False

    def change_position(self, employee_id: int, new_position: str) -> bool:
        for employee in self.employees:
            if employee["id"] == employee_id:
                employee["position"] = new_position
                return True
        return False

    def transfer_employee(self, employee_id: int, new_department: str) -> bool:
        for employee in self.employees:
            if employee["id"] == employee_id:
                employee["department"] = new_department
                return True
        return False
