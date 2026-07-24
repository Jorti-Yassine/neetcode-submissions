class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Mastering the two pointers approach
        s="".join([e.lower() if e.isalnum() else "" for e in s ])
        l,r = 0, len(s)-1
        while l<r:
            if s[l]!=s[r]:
                return False
            l+=1
            r-=1
        return True