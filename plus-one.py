class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if (digits[-1] + 1) < 10:
            return digits[:-1] + [digits[-1] + 1]
        else:
            try:
                return self.plusOne(digits[:-1]) + [0]
            except:
                return [1,0]
