class Solution:
    def overlapInt(self, arr):
        n = len(arr)
        
        # Separate start and end times
        start = sorted(interval[0] for interval in arr)
        end = sorted(interval[1] for interval in arr)
        
        i = j = 0
        current_overlap = 0
        max_overlap = 0
        
        # Traverse through all start times
        while i < n:
            # If next interval starts before or when current one ends
            if start[i] <= end[j]:
                current_overlap += 1
                max_overlap = max(max_overlap, current_overlap)
                i += 1
            else:
                current_overlap -= 1
                j += 1
        
        return max_overlap
