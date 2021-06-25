A = [6, 5, 6, 10, 3, 6, 100]


def ferry(cars, length):
    def ferry_recur(i, l, r):
        if F[i][l][r] != -1:
            return F[i][l][r]
        when_left, when_right = 0, 0
        if i < n and l + cars[i] <= length:
            when_left = ferry_recur(i + 1, l + cars[i], r)
            when_left += 1
        if i < n and r + cars[i] <= length:
            when_right = ferry_recur(i + 1, l, r + cars[i])
            when_right += 1
        F[i][l][r] = max(when_left, when_right)
        return max(when_left, when_right)
    def get_res(car_cnt, fits, l, r):
        if fits == 0:
            return
        if l+cars[car_cnt] <= length and F[car_cnt+1][l+cars[car_cnt]][r] == fits - 1:
            print("Auto {} w lewo".format(car_cnt))
            get_res(car_cnt+1, fits-1, l+cars[car_cnt], r)
        elif r+cars[car_cnt] <= length and F[car_cnt+1][l][r+cars[car_cnt]] == fits - 1:
            print("Auto {} w prawo".format(car_cnt))
            get_res(car_cnt + 1, fits - 1, l, r+cars[car_cnt])
        else:
            print("Coś nie tak")
    n = len(cars)
    F = [[[-1 for _ in range(length + 1)] for _ in range(length + 1)] for _ in range(n)]
    res = ferry_recur(0, 0, 0)
    get_res(0, res, 0, 0)
    for line in F:
        print(line)

ferry(A, 15)
