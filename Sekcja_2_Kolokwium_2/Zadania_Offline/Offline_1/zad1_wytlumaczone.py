from copy import copy
from time import time

"""Życzę miłego czytania mojego marnego wytłumaczenia :)))) Zacznij od tego kloca na samym dole"""


def reverse_arr(arr):
    i = 0
    j = len(arr) - 1
    while j - i > 0:
        arr[i], arr[j] = arr[j], arr[i]
        i += 1
        j -= 1


# Longest decreasing subsequence
def lds(arr):
    n = len(arr)
    lengths = [1] * n
    extends = [[] for _ in range(n)]
    max_length = 0
    # Tak właściwie to jest to standardowa funkcja LIS tylko tam jakieś minimalne zmiany na to żeby był malejący
    # Na luzie napiszesz własną
    for i in range(1, n):
        local_max_length = 1
        """
            Ważne! tutaj cofamy się od aktualnego indexu bo jeżeli tak zrobimy to zawsze w tablicy rozszerzeń
            gdy zajdzie sytuacja gdzie są rozgałęzienia na kilka możliwości zbudowania najdłuższego podciągu to indexy 
            wpiszą się w malejącej kolejności. np. extends = [[],[],[], [2,1], [3]] to jest przydatne w rekurencji i 
            tam wyjaśnię dlaczego.                                        ^tu rozgałęzienie
        """
        for j in range(i - 1, -1, -1):
            # Jeśli długość jest większa wyczyść extends na j i wstaw nowe, prawidłowe przedłużenie
            if arr[j] > arr[i] and lengths[j] + 1 > local_max_length:
                local_max_length = lengths[j] + 1
                # Jeżeli ta maksymalna lokalna długość jest większa od tej głównej to ją zastąp
                max_length = max(max_length, local_max_length)
                extends[i] = [j]
            # Jeśli długość  jest równa aktualnej maksymalnej to jest kilka potencjalnie najdłuższych podciągów
            elif arr[j] > arr[i] and lengths[j] + 1 == local_max_length:
                extends[i].append(j)
            lengths[i] = local_max_length

    # Rekurencja zwróci nam ile podciągów zbudowało z każdego końca więc musimy je zsumować do total.
    total = 0
    print(arr)
    print(lengths)
    print(extends)
    """
        Idziemy po długości tablicy od końca żeby zacząć wypisywanie od elementu co jest najbliższy początku w tablicy
        nieodwróconej tak jak w tym głównym klocu pisałem.
    """
    for i in range(n - 1, -1, -1):
        if lengths[i] == max_length:
            # Dajemy mu tablicę długości max_length, i będziemy ją wypełniać wgłąb rekurencji wartościami, na końcu
            # rekurencji każdy ciąg będzie i tak długości max_length więc na pewno ją wypełni.
            total += print_solution(arr, extends, i, [0] * max_length)
    return total


# Okazuje się że rekurencja jest dość krótka :)))

