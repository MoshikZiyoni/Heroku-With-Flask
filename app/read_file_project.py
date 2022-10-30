from app.project_near import Project, ProjectList

project_list = ProjectList()


def read_project():
    project_list = []
    with open("Project-file.csv") as project_file:
        project_file.readline()
        project_file1 = project_file.readlines()

        for i in project_file1:
            i = i.strip()
            temp = i.split(",")
            project = Project(temp[0], temp[1], temp[2], temp[3], temp[4], temp[5], temp[6], temp[7])
            project_list.append(project)

    for i in project_list:
        return project_list
