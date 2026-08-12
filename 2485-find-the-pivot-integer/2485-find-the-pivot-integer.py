class Solution:
    def pivotInteger(self, n: int) -> int:
        running = 0

        for i in range(1, n + 1):
            running += i
            
            between = 0
            for j in range(i, n + 1):
                between += j
                
            if running == between:
                return i

        return -1