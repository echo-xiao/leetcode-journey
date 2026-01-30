class Solution(object):
    def badSensor(self, sensor1, sensor2):
        """
        :type sensor1: List[int]
        :type sensor2: List[int]
        :rtype: int
        """
        i = 0
        n = len(sensor1)
        while i < n-1:
            if sensor1[i] != sensor2[i]:
                if sensor1[i+1:n] == sensor2[i:n-1] and sensor1[i:n-1] == sensor2[i+1:n]:
                    return -1
                elif sensor1[i+1:n] == sensor2[i:n-1]:
                    return 2
                elif sensor1[i:n-1] == sensor2[i+1:n]:
                    return 1
            i += 1
        return -1