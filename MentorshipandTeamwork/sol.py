from collections import Counter, defaultdict


class Teamwork:

    def __init__(self, file):
        self.totalProjects = None
        self.totalContributors = None
        self.contributors = []
        self.projects = []
        self.filename = file
        self.selectedcontributor = []
        self.selectedProjects = []

    def read_input(self):
        '''
        Sample payload is this:


        Contributor:
        {   "name": "Anna",    
            "noSkills": 1, 
            "skills": [{"name": "C++", "level": 2}]
        }

        Project:
        {
            "name": "Logging",
            "complete": 5,
            "score": 10,
            "before": 5,
            "totalRoles": 1,
            "skills": [{"name": "C++", "level": 3}],
        },
        '''

        f = open('inputs/{}.txt'.format(self.filename), 'r')
        self.totalContributors, self.totalProjects = map(int, f.readline().strip().split(" "))
        for x in range(0, self.totalContributors):
            contributor =defaultdict()
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
            if x == self.totalContributors:
                import pdb; pdb.set_trace()
                break

        for _ in range(0, self.totalProjects):
            projects = defaultdict()
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
        print("writed"+self.filename)


    def select_contributor(self, skill, level,prjcontributor):
        '''
        return: name or False
        '''
        for contributor in self.contributors:
            for cskill in contributor["skills"]:
                if skill == cskill["name"] and cskill["level"] >= level and contributor["name"] not in prjcontributor:
                    return contributor["name"]
        return False


    def update_skill(self, name, skill, projLevel):
        for idc, contributor in enumerate(self.contributors):
            if contributor["name"] == name:
                for ids, cskill in enumerate(contributor["skills"]):
                    if cskill["name"] == skill:
                        if cskill["level"] > projLevel:
                            return True
                        else:
                            self.contributors[idc]["skills"][ids]["level"] = self.contributors[idc]["skills"][ids]["level"] +1
                            return True
        return False


    def select_project(self, project):
        contributor = []
        sk = [] # skill of the contributor
        level = [] # project skill level
        for skill in project['skills']:
            ans = self.select_contributor(skill["name"], skill["level"],contributor)
            if ans == False:
                return False
            else:
                contributor.append(ans)
                sk.append(skill["name"])
                level.append(skill["level"])

        self.selectedcontributor.append(contributor)
        for id, c in enumerate(contributor):
            self.update_skill(c, sk[id], level[id])
        return True


    def solution(self):
        self.read_input()
        contributors = []
        selectedProjects = []
        currProjects = [p["name"] for p in self.projects]

        # self.select_project(self.projects[1])
        while currProjects.__len__()>1: # added to complete all projects
            print(currProjects)
            print(self.contributors)
            for id, project in enumerate(currProjects):
                project = self.projects[id]
                if project['name'] in currProjects:
                    if self.select_project(project) == False:
                        continue
                    else:
                        selectedProjects.append(project["name"])
                        currProjects.remove(project["name"])

        self.selectedProjects = selectedProjects
        self.output(selectedProjects, self.selectedcontributor)

        # for project in currProjects:
        #     skipProj = False
        #     conProj = []
        #     for Pskill in project['skills']:
        #         import pdb; pdb.set_trace()
        #         sfound = False
        #         if skipProj==True:
        #             break
        #         for contributor in self.contributors:
        #             if sfound == True:
        #                 break
        #             if skipProj==True:
        #                 break
        #             for Cskill in contributor['skills']:
        #                 if Pskill['name'] == Cskill['name'] and Cskill['level'] >= Pskill['level']:
        #                     conProj.append(contributor['name'])
        #                     sfound = True
        #                 elif sfound == True:
        #                     break
        #                 else:
        #                     continue
        #             if sfound == False:
        #                 skipProj=True

        # selectedProjects= ["Logging", "WebApp"]
        # contributors = [["Anna", "Bob", "Cathy"], ["Bob", "Cathy", "Dave"]]
        #print(selectedProjects, self.selectedcontributor)


if __name__ == '__main__':
    # for x in ['a_an_example.in', 'b_basic.in', 'c_coarse.in', 'd_difficult.in', 'e_elaborate.in']:
    for x in ['b_better_start_small.in']:
    #for x in ['a_an_example.in']:
    #for x in [ 'a_an_example.in','b_better_start_small.in', 'c_collaboration.in', 'd_dense_schedule.in','e_exceptional_skills.in', 'f_find_great_mentors.in']:
        Teamwork(x).solution()






# projects = [logign, webchat]



# def select_contributor(skill, level):
#     for contributor in self.contributors:
#         for cskill in contributor["skills"]:
#             if skill == cskill["name"] and cskill["level"] >= level:
#                 return contributor["name"]
# 	return False


# def update_skill(name, skill, projLevel):
#     increse contributor skill by 1
	
	


# def select_project(project_name):
#     contributor = []
# 	for skill in project["skill"]:
#         select_contributor(skill, level)
# 		contributor.append(ans)
# 	if ans == False:
# 		return False
#     for c in contributor:
#     update_skill(name, skill, projLevel)




# def total_project():
#     proj = ["logging", "webchat"]
#     select_project =[]
#     for p in proj:
#         ans = select_project(p)
#         if ans == False:
#             print(p)
#         select_project.append(p)
