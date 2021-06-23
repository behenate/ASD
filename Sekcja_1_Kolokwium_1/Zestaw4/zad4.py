from random import randint, seed

def do_test(arr):
    test_num = 1
    print("Allocating arr")
    unique_arr = [0]*(10**9)

    for to_test in arr:
        ctr = 0
        for number in to_test:
            if unique_arr[number] != test_num:
                ctr += 1
            unique_arr[number] = test_num
        print(ctr)
n = 10
seed("Dasia Boncer")
to_test = [[randint(0,10**9-1) for _ in range(randint(5,9))] for _ in range(n)]
do_test(to_test)
print(to_test)

