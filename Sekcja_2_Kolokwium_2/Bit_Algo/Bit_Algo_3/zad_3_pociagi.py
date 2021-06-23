from queue import PriorityQueue


class Train:
    def __init__(self, arr, dep):
        self.arr = arr
        self.dep = dep

    # Funkcje porównawcze dla priority queue. Zmienne mogą być identyczne jak u innych bo pycharm je sugeruje (⌐■_■)
    def __gt__(self, other):
        return self.dep > other.dep

    def __lt__(self, other):
        return self.dep < other.dep


trains = [(1, 2), (1, 3), (1, 4), (2, 3), (4, 5), (4, 6), (6, 8), (9, 10)]
stations = 3
train_heap = PriorityQueue()
for i in range(stations):
    train_heap.put(Train(-1, -1))
for i in range(len(trains)):
    trains[i] = Train(trains[i][0], trains[i][1])

for train in trains:
    tmp = train_heap.get()
    if tmp.dep >= train.arr:
        train_heap.put(tmp)
    train_heap.put(train)
    if train_heap.qsize() > stations:
        print("False!")
        exit()
print("True!")
