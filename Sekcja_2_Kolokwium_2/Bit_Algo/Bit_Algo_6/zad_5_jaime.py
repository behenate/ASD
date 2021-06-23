def assign_tasks(tasks):
    n = len(tasks)
    for i in range(n):
        tasks[i] = (tasks[i], i)

    tasks = sorted(tasks, key=lambda x:x[0])
    c_e = 0
    j_e = 0
    order = ["_" for _ in range(n)]
    for i in range(n):
        if tasks[i][0][0] >= c_e:
            c_e = tasks[i][0][1]
            order[tasks[i][1]] = "C"
        elif tasks[i][0][0] >= j_e:
            j_e = tasks[i][0][1]
            order[tasks[i][1]] = "J"
        else:
            print("IMPOSSIBLE ")
    print(order)


_tasks = [
    [99, 150],
    [1, 100],
    [100, 301],
    [2, 5],
    [150, 250]
]

assign_tasks(_tasks)


