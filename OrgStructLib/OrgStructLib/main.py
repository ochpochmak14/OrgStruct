from datetime import datetime

current_date = datetime.now().date()
class Company:
    def __init__(self, company_title: str, founders: list):
        self.company_title = company_title
        self.founders = founders
        self.creation_time = current_date
    
    
    
    
    def Roadmap(self) -> str:
        """Returns a Company Roadmap"""
        pass
    
    
    def Company_achievements(self) -> list:
        """Describing company_achievements"""
        pass
    
    
    def Create_department(self) -> None:
        """Creates department in Company"""
        pass
    
    def List_department(self) -> list:
        """Returns list of departments in Company"""
        pass
    
    
    
        
    
    
    
        
        