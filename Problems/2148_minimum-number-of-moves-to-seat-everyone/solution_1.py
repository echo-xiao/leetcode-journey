class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        seats.sort()
        students.sort()
        res = 0

        for i in range(0, len(seats)):
            diff = abs(seats[i] - students[i])
            res += diff
        return res