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


    def select_project(self):
        self.read_input()

        # ingredients = []
        # for x in self.likes.most_common():
        #     if self.likes[x[0]] > self.dislikes[x[0]]:
        #         ingredients.append(x[0])
        # # ingredients.sort()
        self.output(["Logging", "WebChat"], [["Anna", "Bob"], ["Maria","Anna"]])


if __name__ == '__main__':
    # for x in ['a_an_example.in', 'b_basic.in', 'c_coarse.in', 'd_difficult.in', 'e_elaborate.in']:
    for x in ['a_an_example.in']:
        Teamwork(x).select_project()
