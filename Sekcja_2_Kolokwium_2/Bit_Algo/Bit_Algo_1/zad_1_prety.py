def slice(prices, n):
    # Podział na 2 kawałki to 3 [0,1,2]
    n = n + 1
    slice_price = [-1] * n
    slice_price[0] = prices[0]
    slice_price[1] = prices[1]
    for dlugosc in range(2, n):
        slice_price[dlugosc] = prices[dlugosc]
        for odcinany in range(1, dlugosc):
            do_pociecia = dlugosc-odcinany
            if slice_price[dlugosc] < slice_price[do_pociecia] + prices[odcinany]:
                slice_price[dlugosc] = slice_price[do_pociecia] + prices[odcinany]
    print(slice_price)


prices = [0, 5, 8, 9, 10]
slice(prices, 2)
