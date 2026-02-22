class Solution:
    def subarrayXor(self, arr, k):
        count = 0
        prefix = 0
        freq = {0: 1}
        
        for num in arr:
            prefix ^= num
            if prefix ^ k in freq:
                count += freq[prefix ^ k]
            freq[prefix] = freq.get(prefix, 0) + 1
        
        return count
