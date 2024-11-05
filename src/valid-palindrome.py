class Solution:
    def isPalindrome(self, s: str) -> bool:
        valid = []

        for c in s:
            if c.isalnum():
                valid.append(c)

        return valid.__str__().lower() == valid[::-1].__str__().lower()