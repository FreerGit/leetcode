class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        tbl = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]

        def translate(c):
            return tbl[ord(c) - ord('a')]

        uniq = set()
        for w in words:
            tt = ""
            for c in w:
                tt += translate(c)

            uniq.add(tt)

        return len(uniq)




        