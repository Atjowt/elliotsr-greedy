n = int(input())
nums = [int(input()) for _ in range(n)]

n = len(nums)

result = 0

lis = [1] * n
lds = [1] * n
for i in reversed(range(n)):
    for j in range(i+1, n):
        if nums[i] < nums[j]:
            lis[i] = max(1 + lis[j], lis[i])
        if nums[i] > nums[j]:
            lds[i] = max(1 + lds[j], lds[i])
    result = max(result, (lds[i] - 1) + 1 + (lis[i] - 1))

print(result)