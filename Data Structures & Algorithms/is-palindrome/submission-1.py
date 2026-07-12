class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = re.sub(r"[?:;.,&!\'\"\s+]", "", s).lower()
        print(cleaned)
        return cleaned[::-1]==cleaned