import sys

nums = [0] * 11
nums[1] = 1
nums[2] = 2
nums[3] = 4

for i in range(4, 11):
    nums[i] = nums[i - 3] + nums[i - 2] + nums[i - 1]

t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    print(nums[n])