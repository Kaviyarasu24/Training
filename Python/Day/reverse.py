class Solution:
    @staticmethod
    def reverse_number(num):
        rev = 0
        if num > 0:
            n=len(str(num))
            for _ in range(n):
                rev = rev * 10 + (num % 10)
                num //= 10
            return rev

        else:  
            num = num * -1
            n=len(str(num))
            for _ in range(n):
                rev = rev * 10 + (num % 10)
                num //= 10
            return rev*-1
a = int(input("Enter a number to reverse: "))
print(Solution.reverse_number(a))