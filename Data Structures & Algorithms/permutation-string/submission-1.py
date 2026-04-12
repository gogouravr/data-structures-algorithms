class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False

        from collections import Counter

        c1 = Counter(s1)
        c2 = Counter(s2[:len(s1)])

        for i in range(len(s2)-len(s1)+1):
            # print(i,len(s1),sorted(s2[i:i+len(s1)]) , sorted(s1))
            # if sorted(s2[i:i+len(s1)]) == sorted(s1):
                # return True

            print(i,c1,c2)

            if c1 == c2:
                return True
            
            if c2.get(s2[i]) == 1:
                c2.pop(s2[i])
            else:
                c2[s2[i]] -= 1

            if i  < len(s2)-len(s1):
                c2[s2[i+len(s1)]] = c2.get(s2[i+len(s1)],0) + 1
            

        return False
    