#worked, learned from other peoples solutions, ~72% run and ~ 71% mem
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s)==Counter(t)

#worked, original answer, ~37% run and ~18% mem
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        if sorted(s) == sorted(t):
            return True
        return False
        
