def twoSum(nums: list[int], target: int) -> list[int]:
    num_map = {}

    for i, num in enumerate(nums):
        complement = target - num

        if complement in num_map:
            return [num_map[complement], i]
        
        num_map[num] = i
    
    return []

list = [1,2,3,4,5,6,7,8,9]
result = twoSum(list, 6)
print(result)