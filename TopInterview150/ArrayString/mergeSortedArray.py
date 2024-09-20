class Solution1(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        i = m-1
        j = n-1
        l = m + n -1
        
        while j >= 0:
            if nums1[i] > nums2[j] and i >= 0:
                nums1[l] = nums1[i]
                i -= 1
            else:
                nums1[l] = nums2[j]
                j -= 1
            l -= 1

        return nums1
    
class Solution2(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        for j in range(n):
            nums1[m + j] = nums2[j]
        nums1.sort()

sol = Solution1()
print(sol.merge([1,2,3,0,0,0], 3, [2,5,6], 3))