

from collections import Counter, defaultdict


class Teamwork:

    def __init__(self, file):
        self.totalProjects = None
        self.totalContributors = None
        self.contributors = []
        self.projects = []
                         
        self.filename = file

    def read_input(self):

        f = open('input/{}.txt'.format(self.filename), 'r')
        cus = int(f.readline())

        for _ in range(0, cus):
            l = f.readline().strip().split(" ")
            d = f.readline().strip().split(" ")
            self.likes.update(list(l)[1:])
            self.dislikes.update(list(d)[1:])
        f.close()

    def output(self, completedProjects):
        f = open('output/{}_output.txt'.format(self.filename), 'w')
        f.write(str(len(completedProjects)))
        f.write(" ")
        f.write(" ".join(completedProjects))
        f.close()


    def evaluateOutput(self):
        self.contributors = [{ "name": "anna", "noSkills": 1, "skills": [{"name": "c++", "level": 1}]},
  { "name": "bob", "noskills": 2, "skills": [{"name": "c++", "level": 1}, {"name": "html", "level": 5}]},
  {"name": "Maria", "noskills": 1, "skills": [{"name": "Python", "level": 3}]}]
        self.projects = [{"name": "logging", "complete": 5, "score": 10, "before":5, "TotalRoles": 1, "Roles": [{"name": "c++", "level": 3}]},
                         { "name": "WebServer", "complete": 7, "score": 10, "before": 7, "TotalRoles": 2, "Roles": [{"name": "c++", "level": 2}, {"name": "html", "level": 3}]},
                         {"name": "WebChat", "complete": 10, "score": 20, "before": 20, "TotalRoles": 2, "Roles": [{"name": "python", "level": 2}, {"name": "html", "level": 3}]}]
                     
        #self.read_input()

        completedProjects = []
        for x in self.projects.():
            if self.likes[x[0]] > self.dislikes[x[0]]:
                completedProjects.append(x[0])
        # ingredients.sort()
        # ingredients = ingredients[:5]
        self.output(completedProjects)


if __name__ == '__main__':
    for x in ['a_an_example.in', 'b_basic.in', 'c_coarse.in', 'd_difficult.in', 'e_elaborate.in']:
        Teamwork(x).evaluateOutput()
