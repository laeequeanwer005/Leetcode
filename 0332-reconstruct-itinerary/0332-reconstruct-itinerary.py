class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:

        graph = {}

        for frm, to in tickets:
            if frm not in graph:
                graph[frm] = []
            graph[frm].append(to)

        for airport in graph:
            graph[airport].sort(reverse=True)

        result = []

        def dfs(airport):
            while graph.get(airport):
                next_airport = graph[airport].pop()
                dfs(next_airport)

            result.append(airport)

        dfs("JFK")

        return result[::-1]