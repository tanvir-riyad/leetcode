def find_two_single_numbers(nums):
    xor_result = 0
    for i in nums:
        xor_result ^= i
    
    
    #find the rightmost set bit
    rightmost_bit = 1
    while (rightmost_bit & xor_result) == 0:
        rightmost_bit <<= 1
    group1, group2 = 0, 0

    for num in nums:
        if (num & rightmost_bit) == 0:
            group1 ^= num
        else:
            group2 ^= num
    return [group1, group2]
    


print(find_two_single_numbers([1,2,1,3,2,5]))
