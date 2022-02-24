

from calendar import c
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
        self.totalContributors,self.totalProjects = map(int, f.readline().strip().split(" "))

        print(self.totalProjects, self.totalContributors)
        for i in range(0, self.totalContributors):
            contributor ={}
            skills = []
            line=f.readline().strip()
            contributor["name"], contributor["noSkills"] = line.split(" ")
            contributor["noSkills"] = int(contributor["noSkills"])
           
            for j in range(contributor["noSkills"]):
                skill = {}
                sl=f.readline().strip()
                skill["name"], skill["level"] = sl.split(" ")
                skill["level"] = int(skill["level"])
                skills.append(skill)
            contributor["skills"] = skills
            contributor["free"] = True
            self.contributors.append(contributor)

        for k in range(0, self.totalProjects):
            projects = {}
            skills = []
            projects["name"], projects["complete"], projects["score"], projects["before"], projects["totalRoles"] = f.readline().strip().split(" ")
            projects["complete"] = int(projects["complete"])
            projects["score"] = int(projects["score"])
            projects["before"] = int(projects["before"])
            projects["totalRoles"] = int(projects["totalRoles"])
            for l in range(0, projects["totalRoles"]):
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

    def selectContributors(self,skill,level):
         contrib=[contributor for contributor in self.contributors if contributor.get("skills")[skill].get("level") >= level]
         if contrib:
             return contrib
         return False
    
    def select_project(self, project):
        
        contribs=self.selectContributors(project.get("skills")[0].get("name"), project.get("skills")[0].get("level"))
        if contribs:
            return contribs
        return False
    
    def evaluateOutput(self):
#         self.contributors = [{'name': 'Anna', 'noSkills': 1, 'skills': [{'name': 'C++', 'level': 2}]}, {'name': 'Bob', 'noSkills': 2, 'skills': [{'name': 'HTML', 'level': 5}, {'name': 'CSS', 'level': 5}]}, {'name': 'Maria', 'noSkills': 1, 'skills': [{'name': 'Python', 'level': 3}]}]
#         self.projects = [{'name': 'Logging', 'complete': 5, 'score': 10, 'before': 5, 'totalRoles': 1, 'skills': [{'name': 'C++', 'level': 3}]}, {'name': 'WebServer', 'complete': 7, 'score': 10, 'before': 7, 'totalRoles': 2, 'skills': [{'name': 'HTML', 'level': 3}, {'name': 'C++', 'level': 2}]}, {'name': 'WebChat', 'complete': 10, 'score': 20, 'before': 20, 'totalRoles': 2, 'skills': [{'name': 'Python', 'level': 3}, {'name': 'HTML', 'level': 3}]}]
                     
        self.read_input()
        
        completedProjects =[]
        
        prjcontributors=[]
        final=[]
        print(self.projects)
        
        for proj in self.projects:
            prjcontributors.clear()
            #print(proj)
            for prjskill in proj.get("skills"):
                for cont in self.contributors:
                    print(cont)
                    for contskills in cont.get("skills"):
                        if prjskill.get("name") == contskills.get("name") and prjskill.get("level") <= contskills.get("level"):
                            if  cont.get("name") not in completedProjects and proj.get("name") not in prjcontributors and cont.get("free"):
                                prjcontributors.append(cont.get("name"))
                                contskills["level"] = int(contskills.get("level") + 1)
                                contskills["free"] = False
                        
    
            completedProjects.append(proj.get("name"))  
            
                      
            #final.append(proj.get("name"))    
            final.append(prjcontributors)     
                    
        print(self.contributors)             
                        
        print(completedProjects,final)           
        self.output(completedProjects,final)


if __name__ == '__main__':
    for x in [ 'b_better_start_small.in', 'a_an_example.in','c_collaboration.in', 'd_dense_schedule.in','e_exceptional_skills', 'f_find_great_mentors.in']:
        Teamwork(x).evaluateOutput()
