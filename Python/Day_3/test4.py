def numberOfArithmeticSlices(nums):
    n = len(nums)
    if n < 3: return 0

    dp = [0] * n
    total = 0

    for i in range(2, n):
        if nums[i] - nums[i-1] == nums[i-1] - nums[i-2]:
            dp[i] = dp[i-1] + 1
            total += dp[i]

    return total

num = input("Enter the numbers separated by commas: ")
a = list(map(int, num.split(",")))
print(numberOfArithmeticSlices(a))