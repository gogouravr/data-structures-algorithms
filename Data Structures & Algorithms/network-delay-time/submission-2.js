class Solution {
    /**
     * @param {number[][]} times
     * @param {number} n
     * @param {number} k
     * @return {number}
     */
    networkDelayTime(times, n, k) {    
        const dp = new Map()
        const graph = []
        const costToReach = []

        for(let i=0;i<n; i++){
            graph.push([])
            costToReach.push(Number.MAX_SAFE_INTEGER)
        }

        times.forEach(([u,v,t])=>{
            graph[u-1].push([v-1,t])
        })


        function dfs(u,dis, rs){
            rs.add(u)
            costToReach[u] = Math.min(costToReach[u],dis)

            for(const [v,t] of graph[u]){
                if(!rs.has(v) && costToReach[v] > dis + t){
                    dfs(v, t+dis, rs)
                }
            }

            rs.delete(u)
        }

        dfs(k-1,0, new Set())
        console.log(costToReach)
        return costToReach.some(e => e === Number.MAX_SAFE_INTEGER) ? -1 : Math.max(...costToReach)
    }
}
