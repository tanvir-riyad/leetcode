def subsets(nums):
        subsets = [[]]
        if len(nums) == 0:
            return subsets
        else:
            for num in nums:
                new_subsets = []
                for subset in subsets:
                    print(subset)
                    new_subsets.append(subset + [num])  
                    print(new_subsets)
                subsets.extend(new_subsets)
                print('subsets',subsets) 

            return subsets


print(subsets([1,5,6,7]))