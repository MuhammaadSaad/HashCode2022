

from collections import Counter, defaultdict


class Teamwork:

    def __init__(self, file):
        self.totalProjects = None
        self.totalContributors = None
        self.contributors = []
        self.projects = []
                         
        self.filename = file

    def read_input(self):

        f = open('inputs/{}.txt'.format(self.filename), 'r')
        self.totalProjects, self.totalContributors = map(int, f.readline().strip().split(" "))


        for _ in range(0, self.totalContributors):

            contributor ={}
            skills = []
            contributor["name"], contributor["noSkills"] = f.readline().strip().split(" ")
            contributor["noSkills"] = int(contributor["noSkills"])
            for _ in range(contributor["noSkills"]):
                skill = {}
                skill["name"], skill["level"] = f.readline().strip().split(" ")
                skill["level"] = int(skill["level"])
                skills.append(skill)
            contributor["skills"] = skills
            self.contributors.append(contributor)

        for _ in range(0, self.totalProjects):
            projects = {}
            skills = []
            projects["name"], projects["complete"], projects["score"], projects["before"], projects["totalRoles"] = f.readline().strip().split(" ")
            projects["complete"] = int(projects["complete"])
            projects["score"] = int(projects["score"])
            projects["before"] = int(projects["before"])
            projects["totalRoles"] = int(projects["totalRoles"])
            for _ in range(0, projects["totalRoles"]):
                skill = {}
                skill["name"], skill["level"] = f.readline().strip().split(" ")
                skill["level"] = int(skill["level"])
                skills.append(skill)
            projects["skills"] = skills
            self.projects.append(projects)
        f.close()

    
    def output(self, projects, contributors):
        f = open('output/{}_output.txt'.format(self.filename), 'w')
        f.write(str(len(projects)))
        for idx, project in enumerate(projects):
            f.write("\n" + project + "\n")
            f.write(" ".join(contributors[idx]))
        f.close()



    def evaluateOutput(self):
#         self.contributors = [{'name': 'Anna', 'noSkills': 1, 'skills': [{'name': 'C++', 'level': 2}]}, {'name': 'Bob', 'noSkills': 2, 'skills': [{'name': 'HTML', 'level': 5}, {'name': 'CSS', 'level': 5}]}, {'name': 'Maria', 'noSkills': 1, 'skills': [{'name': 'Python', 'level': 3}]}]
#         self.projects = [{'name': 'Logging', 'complete': 5, 'score': 10, 'before': 5, 'totalRoles': 1, 'skills': [{'name': 'C++', 'level': 3}]}, {'name': 'WebServer', 'complete': 7, 'score': 10, 'before': 7, 'totalRoles': 2, 'skills': [{'name': 'HTML', 'level': 3}, {'name': 'C++', 'level': 2}]}, {'name': 'WebChat', 'complete': 10, 'score': 20, 'before': 20, 'totalRoles': 2, 'skills': [{'name': 'Python', 'level': 3}, {'name': 'HTML', 'level': 3}]}]
                     
        self.read_input()
        
        completedProjects = {"projects":[], "contributors":[]}
        for proj in self.projects:
            print(proj)
            for prjskill in proj.get("skills"):
                for cont in self.contributors:
                    for contskills in cont.get("skills"):
                        if prjskill.get("name") == contskills.get("name") and prjskill.get("level") <= contskills.get("level"):
                            if  cont.get("name") not in completedProjects.get("contributors") and proj.get("name") not in completedProjects.get("projects"):
                                completedProjects.get("contributors").append(cont.get("name"))
            completedProjects.get("projects").append(proj.get("name"))  
                                
                    
                
        print(completedProjects)           
        #self.output(completedProjects)


if __name__ == '__main__':
    for x in ['a_an_example.in']:#, 'b_basic.in', 'c_coarse.in', 'd_difficult.in', 'e_elaborate.in']:
        Teamwork(x).evaluateOutput()
