from collections import Counter, defaultdict


class OnePizza:

    def __init__(self, file):
        self.cus = None
        self.likes = Counter()
        self.dislikes = Counter()
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

    def output(self, ingredients):
        f = open('output/{}_output.txt'.format(self.filename), 'w')
        f.write(str(len(ingredients)))
        f.write(" ")
        f.write(" ".join(ingredients))
        f.close()


    def top_5_ingredients(self):
        self.read_input()

        ingredients = []
        for x in self.likes.most_common():
            if self.likes[x[0]] > self.dislikes[x[0]]:
                ingredients.append(x[0])
        # ingredients.sort()
        # ingredients = ingredients[:5]
        self.output(ingredients)


if __name__ == '__main__':
    for x in ['a_an_example.in', 'b_basic.in', 'c_coarse.in', 'd_difficult.in', 'e_elaborate.in']:
        OnePizza(x).top_5_ingredients()
