from Department_managment import DepartmentManagment


class Company_abilities(DepartmentManagment):
    def __init__(self):
        super().__init__()

    def get_company_roadmap(self, file_path: str) -> str:
        """Reads and returns the company roadmap from a file.

        Argument:
            file_path (str): Path to the roadmap file (e.g., 'file.txt')

        Returns:
            str: The content of the roadmap file as a string.
        """
        with open(file_path, "r", encoding="utf-8") as file:
            return file.read()

    def get_company_achievements(self, file_path: str) -> list:
        """Returns a list of company achievements from a file.
        Argument:
            file_path (str): Path to the achievements file (e.g., 'ach.txt')
        Returns:
            list: List of achievements (each line as a separate item)
        """
        with open(file_path, "r", encoding="utf-8") as file:
            return file.read().splitlines()
