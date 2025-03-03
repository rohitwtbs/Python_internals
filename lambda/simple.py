x = 50


y = lambda x: x*x+2
print(y) # lambdas donot consider the scope of the variable
print(y(x))