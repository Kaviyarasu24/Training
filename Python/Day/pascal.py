class Solution:
    def generate(self,n):
        triangle = []
        for i in range(n):
            row = [1]  
            if triangle:
                previous_row = triangle[-1]
                row.extend([previous_row[j] + previous_row[j + 1] for j in range(len(previous_row) - 1)])
                row.append(1)
            triangle.append(row)
        return triangle
n = int(input())
solution=Solution()
triangle = solution.generate(n)
for row in triangle:
    a=[]
    a.append(row)
print(a)
