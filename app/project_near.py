class Project:
    def __init__(self, type_project, size_project, company, dates, value, location, street, street_number):
        self.value = float(value)
        self.dates = int(dates)
        self.company = company
        self.size_project = int(size_project)
        self.type_project = type_project
        self.location = location
        self.street = street
        self.street_number = int(street_number)

    def __str__(self):
        return f"{self.type_project} {self.size_project} {self.company} {self.dates} {self.value} {self.location}" \
               f" {self.street} {self.street_number}"
    def __repr__(self):
        return self.__str__()

class ProjectList:
    def __init__(self):
        self.inventory1 = []

    def add_project(self, project1):
        self.inventory1.append(project1)
