class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        window = len(s1)
        permutation = {}
        substring = {}

        for i in range(window):
            permutation[s1[i]] = permutation.get(s1[i], 0) + 1
        
        for i in range(len(s2)):
            print(s2[i])
            substring[s2[i]] = substring.get(s2[i], 0) + 1

            if i - window >= 0:
                substring[s2[i - window]] -= 1

                if substring[s2[i - window]] == 0:
                    del substring[s2[i - window]]

            if substring == permutation:
                return True
                
        return False