def print_solution(arr, extends, current_index, append_tab, tab_index=0):
    """
    Wow ale pycharm dodał automatycznie komentarz do parametrów to wykorzystam
    :param arr: Odrwócona tablica
    :param extends: Tablica rozszerzeń
    :param current_index: Aktualny index z którego chcemy iść głębiej w podciąg
    :param append_tab:  Tablica do której wpisujemy wartość z aktualnego indeksu
    :param tab_index: Informacja na który index w powyższej tablicy wpisać element
    """
    # Jeśli długość aktualnego w tablicy rozszerzeń to 0 to znaczy że jesteśmy na końcu rekurencji
    if len(extends[current_index]) == 0:
        # Przypisuje ostatnią wartość przed wypisaniem
        append_tab[tab_index] = arr[current_index]
        # Nie muszę jej odwracać bo rekurencja buduje od tyłu dodając na kolejne indexy więc odwraca za nas.
        # print żeby był dobry format do odp. dla Falisza
        for elem in append_tab:
            print(elem, end=" ")
        print("")
        # Zwraca wartość jeden no bo znalazło koniec jednego podciągu
        return 1

    # Licznik ilości końców podciągów które zostały znalezione
    cnt = 0
    """
        Tutaj idziemy po każdym elemencie z tablicy rozszerzeń pod aktualnym indexem. Jeżeli mamy np. [3,2]
        to najpierw podepnie do tablicy arr[3], wykona dla niej rekurencję, a potem podepnie arr[2] i wykona rekurencję.
        Dzięki temu na pewno będzie kolejność która zadowoli faliszewskiego. 
        No bo tak właściwie to budujemy tą tablicę do przodu więc wybierając najpierw większy index na pewno wybierzemy
        ten bliżej początku bo tablica jest odwrócona. Mówiąc do przodu mam na myśli patrząc w kontekście tablicy 
        nieodwróconej. 
        Ostatni w odwróconej -> pierwszy w nieodwróconej
        Dalej od początku w odwróconej -> Bliżej do początku w odwróconej
    """
    """
        Działa to mega sprytnie i też nie jest moim pomysłem. Mój był głupszy, janka był mądrzejszy od mojego ale też 
        głupszy a ten ktoś na grupie napisał i jest mega super, bo nie zżera pamięci zupełnie.
        Jak mamy tą tablicę długości max_len no to dostajemy w wywołaniu na który index w niej mamy wpisać wartość. 
        Dajmy że mamy już w append_tab wartości [1,2,3,0,0,0], wtedy tab_index = 3 a z tablicy extends mamy informację
        że rozszerzą ją jakieś dwa indeksy co mają wartości [5,4], gdzie arr[5]=4 arr[4]=5
        Wtedy rekurencja zrobi w append_tab [1,2,3,4,0,0] i odpali sobie dla niej rekurencję i ona sobie będzie szła dalej,
        dojdzie do końca no i wypisze jakieś tam dajmy [1,2,3,4,7,9] to juz nas nie obchodzi co wypisze w sumie.
        Wypisała to i wraca. Teraz nasza pętla przejdzie jeszcze raz i po prostu nadpisze w tej tablicy 4 na 5 
        (no bo rekurencja pamięta ten tab_index jaki kiedyś tam dostała) i zrobi [1,2,3,5,7,9] a dalej w tej rekurencji
        normalnie nadpiszą się te wartości pod 7 i 9 jakimiś innymi. To działa, bo wiemy że każda tablica co wypisujemy
        ma dokładnie taką samą długość więc zawsze do końca ponadpisuje na końcu rekurencji.
        Więc nie trzeba żadnych appendów ani kopii tablicy co jest bardzo spoko.
        
    """
    for i in range(len(extends[current_index])):
        append_tab[tab_index] = arr[current_index]
        cnt += print_solution(arr, extends, extends[current_index][i], append_tab, tab_index + 1)
    return cnt


