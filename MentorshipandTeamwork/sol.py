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
        cus = int(f.readline().split())

        for _ in range(0, cus):
            l = f.readline().strip().split(" ")
            d = f.readline().strip().split(" ")
            self.likes.update(list(l)[1:])
            self.dislikes.update(list(d)[1:])
        f.close()

    def output(self, ingredients):
        f = open('output/{}_output.txt'.format(self.filename), 'w')
        f.write(str(len(ingredients)))
        f.write(" ")
        f.write(" ".join(ingredients))
        f.close()


    def select_project(self):
        self.read_input()

        ingredients = []
        for x in self.likes.most_common():
            if self.likes[x[0]] > self.dislikes[x[0]]:
                ingredients.append(x[0])
        # ingredients.sort()
        # ingredients = ingredients[:5]
        self.output(ingredients)


if __name__ == '__main__':
    # for x in ['a_an_example.in', 'b_basic.in', 'c_coarse.in', 'd_difficult.in', 'e_elaborate.in']:
    for x in ['a_an_example.in']:
        Teamwork(x).top_5_ingredients()
