class Solution:
    def char_frequency(self, text):
        d = {}
        for c in text:
            keys = d.keys()
            if c in keys:
                d[c] += 1
            else:
                d[c] = 1
        return d

    def maxNumberOfBalloons(self, text: str) -> int:
        blnDict = self.char_frequency("balloon")
        textDict = self.char_frequency(text)
        blnCount = 0
        while True:
            for char, count in blnDict.items():
                if char in textDict and count <= textDict[char]:
                    textDict[char] -= count
                else:
                    return blnCount
            blnCount += 1

        return blnCount

