class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
         # Make sure nums1 is the smaller array, so the binary search is on the smaller side.
        A, B = nums1, nums2
        m, n = len(A), len(B)
        if m > n:
            A, B, m, n = B, A, n, m

        # We're going to search i over [0..m].  j is then determined so that
        # the left half has (m+n+1)//2 elements total.
        half = (m + n + 1) // 2
        lo, hi = 0, m

        while lo <= hi:
            i = (lo + hi) // 2
            j = half - i

            # Boundaries: if i==0 or i==m, we pretend A[i-1] or A[i] is -∞ / +∞ respectively
            A_left  = A[i-1] if i > 0 else float("-infinity")
            A_right = A[i]   if i < m else float("infinity")
            B_left  = B[j-1] if j > 0 else float("-infinity")
            B_right = B[j]   if j < n else float("infinity")

            # Are we too far right in A?  Need to move i left.
            if A_left > B_right:
                hi = i - 1
            # Are we too far left in A?  Need to move i right.
            elif B_left > A_right:
                lo = i + 1
            else:
                # Perfect partition!
                # If total length odd, median is max of left side.
                if (m + n) % 2 == 1:
                    return max(A_left, B_left)
                # If even, median is average of the two center values.
                return (max(A_left, B_left) + min(A_right, B_right)) / 2.0
        