def backtrack(nums, current_permutation, result):
    if len(current_permutation) == len(nums):
        result.append(list(current_permutation))
        return

    for num in nums:
        # If the current number is not in the current permutation, add it and backtrack.
        if num not in current_permutation:
            current_permutation.append(num)
            backtrack(nums, current_permutation, result)
            current_permutation.pop()

def permutations(nums):
    result = []
    backtrack(nums, [], result)
    return result

nums = [1, 2, 3]
result = permutations(nums)
print(result)
