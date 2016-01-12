from typing import *

def selection_sort(a: list):
    for k, v in enumerate(a):
        # print(k, v)
        min_index = k
        for j in range(k, len(a)):
            # print(j, a[j])
            if a[j] < a[min_index]:
                min_index = j
        if min_index != k:
            a[k], a[min_index] = a[min_index], a[k]
        for z, vz in enumerate(a):
            print(z, vz)

if __name__ == '__main__':
    array = [1, 2, 34, 56, 12, -1]
    selection_sort(array)
    print(array)
