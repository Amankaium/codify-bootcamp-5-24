nums = [6, 25, 22, 0, 4, 6, 7, 2]
# найти сумму элементов без sum(nums)

sm = 0
i = 0
while i < len(nums):
    sm += nums[i]
    i += 1
print(sm)
print(sm/len(nums))
