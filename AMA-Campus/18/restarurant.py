##與 customer 最近的距離
class Solution:
    """
    @param restaurant: 
    @param n: 
    @return: nothing
    """
    def distance(self,x,y):
        return x**2 + y**2 
    def nearestRestaurant(self, restaurant, n):
        # Write your code here
        if len(restaurant) == 0 or len(restaurant) < n:
            return []
        import heapq 
        order = []
        result = []
        res = []
        for i , (x,y) in enumerate(restaurant):
           heapq.heappush(order,(self.distance(x,y),i,[x,y]))
       
        for i in range(n):
            heapq.heappush(result,(heapq.heappop(order)[1:]))
      
        for i in range(n):
            res.append(heapq.heappop(result)[1])

        return res
