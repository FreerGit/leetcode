# After looking at solution, a obviously simpler solution is just to
# sort the two strings and compare. It's a bit slower though.

# A similar solution, using default dict is:
# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         if len(s) != len(t):
#             return False
#         sm = defaultdict(int)
#         tm = defaultdict(int)
#         for i in range(len(s)):
#             sm[s[i]] += 1
#             tm[t[i]] += 1
#         return sm == tm

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_m = {}
        t_m = {}
        for i, c in enumerate(s):
            if c in s_m:
                s_m[c] += 1
            else:
                s_m[c] = 1
            if t[i] in t_m:
                t_m[t[i]] += 1
            else:
                t_m[t[i]] = 1
