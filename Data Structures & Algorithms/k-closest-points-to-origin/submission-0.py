class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        res = []
        for point in points:
            distance = (point[0] - 0)**2 + (point[1] - 0)**2
            point.insert(0,distance)
        heapq.heapify(points)
        while k > 0:
            smallest = heapq.heappop(points)
            del smallest[0]
            res.append(smallest)
            k -=1
        return res