"""
Jest super okrąg super punkty i generalnie jest super.
"""
from random import randint, seed
from math import sqrt, pi, floor


def find_max_point(arr):
    max_dist = 0
    for point in arr:
        dist = sqrt(point[0]**2 + point[1]**2)
        max_dist = max(dist, max_dist)
    return max_dist


def area(point):
    return  (sqrt(point[0] ** 2 + point[1] ** 2))**2*pi


def radius(point):
    return sqrt(point[0] ** 2 + point[1] ** 2)


def insertion_sort(tab):
    for j in range(1, len(tab)):
        key = tab[j]
        i = j-1
        while i >= 0 and radius(tab[i]) > radius(key):
            tab[i+1] = tab[i]
            i -= 1
        tab[i+1] = key

def bucket_points(arr):
    n = len(arr)
    max_r = find_max_point(arr)
    target_area = (pi*(max_r**2)) + 1
    buckets = [[] for _ in range(n)]
    for i in range(n):
        point_area = area(arr[i])
        buckets[floor((point_area/target_area)*n)].append(arr[i])
    for bucket in buckets:
        insertion_sort(bucket)
    n =0
    for bucket in buckets:
        for point in bucket:
            arr[n] = point
            n += 1


m_r = 10
n = 20
seed(45)
points = [[randint(-m_r, m_r) for _ in range(2)] for _ in range(n)]
print("Sorting!")
bucket_points(points)
print(points)