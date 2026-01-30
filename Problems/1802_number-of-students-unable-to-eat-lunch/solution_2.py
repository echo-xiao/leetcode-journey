from collections import deque


class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        
        queue = deque(students)
        stack = deque(sandwiches)
        attemps = 0

        while len(queue) > 0 and len(stack) > 0:
            if attemps == len(queue):
                break

            if stack[0] == queue[0]:
                queue.popleft()
                stack.popleft()
                attemps = 0
            else:
                queue.append(queue.popleft())
                attemps += 1
        return len(queue)
