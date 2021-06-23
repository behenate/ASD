class HuntingList:
    def __init__(self, predator=None, prey=None, next=None):
        self.next = next
        self.predator = None
        self.prey = None


def arr_to_huntlist(arr):
    n = len(arr)
    start = HuntingList()
    curr = start
    for i in range(n):
        curr.predator = arr[i][0]
        curr.prey = arr[i][1]
        curr.next = HuntingList()
        curr = curr.next
    return start


def release_them_all(hunting_list, n):
    to_calm = [0 for _ in range(n)]
    hunt_arr = [[0 for _ in range(n)] for _ in range(n)]
    hunt = hunting_list
    while hunt.next is not None:
        to_calm[hunt.predator] = 2
        hunt_arr[hunt.predator][hunt.prey] = 1
        hunt = hunt.next
    to_release = []
    for i in range(n):
        if to_calm[i] == 0:
            to_release.append(i)
    while len(to_release) > 0:
        r_i = to_release[-1]
        print(r_i)
        to_release.pop()
        for i in range(n):
            if hunt_arr[i][r_i] == 1:
                to_calm[i] -= 1
                if to_calm[i] == 0:
                    to_release.append(i)

who_hunts_who = [
    [1, 2],
    [1, 3],
    [1, 4],
    [1, 0],
    [1, 5],
    [2, 3],
    [2, 1],
    [3, 4],
    [3, 2],
    [4, 1],
    [4, 3],
    [2, 6],
    [4, 0]
]

_lst = arr_to_huntlist(who_hunts_who)
release_them_all(_lst, 7)