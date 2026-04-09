class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter

        c = Counter(nums)

        items = [key for key in c.keys()]

        items.sort(key=lambda t : c[t])
        print(items)

        return items[-1:-k-1:-1]


            