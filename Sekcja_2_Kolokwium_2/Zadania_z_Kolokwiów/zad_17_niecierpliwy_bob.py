from math import inf

def impatientBob(jobs, m):
    n = len(jobs)
    jobs = sorted(jobs, key=lambda x:x[1])
    F = [[inf for _ in range(n)] for _ in range(m)]
    for i in range(n):
        F[0][i] = 0
    for j in range(1, m):
        for i in range(n):
            for k in range(i-1, -1, -1):
                dist = jobs[i][0] - jobs[k][1]
                if dist < 0:
                    continue
                # Jeśli nie da się wykonać j-1 zadań dla k zbiorów to dla k-1 też sie nie będzie dało, można wyjść.
                if F[j-1][k] == inf:
                    break
                F[j][i] = min(F[j][i], F[j-1][k]+dist)
    for line in F:
        print(line)
    # for i in range(1, k):

_jobs = [(0, 3), (2, 4), (1, 4), (4, 7), (5, 9), (10, 12), (5, 11), (13, 14)]
impatientBob(_jobs, 3)
_jobs = A = [(0, 4), (2, 4), (1, 4), (4, 7)]
impatientBob(_jobs, 3)