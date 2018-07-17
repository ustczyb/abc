"""
给定一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？找出所有满足条件且不重复的三元组。

注意：答案中不可以包含重复的三元组。

例如, 给定数组 nums = [-1, 0, 1, 2, -1, -4]，

满足要求的三元组集合为：
[
  [-1, 0, 1],
  [-1, -1, 2]
]
"""


def threeSum(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    我的思路（超时了）：将这个数组拆分成正数和负数两个数组，取绝对值后排序 问题转换为两个有序数组，一个数组是否存在一个元素，是的它是另一个数组两个元素的和
    """
    result = []
    nums.sort()

    def next_index(nums, index, flag):
        value = nums[index]
        next_i = index
        if flag:
            while next_i < len(nums) and nums[next_i] == value:
                next_i += 1
        else:
            while next_i > -1 and nums[next_i] == value:
                next_i -= 1
        return next_i


    def find_sum(i, nums):
        """
        在排序数组nums中找到两个数，它们的和是nums[i]且这两个数分布在i的后面
        :type i: int
        :type nums: list
        :rtype: list[(,)]
        """
        res = []
        if nums[i] > 0:
            return res
        lo, hi = i + 1, len(nums) - 1
        while lo < hi:
            if nums[lo] + nums[hi] == -nums[i]:
                res.append((nums[lo], nums[hi]))
                hi = next_index(nums, hi, False)
                lo = next_index(nums, lo, True)
            elif nums[lo] + nums[hi] > -nums[i]:
                hi = next_index(nums, hi, False)
            else:
                lo = next_index(nums, lo, True)
        return res

    i = 0
    while i < len(nums):
        for n1, n2 in find_sum(i, nums):
            result.append([n1, n2, nums[i]])
        value = nums[i]
        while i < len(nums) and nums[i] == value:
            i += 1

    return result


if __name__ == '__main__':
    nums = [0, 0, 0, 0, 0, 0, 0]
    print(threeSum(nums))
µ