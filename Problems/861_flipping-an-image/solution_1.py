class Solution(object):
    def flipAndInvertImage(self, image):
        """
        :type image: List[List[int]]
        :rtype: List[List[int]]
        """
        
        
        for i in range(0, len(image)):
            left = 0
            right = len(image)-1
            while left < right:
                image[i][left], image[i][right] = image[i][right], image[i][left]
                left += 1
                right -= 1

        for i in range(0, len(image)):
            for j in range(0, len(image)):
                if image[i][j] == 1:
                    image[i][j] = 0
                else:
                    image[i][j] = 1
        
        return image
            