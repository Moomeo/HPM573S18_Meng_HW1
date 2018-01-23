# Question 3
def sum_rec(n):
    if n == 1:
        sum1 = 1
        return sum1
    else:
        sum1 = n + sum_rec(n - 1)
        return sum1

print(sum_rec(100))

def sum_ite(n):
    sum2 = 0
    for n in range(n + 1):
        sum2 += n
    return sum2

print(sum_ite(100))