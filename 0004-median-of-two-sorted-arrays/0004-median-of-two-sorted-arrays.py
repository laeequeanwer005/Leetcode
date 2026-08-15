class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        # Make nums1 the smaller array
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        left = 0
        right = len(nums1)

        while left <= right:

            # Partition nums1
            mid1 = (left + right) // 2

            # Partition nums2
            mid2 = (len(nums1) + len(nums2) + 1) // 2 - mid1

            # Values around the partitions
            left1 = nums1[mid1 - 1] if mid1 > 0 else float("-inf")
            right1 = nums1[mid1] if mid1 < len(nums1) else float("inf")

            left2 = nums2[mid2 - 1] if mid2 > 0 else float("-inf")
            right2 = nums2[mid2] if mid2 < len(nums2) else float("inf")

            # Correct partition
            if left1 <= right2 and left2 <= right1:

                # Odd total number of elements
                if (len(nums1) + len(nums2)) % 2 == 1:
                    return max(left1, left2)

                # Even total number of elements
                return (max(left1, left2) + min(right1, right2)) / 2

            # We took too many elements from nums1
            elif left1 > right2:
                right = mid1 - 1

            # We took too few elements from nums1
            else:
                left = mid1 + 1