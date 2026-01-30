class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        suma = sum(aliceSizes)
        sumb = sum(bobSizes)
        sumt = (suma + sumb) / 2

        seen = set(bobSizes)

        for i in aliceSizes:
            res = sumt - suma + i
            if res in seen:
                return [i, res]
        return -1
