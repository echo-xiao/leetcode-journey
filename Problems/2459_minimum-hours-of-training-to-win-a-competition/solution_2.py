class Solution:
    def minNumberOfHours(self, initialEnergy: int, initialExperience: int, energy: List[int], experience: List[int]) -> int:
        currEnergy = initialEnergy
        resEn = 0
        for i in range(0, len(energy)):
            if currEnergy <= energy[i]:
                needed = energy[i] + 1 - currEnergy
                currEnergy += needed
                resEn += needed
            currEnergy -= energy[i]

        currExperience = initialExperience
        resEx = 0 
        for i in range(0, len(experience)):
            if currExperience <= experience[i]:                
                needed = experience[i] + 1 - currExperience
                currExperience += needed
                resEx += needed
            currExperience += experience[i]

        return resEn + resEx



