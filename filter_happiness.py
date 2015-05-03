from sys import argv

HISTORY_LEN = 5
class HappinessFilter(object):
    def __init__(self):
        self.history = [0] * HISTORY_LEN

    def update(self, x):
        self.history = self.history[1:] + [x]
        mean = sum(self.history) / HISTORY_LEN
        return mean

logFilename = argv[1]

myFilter = HappinessFilter()
with open(logFilename) as f:
    for line in f:
        happiness = float(line.rstrip("\n"))
        filteredHappiness = myFilter.update(happiness)
        print(filteredHappiness)
