x = 50


y = lambda x: x*x+2
print(y) # lambdas donot consider the scope of the variable
print(y(x))

# passing container types to a lambda

ls =[2,3,4,5,6]

z = lambda x:sum(x)
print(z(ls))

# lest check dictionary

dic = {
    "chennai": 25,
    "bangalore": 15,
    "delhi": 20
}

zz = lambda x:len(x)

print(zz(dic))

import dis

print(dis.dis(zz))
# output
        #   0 RESUME                   0
        #       2 LOAD_GLOBAL              1 (NULL + len)
        #      14 LOAD_FAST                0 (x)
        #      16 PRECALL                  1
        #      20 CALL                     1
        #      30 RETURN_VALUE