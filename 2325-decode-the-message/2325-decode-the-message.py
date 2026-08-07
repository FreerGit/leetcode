class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        seen = set()

        aligned = [''] * 26

        place = 0
        for i in range(len(key)):
            if key[i] != ' ' and key[i] not in seen:
                print(place)
                aligned[place] = key[i]
                place += 1

            seen.add(key[i])

        out = ""

        for c in message:
            if c == ' ':
                out += ' '
            else:
                i = aligned.index(c)
                out += chr(ord('a') + i)


        return out