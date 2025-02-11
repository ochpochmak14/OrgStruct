from Employee_managment import EmployeeManagement


class DepartmentManagment(EmployeeManagement):
    Department_id = 0

    def __init__(self):
        
        super().__init__()
        self.department_list = []

    def Create_department(self, department_name: str) -> None:
        """Creates department in Company
        Arguments:
            depratment name
        
        Return:
            None
        
        """
        DepartmentManagment.Department_id += 1
        Department = {
            "id": DepartmentManagment.Department_id,
            "title": department_name,
            "employees": [],
        }
        self.department_list.append(Department)

    def List_department(self) -> list:
        """Returns list of departments in Company"""
        return self.department_list
