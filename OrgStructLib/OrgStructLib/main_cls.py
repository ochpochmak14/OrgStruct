from datetime import datetime
from Company_abilities import Company_abilities

current_date = datetime.now().date()


class Company(Company_abilities):
    def __init__(self, company_title: str, founders: list[str]):
        """Data about initialized Company
        Arguments:
            Company_title, Founders list of strings

        Return:
            None
            
        
        Extra Data: creation time
        """
        super().__init__()
        self.company_title = company_title
        self.founders = founders
        self.creation_time = current_date
