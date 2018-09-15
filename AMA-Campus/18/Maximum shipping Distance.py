def maxShipDist(list1, list2, maxDist):
    total_Dist = 0
    result =[]
    for item1 in list1:
        for item2 in list2:
            if len(item1) == 2 and len(item2) == 2:
                if item1[1] + item2[1] <= maxDist:
                    total_Dist = max(total_Dist, item1[1] + item2[1])
    for item1 in list1:
        for item2 in list2:
            if len(item1) == 2 and len(item2) == 2:
                if item1[1] + item2[1] == total_Dist:
                    result.append([item1[0], item2[0]])
    return result

list1 = [[1,3000], [2, 5000], [3, 7000], [4, 10000]]
list2 = [[1,2000], [2, 3000], [3, 4000], [4, 5000]]
maxDist = 10000
print(maxShipDist(list1, list2, maxDist))

