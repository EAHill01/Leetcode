#import re

#works, ~63% run, ~30% memory
class Solution:
    def isPalindrome(self, s: str) -> bool:
        #string = (re.sub(r'\W+', '', s)).lower() - doesn't work for removing _
        string = (''.join(filter(str.isalnum, s))).lower()
        if len(string)==0 or len(string)==1:
            return True
        for a, b in enumerate(string):
            if b != string[len(string)-a-1]:
                return False
            if len(string)/2 <= a:
                return True #means they've crossed over halfway
