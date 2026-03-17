class Solution:
    def watchedVideosByFriends(self, watchedVideos: List[List[str]], friends: List[List[int]], id: int, level: int) -> List[str]:
        visited = [False] * len(friends)
        visited[id] = True
        queue = collections.deque([(id, level)])

        res = []
        while queue:
            idx, depth = queue.popleft()

            if depth == 0:
                res.append(idx)
                continue

            for v in friends[idx]:
                if not visited[v]:
                    visited[v] = True
                    queue.append((v, depth-1))

        cnts = Counter()
        for t in res:
            for video in watchedVideos[t]:
                cnts[video] += 1
        sortedList = sorted(cnts.items(), key=lambda x: (x[1], x[0]))

        return [item[0] for item in sortedList]