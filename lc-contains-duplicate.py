def containsDuplicate(nums):
    dupes = set()
    for i in nums:
        if i in dupes:
            return True
        else:
            dupes.add(i)

nums = (1, 1, 2, 3)
print(containsDuplicate(nums))