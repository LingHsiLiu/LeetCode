
#Definition for a point.
class Point:
    def __init__(self, a=0, b = 0):
        '''Defines x and y variables'''
        self.x = a
        self.y = b

import heapq

    # method1: use heapq's nsmallest function and lambda expression
# def kClosest(self, points, origin, k):
#     return heapq.nsmallest(k, points, key=lambda p: [(p.x-o.x)**2 + (p.y-o.y)**2, p.x])

# method2: use minheap
def kClosest(points, o, k):

    heap_dis, res, dis2points = [], [], {}
    # build dis2points map

    for p in points:
        d = (p.x-o.x)**2 + (p.y-o.y)**2
        if d not in dis2points:
            dis2points[d] = [p]
            heapq.heappush(heap_dis, d)
        else:
            dis2points[d].append(p)

    # find kth closest
    while len(res) < k:
        d = heapq.heappop(heap_dis)
        res += sorted(dis2points[d], key=lambda p: p.x)
        # if len(dis2points[d]) + len(res) <= k:
        #     # sort points by x, version1
        #     res += sorted(dis2points[d], key=lambda p: p.x)
        # else:
        #     # sort points by x, version2
        #     x_heap, x2point = [], {}
        #     print(dis2points[d])
        #     for p in dis2points[d]:
        #         print(p)
        #         x2point[p.x] = p
        #         heapq.heappush(x_heap, p.x)
        #     while len(res) < k:
        #         x = heapq.heappop(x_heap)
        #         res += [x2point[x]]
    return res


o = Point(0,0)
# print(o.x)
# points = [(9,6),(4,7),(4,4),(2,5),(1,1)]
#
a = Point(9,6)
b = Point(4,7)
c = Point(4,4)
d = Point(2,5)
e = Point(1,1)
f = Point(5,2)
points = [a,b,c,d,e,f]


k = 3
result = (kClosest(points, o, k))
for i in result:
    print(i.x, i.y)
# print(kClosest(points, o, k))
