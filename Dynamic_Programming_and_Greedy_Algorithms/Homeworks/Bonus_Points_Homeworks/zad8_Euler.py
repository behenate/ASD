from copy import deepcopy

"""
Dany jest graf nieskierowany reprezentowany przez macierz sąsiedztwa G, w
której pole G[i][j] ma wartość True wtedy gdy istnieje krawędź między wierzchołkami i oraz j (wartość False oznacza brak krawędzi). Wierzchołkami są
liczby naturalne 0, 1, . . . , n − 1, gdzie n = len(G). Proszę zaimplementować
funkcję:
euler(G)
która sprawdza czy G posiada cykl Eulera i jeśli tak, to zwraca listę z kolejnymi
numerami wierzchołków na takim cyklu, a jeśli nie to zwraca None. Funkcja nie
powinna niszczyć macierzy G.
"""

# Wojciech Dróżdż
# Aby uniknąć niepotrzebnych sprawdzeń algorytm przerabia graf na postać listy sąsiedztwa.
# W trakcie działania iterowane są tylko krawędzie, które istniały przy stworzeniu grafu i sprawdzane, czy nadal
# istnieją, poprzez sprawdzenie grafu wejściowego ( to tam są usuwane te krawędzie),po zakończeniu działania algorytm
# przywraca Graf wejściowy do początkowego stanu, poprzez informacje o krawędziach zapisane w cyklu Eulera.
# Jeżeli cykl nie istnieje, algorytm nie uruchomi się, dzięki czemu nie dojdzie do modyfikacji grafu wejściowego


def integrity_check(G):
    def DFS_visit(G, i):
        visited[i] = True
        for neigh in G[i]:
            if not visited[neigh]:
                DFS_visit(G, neigh)

    n = len(G)
    visited = [False for _ in range(n)]
    visit_cnt = 0
    for i in range(n):
        if not visited[i]:
            visit_cnt += 1
            DFS_visit(G, i)
    return visit_cnt <= 1


# Z postaci macierzowej utwórz listę sąsiedztwa, w ten sposób nie będzie konieczne iterowanie po wszystkich
# Wierzchołkach w każdym wywołaniu DFS dla wierzchołka, co pozwala uniknąć wysokiej złożoności
def matrix_to_adj(matrix):
    n = len(matrix)
    adj_g = [[] for _ in range(n)]
    can_do = True
    for i in range(n):
        for j in range(i, n):
            if matrix[i][j]:
                adj_g[i].append(j)
                adj_g[j].append(i)
    # Używając nowo powstałej listy sprawdź czy cykl Eulera istnieje
    for i in range(n):
        o = len(adj_g[i])
        if o % 2 != 0:
            can_do = False
    # Sprawdź czy graf jest spójny. Niespójny graf nie może mieć cyklu eulera
    can_do = can_do and integrity_check(adj_g)
    return adj_g, can_do


def euler(G):
    def DFS_visit(G, n_g, i, parent):
        if parent != -1:
            G[parent][i] = 0
            G[i][parent] = 0
        stack.append(i)
        # Przejdź po każdej krawędzi wychodzącej z wierzchołka
        for k in range(len(n_g[i])):
            neigh = n_g[i][k]
            # Jeżeli krawędź nadal istnieje wywołaj dla niej DFS
            if G[i][neigh]:
                DFS_visit(G, n_g, neigh, i)
        cycle.append(stack.pop())

    n_g, can_do = matrix_to_adj(G)
    # Jeżeli z warunku koniecznego na istnienie cyklu eulera nie istnieje on, zwróć None
    if not can_do:
        return None
    stack = []
    cycle = []
    # Wywołaj z dowolnego wierzchołka. (Zał: podany graf jest spójny)
    DFS_visit(G, n_g, 0, -1)
    # Na podstawie ścieżki odtwórz graf to stanu początkowego
    for i in range(len(cycle) - 1):
        G[cycle[i]][cycle[i + 1]] = 1
        G[cycle[i + 1]][cycle[i]] = 1
    return cycle
  
  
  
  
  
### sprawdzenie czy dla grafu G (o ktorym zakladamy, ze ma cykl Eulera
### funkcja zwraca prawidłowy wynik
  
  
G = [[0,1,1,0,0,0],
     [1,0,1,1,0,1],
     [1,1,0,0,1,1],
     [0,1,0,0,0,1],
     [0,0,1,0,0,1],
     [0,1,1,1,1,0]]

GG = deepcopy( G )
cycle = euler( G )

if cycle == None: 
  print("Błąd (1)!")
  exit(0)

u = cycle[0]
for v in cycle[1:]:
  if GG[u][v] == False:
    print("Błąd (2)!")
    exit(0)
  GG[u][v] = False
  GG[v][u] = False
  u = v
  
for i in range(len(GG)):
  for j in range(len(GG)):
    if GG[i][j] == True:
      print("Błąd (3)!")
      exit(0)
      
print("OK")
