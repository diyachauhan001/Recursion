import bisect

def search( nums, target):
    index = bisect.bisect_left(nums, target)
    return index if index < len(nums) and nums[index] == target else -1

num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(search(num, 5))