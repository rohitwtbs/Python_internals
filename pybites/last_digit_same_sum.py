# There is an array A consisting of N integers. What is the maximum sum of two integers from A that have common  first and last digits?  If there are no two integers that have common  first and last digits, the function should return −1.

# Examples:

# 1. Given A = [405, 45, 300, 300], the function should return 600. There are two pairs of integers that share first and last digits: (405, 45) and (300, 300). The sum of the two 300s is bigger than the sum of 405 and 45.

# 2. Given A = [30, 909, 3190, 99, 3990, 9009], the function should return 9918.
def last_two(num):
    ls_of_numbers = []
    while num > 0:
        last_digit = num %10
        ls_of_numbers.append(last_digit)
        num = num//10
        
    # print(ls_of_numbers)
    key = ls_of_numbers[-1] * 10 + ls_of_numbers[0]
    return key  

a = [30,909,3190,99,9009,3990]
dic = {}
for i in a:
    # print(last_two(i))
    key =last_two(i)
    if key not in dic:
        dic[key] = []
    dic[key].append(i)

print(dic)
sums = []
for i in dic:
    dic[i].sort()
    if(dic[i][-1] != dic[i][-2]):
        sums.append(dic[i][-1] + dic[i][-2])

sums.sort()
print(sums[-1])