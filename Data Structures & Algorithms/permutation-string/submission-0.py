class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        # print(len(s2)-len(s1)+1)
        for i in range(len(s2)-len(s1)+1):
            # print(i,len(s1),sorted(s2[i:i+len(s1)]) , sorted(s1))
            if sorted(s2[i:i+len(s1)]) == sorted(s1):
                return True

        return False
    