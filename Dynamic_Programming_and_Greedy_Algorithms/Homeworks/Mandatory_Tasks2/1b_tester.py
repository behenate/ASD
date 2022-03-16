from basia_czolgista import tank
from zad_1_b_czolg import cheapest_path
from random import randint, seed
from time import time
passed = True
wojtek_saved = 0
seed(0)
passed_cnt = 0
failed_cnt = 0
for i in range(1000):
    stations = randint(5,8)
    s = [0 for _ in range(stations)]
    p = [0 for _ in range(stations)]
    l = randint(5,20)
    for j in range(stations):
        s[j] = s[j-1] + randint(1,l-1)
        p[j] = randint(1,4)

    w_s = time()
    wojtek = cheapest_path(s,p,l, s[-1])
    w_e = time()-w_s
    b_s = time()
    bogus = tank(s, p, l)
    b_e = time()-b_s
    wojtek_saved += b_e - w_e

    if wojtek != bogus:
        print("Different for: wojtek: {}, bogus: {}, l: {}".format(wojtek, bogus, l))
        print(s, p, l)
        failed_cnt += 1
        passed = False
    else:
        passed_cnt += 1
        print("Ok for: wojtek: {}, bogus: {}".format(wojtek, bogus))
print(wojtek_saved)
if passed:
    print("Passed!")
    print("Passed: {} out of {}".format(passed_cnt, passed_cnt+failed_cnt))
else:
    print("Failed!")
    print("Passed: {} out of {}".format(passed_cnt, passed_cnt + failed_cnt))