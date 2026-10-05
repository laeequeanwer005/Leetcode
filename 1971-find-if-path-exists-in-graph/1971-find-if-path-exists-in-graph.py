class Solution:
    def validPath(self, n, edges, source, destination):

        graph = [[] for _ in range(n)]

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        queue = [source]
        visited = {source}
        front = 0

        while front < len(queue):

            node = queue[front]
            front += 1

            if node == destination:
                return True

            for neighbor in graph[node]:

                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

        return False