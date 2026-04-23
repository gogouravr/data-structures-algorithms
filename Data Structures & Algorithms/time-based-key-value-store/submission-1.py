class TimeMap:

    def __init__(self):
        self.store =  {}  #\\replace# key: key , value = {list, dict}


        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = [[],{}]

        self.store[key][0].append(timestamp)
        self.store[key][1][timestamp] = value
        

    def get(self, key: str, ts: int) -> str:
        # binary search, next greated timestamp
        if key not in self.store:
            return ""

        tms = self.store[key][0]

        l = 0
        r = len(tms)-1
        ans = None

        while l <= r:
            m = l + (r-l)//2
            if tms[m] == ts:
                ans = tms[m]
                break

            if tms[m] < ts:
                ans = tms[m]
                l = m + 1
            else:
                r = m - 1 



        return self.store[key][1][ans] if ans is not None else ""
        
