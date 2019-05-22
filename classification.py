class Classified(object):
    def __init__(self):
        self.scores = []

    def add_score(self, item):
        self.scores.append(item)

    def classify(self):
        scores = 0
        if len(self.scores) > 0:
            for score in self.scores:
                if score == "A":
                    scores += 100
                if score == "B":
                    scores += 80
                if score == "C":
                    scores += 60
                if score == "D":
                    scores += 40
                if score == "F":
                    scores += 20
                else:
                    scores += 0

            return scores


me = Classified()
me.add_score("B")
me.add_score("A")
me.add_score("D")

print(me.classify())