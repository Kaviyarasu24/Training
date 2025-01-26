def climbStairs(n):
        if n == 0 or n == 1:
            return 1
        prev, curr = 1, 1
        for i in range(2, n+1):
            temp = curr
            curr = prev + curr
            prev = temp
        return curr
num=int(input("Enter the number: "))
print(climbStairs(num))