class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = [[] for _ in range(n)]

        for s,d,p in flights:
            graph[s].append([d,p])
        
        vis = {}
        dp = {}
        def dfs(curr: int, t: int) -> int:
            if (curr,t) in dp:
                return dp[(curr,t)]
            if curr == dst:
                return 0

            vis[curr] = True
            res = 1e10

            for d,p in graph[curr]:
                if vis.get(d,False) == False and t > 0:
                    res =  min(p+dfs(d,t-1),res)
                    
            vis[curr] = False

            dp[(curr,t)] = int(res)
            return dp[(curr,t)]

        ans = dfs(src,k+1) 
        return ans if ans != int(1e10) else -1


