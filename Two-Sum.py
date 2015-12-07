class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hash = {}
        for i in xrange(0, len(nums)):
            if target-nums[i] in hash:
                return [hash[target-nums[i]]+1, i+1]
                
            hash[nums[i]] = i
