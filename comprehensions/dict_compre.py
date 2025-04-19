sample = {x: x*x for x in range(10)}
sampl2 = {y:x*x for x in range(10) for y in range(10)}
smaple3 = {x: x*y*z for x in range(10) for y in range(10) for z in range(10)}
print(sample)
print(sampl2)
print(smaple3)