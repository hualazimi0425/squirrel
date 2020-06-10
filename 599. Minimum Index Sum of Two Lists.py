# 1. put list1 items into a HashMap, item as index,
# index as value.
# 2. Scan list2 items, if find common item with list1
# compare sum of indexes with minIndex, if smaller,
# clear the stack and add new item into a stack.
# 3. if minIndex is equal current minIndex, just put item
# into stack.
import sys
from typing import List


def findRestaurant(list1: List[str], list2: List[str]) -> List[str]:
    map_list1 = {}
    stack = []
    n, m = len(list1), len(list2)
    min_index = sys.maxsize
    for i in range(n):
        map_list1[list1[i]] = i
    for j in range(m):
        if list2[j] in map_list1:
            if map_list1.get(list2[j]) + j < min_index:
                min_index = map_list1.get(list2[j]) + j
                stack.clear()
                stack.append(list2[j])
            elif map_list1.get(list2[j]) + j == min_index:
                stack.append(list2[j])
    res = [None] * len(stack)
    for i in range(len(stack)):
        res[i] = stack.pop()
    return res


print(findRestaurant(["Shogun", "Tapioca Express", "Burger King", "KFC"],
                     ["Piatti", "The Grill at Torrey Pines", "Hungry Hunter Steakhouse", "Shogun"]))
print(findRestaurant(["Shogun", "Tapioca Express", "Burger King", "KFC"],
["KFC", "Shogun", "Burger King"]))