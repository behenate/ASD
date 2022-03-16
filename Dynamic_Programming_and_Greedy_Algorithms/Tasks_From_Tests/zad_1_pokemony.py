"""
Student chce wypuścić n różnych pok´emonów (numerowanych od 0 do n − 1) z klatek
(pok´eball’i). Wypuszczony Pok´emon natychmiast atakuje swojego wybawiciela, chyba że (a) jest
spokojny, lub (b) w okolicy znajdują się co najmniej dwa uwolnione pok´emony, na które ten
pok´emon poluje. Proszę zaimplementować funkcję:
int* releaseThemAll( HuntingList* list, int n ),
gdzie list to lista z informacją, które pok´emony polują na które (lista nie zawiera powtórzeń):
struct HuntingList {
HuntingList* next; // następny element listy
int predator; // numer pokemona, który poluje
int prey; } // numer pokemona, na którego poluje
Funkcja powinna zwrócić n elementową tablicę z numerami pok´emonów w kolejności
wypuszczania (tak, żeby wypuszczający nie został zaatakowany) lub NULL jeśli taka kolejność nie
istnieje. Każdy wypuszczony pok´emon zostaje ”w okolicy”. Jeśli pok´emon nie występuje na liście
jako predator to znaczy, że jest spokojny. Zaimplementowana funkcja powinna być możliwie jak
najszybsza. Proszę krótko oszacować jej złożoność.

"""
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