def printAllLIS(A):
    # Wymówki na lenistwo dla Falisza
    """
    W celu utworzenia podciągów malejących można iść w funkcji od końca tablicy lub odwrócić ją przed wykonaniem
    funkcji. Jako że program ma złożoność n^2 (bez wypisywania) to złożoność odwrócenia (n/2) które wymaga tylko O(1)
    pamięci, ma pomijalny wpływ na czas działania programu i moim zdaniem jest dobrym poświęceniem za zwiększoną
    czytelność i intuicyjność kodu.
    """
    """
    Odwracam tablicę ale po co?
    Najpierw rozważmy jak jest nieodwrócona i szukałbym najdłuższego rosnącego:
    [3, 1, 5, 7, 2, 4, 3] <-- Tablica
    [1, 1, 2, 3, 2, 3, 3] <-- Długości podciągów
    [[], [], [1, 0], [2], [1], [4], [4]] <-- Tablica rozszerzeń
    
    Problem jest taki, że Falisz chce żeby ciągi leciały w kolejności takiej w jakiej są w wejściowej tablicy.
    Więc mamy indeks ostatniego elementu ciągu rosnącego i jak się wrócić z tego indeksu do początku podciągu,
    więc na spokojnie można zrobić rekurencję co to wyprintuje, ale problem jest taki że nie wiemy jaki jest 
    pierwszy element podciągu a to od niego (głównie, kolejne też mają wpływ ale to zobaczysz zaraz) zależy w jakiej
    kolejności wyprintujemy. 
    Jako że znamy tak właściwie tylko ostatni element podciągu to trochę przypał i średnio bez wywalenia złożoności w 
    kosmos i kodu na nie wiadomo ile linijek da się to wyprintować. 
    
    Ok to teraz coś na co wpadł ktoś mądrzejszy ode mnie:
    Odwracam tablicę i szukam najdłuższego malejącego podciągu (można też robić to bez odwrócenia, stąd moje tłumaczenie
    u góry ale to takie sranie z indexami że nie warto).
    To teraz dla tej samej tablicy wejściowej [3, 1, 5, 7, 2, 4, 3] wyjdzie:
    [3, 4, 2, 7, 5, 1, 3] <-- Tablica
    [1, 1, 2, 1, 2, 3, 3] <-- Długości podciągów
    [[], [], [1, 0], [], [3], [4, 2], [4]] <-- Tablica rozszerzeń
    
    Po co?
    Jak odwrócimy tablicę i znajdziemy w niej najdłuższy malejący podciąg to jeżeli odwrócimy ten podciąg to będzie
    to najdłuższy rosnący podciąg w tej normalnej, ale co najważniejsze jak mamy tą naszą funkcję "najdłuższy malejący
    podciąg(ldr)" to ona jest normalnie tą na najdłuższy z innym znakiem, więc w niej też mamy tylko informację o tym,
    który element kończy ten podciąg i jak wracać z niego. 
    Jeżeli pomyślimy o tej tej informacji w kontekście tablicy nieodwróconej to element kończący najdłuższy malejący
    podciąg w tablicy odwróconej jest elementem rozpoczynającym najdłuższy możliwy podciąg w tablicy nieodwróconej, .
    a tablica powrotów tak naprawdę jest tablicą jak budować ciąg od początku do końca a nie od końca do początku.
    
    Teraz gdy mamy naszą tablicę długości podciągów i tablicę jak je odtwarzać (one dalej są dla tej tablicy odwróconej
    tam u góry pisałem o tym że jak odwrócimy jeszce raz bla bla ale to tylko tak w ramach wyjaśnienia czemu tak się 
    dzieje) idąc od końca tablicy długości podciągów możemy znaleźć te indeksy gdzie kończą się te najdłuższe odwrócone
    podciągi malejące. Idziemy od końca, bo ostatni element w odwróconej jest pierwszy w nieodwróconej, więc jeśli 
    znajdziemy ten najbliżej końca tablicy długości to będzie on jednocześnie najwcześniejszym początkiem w rosnącym 
    podciągu w tablicy nieodwróconej. Dla niego wywołujemy print_solution i idziemy dalej pętlą i znajdujemy
    kolejny.
    
    Jejku strasznie to zagmatwane :(( Najważniejsze żeby wiedzieć że jak odwrócimy i znajdziemy ten podciąg to jego 
    ostatni element jest pierwszym elementem tego rosnącego. Na podstawie tego praktycznie całe rozwiązanie się 
    łatwo buduje jak sobie to rozrysujesz dla przykładu.
    
    Ja tu sobie rozrysowywałem i w sumie na samym dole zrobiłem przypadkiem całkiem fajne drzewko rekurencji.
    https://wbd.ms/share/v2/aHR0cHM6Ly93aGl0ZWJvYXJkLm1pY3Jvc29mdC5jb20vYXBpL3YxLjAvd2hpdGVib2FyZHMvcmVkZWVtL2FmMTMwYWFiYTcyMTQyOWRhNmZkYTAxYWU5Njg4N2YyXzgwYjEwMzNmLTIxZTAtNGE4Mi1iYmMwLWYwNWZkY2NkM2JjOA==
    """
    reverse_arr(A)
    return lds(A)


start = time()
_arr = [3, 1, 5, 7, 2, 4, 3]
# _arr = [10 * k + i for k in range(8) for i in range(6, 0, -1)]
print(printAllLIS(_arr))
print(time() - start)
