from datetime import datetime

current_date = datetime.now().date()
class Company:
    def __init__(self, company_title: str, founders: list):
        self.company_title = company_title
        self.founders = founders
        self.creation_time = current_date
    
    def Add_employee(self) -> None:
        """Adding employee to the Company"""
        pass
    
    
    def List_employees(self) -> list:
        """Returns a List of employees in Company"""
        pass
    
    
    def Roadmap(self) -> str:
        """Returns a Company Roadmap"""
        pass
    
    
    def Company_achievements(self) -> list:
        """Describing company_achievements"""
        pass
    
    
    def Promote_employee(self) -> None:
        """Promotes employee"""
        pass
    
    
    def Demote_employee(self) -> None:
        """Demotes employee"""
        pass
    
    
    def Update_employee_info(self) -> None:
        """Updates employee info. E.g salary, position"""
        pass
    
    
    def Find_employee(self) -> str:
        """Finds employee in Company"""
        pass
    
    
    def Create_department(self) -> None:
        """Creates department in Company"""
        pass
    
    
    def Transfer_employee(self) -> None:
        """Changes employee department"""
        pass
    
    
    def List_department(self) -> list:
        """Returns list of departments in Company"""
        pass
    
    
    
        
    
    
    
        
        