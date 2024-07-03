import bisect

def search(nums, target):
        i = bisect.bisect_left(nums, target)
        if i != len(nums) and nums[i] == target:
            return i
        return -1
    

nums = [-1,0,3,5,9,12]
target = 9

print(search(nums, target))