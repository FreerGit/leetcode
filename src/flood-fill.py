class Solution:
    def helper(self, image, sr, sc, color, rows, cols, start):
        if sr >= 0 and sr < rows and sc >= 0 and sc < cols and image[sr][sc] == start:
            image[sr][sc] = color
            self.helper(image, sr+1, sc, color, rows, cols, start)
            self.helper(image, sr-1, sc, color, rows, cols, start)
            self.helper(image, sr, sc+1, color, rows, cols, start)
            self.helper(image, sr, sc-1, color, rows, cols, start)


    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        start = image[sr][sc]

        rows = len(image)
        cols = len(image[0])

        if image[sr][sc] != color:
            self.helper(image, sr, sc, color, rows, cols, start)
        image[sr][sc] = color
        return image