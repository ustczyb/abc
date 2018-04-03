# coding=utf-8
"""
给定一个整数数列，找出其中和为特定值的那两个数。

你可以假设每个输入都只会有一种答案，同样的元素不能被重用。

示例:

给定 nums = [2, 7, 11, 15], target = 9

因为 nums[0] + nums[1] = 2 + 7 = 9
所以返回 [0, 1]
"""
def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    dict = {}
    res = []
    for i in range(len(nums)):
        entry = {nums[i] : i}
        dict.update(entry)
    for i in range(len(nums)):
        tar = target - nums[i]
        if tar == nums[i]:
            for j in range(i + 1, len(nums)):
                if nums[j] == tar:
                    res.append(i)
                    res.append(j)
                    return res
            continue
        if dict.has_key(tar):
            res.append(i)
            res.append(dict.get(tar))
            return res
    return res

    # leetcode上更好的解答
    # dict = {}
    #
    # for i, n in enumerate(nums):
    #     m = target - n
    #     if m in dict:
    #         return [dict[m], i]
    #     else:
    #         dict[n] = i



if __name__ == '__main__':
    nums = [3, 3]
    target = 6
    print(twoSum(nums, target))