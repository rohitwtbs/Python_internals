x = 50


y = lambda x: x*x+2
print(y) # lambdas donot consider the scope of the variable
print(y(x))

# passing container types to a lambda

ls =[2,3,4,5,6]

z = lambda x:sum(x)
print(z(ls))