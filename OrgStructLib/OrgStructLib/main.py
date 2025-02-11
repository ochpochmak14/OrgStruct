from datetime import datetime

current_date = datetime.now().date()
class Company:
    def __init__(self, company_title: str, founders: list):
        """Data about initialized Company
        Args:
        company_title,
        founders,
        creation_time"""
        self.company_title = company_title
        self.founders = founders
        self.creation_time = current_date
    
    
    
    
        
    
    
    
        
        