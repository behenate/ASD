def knapsack(price, weight, maxweight):
    max_price = sum(price)
    tab = [[0 for _ in range(max_price + 1)] for _ in range(len(price))]

    for i in range(price[0], 0, -1):
        tab[0][i] = weight[0]

    for i in range(price[0] + 1, max_price + 1):
        tab[0][i] = -1


    for i in range(1, len(price)):
        for pri in range(1, max_price + 1):
            if tab[i - 1][pri] != -1 and tab[i][pri - price[i]] != -1 and pri - price[i]:
                tab[i][pri] = tab[i - 1][pri]
                if price[i] <= pri:
                    tab[i][pri] = min(tab[i][pri], tab[i-1][pri - price[i]] + weight[i])
            else:
                if price[i] <= pri and tab[i][pri - price[i]] != -1:
                    tab[i][pri] = tab[i-1][pri - price[i]] + weight[i]
                else:
                    tab[i][pri] = -1

    for elem in tab:
        print(elem)

wagi =  [1,3,4]
rzeczy = [1,2,3]
print(knapsack(rzeczy, wagi, 15))