class Solution:
    def findLargest(self, arr):
        arr = list(map(str, arr))
        arr.sort(key=lambda x: x*10, reverse=True)
        result = ''.join(arr)
        if result[0] == '0':
            return '0'
        return result
