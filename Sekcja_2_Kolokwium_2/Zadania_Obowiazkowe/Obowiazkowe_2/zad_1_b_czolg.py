from math import inf
def cheapest_path(s, p, l, target):
    n = len(s)
    pos = s[0]
    i = 0
    cost = 0
    fuel = l
    # Dojedź od startu do pierwszej stacji
    fuel -= s[0]
    if fuel < 0 or target - s[-1] > l:

        return False
    for k in range(n-1):
        if s[k+1] - s[k] > l:
            return False
    while pos != target:
        # Jeżeli starczy już paliwa  aby dojechać, to dojedź
        if pos + fuel >= target:
            break
        cheapest = i
        for j in range(i+1, n):
            if p[j] < p[cheapest] and s[j]-pos <= l:
                cheapest = j
                break
        if s[cheapest] == pos:
            # Dotankuj do pełna lub tyle aby dojechać do celu
            cost += min((target-pos-fuel)*p[i], (l-fuel) * p[i])
            fuel = l
            # Przejedź na następną stację i rozważ opcje
            fuel -= s[i+1] - pos
            i += 1
            pos = s[i]
        elif fuel < s[cheapest]-pos:
            cost += min((target-pos-fuel)*p[i], (s[cheapest]-pos-fuel) * p[i])
            # Dotankuj odpowiednią ilość
            fuel += s[cheapest]-pos-fuel
            # Dojedź do celu
            fuel -= s[cheapest] - s[i]
            i = cheapest
            pos = s[i]
        else:
            fuel -= s[cheapest] - pos
            i = cheapest
            pos = s[i]
    return cost

# _s = [2, 5, 10, 15]
# _p = [0.5, 2, 0.01, 4]
# _s = [3,6,7]
# _p = [3,2,1]
# _s = [4,6,9,14,16]
# _p = [2,1,1,3,1]


_s = [1, 2, 3, 4, 8, 11]
_p = [2, 4, 3, 3, 2, 4]
print(cheapest_path(_s, _p, 5, 12))