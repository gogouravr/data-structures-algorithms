from _heapq import heappop
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        import heapq

        a = [(-x,x) for x in nums]
        heapq.heapify(a)

        for i in range(k-1):
            heapq.heappop(a)

        return heapq.heappop(a)[1]
        
            
