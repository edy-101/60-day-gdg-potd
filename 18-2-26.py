class Solution:
    def inversionCount(self, arr):
        self.count = 0
        self.merge_sort(arr)
        return self.count
    
    
    def merge_sort(self, arr):
        if len(arr) > 1:
            mid = len(arr) // 2
            left = arr[:mid]
            right = arr[mid:]
            
            self.merge_sort(left)
            self.merge_sort(right)
            
            i = j = k = 0
            
            while i < len(left) and j < len(right):
                if left[i] <= right[j]:
                    arr[k] = left[i]
                    i += 1
                else:
                    arr[k] = right[j]
                    self.count += len(left) - i  # Count inversions
                    j += 1
                k += 1
            
            while i < len(left):
                arr[k] = left[i]
                i += 1
                k += 1
                
            while j < len(right):
                arr[k] = right[j]
                j += 1
                k += 1
