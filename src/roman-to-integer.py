class Solution:
    def romanToInt(self, s: str) -> int:
        res = 0
        prev = 0
        translations = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        for symbol in s[::-1]:
            if translations[symbol] >= prev:
                res += translations[symbol]
            else:
                res -= translations[symbol]
            prev = translations[symbol]
        return res