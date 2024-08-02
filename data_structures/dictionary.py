dic = {}

dic["2"] = "check"
dic["3"] = "check"
dic["4"] = "check"
dic["5"] = "check"
dic["6"] = "check"

# different ways of iterating over a dictionary
for k in dic:
    print(k, dic[k])


#  what is the type of dic.keys()
print(type(dic.keys()))
print(dir(dic.keys()))
for k in dic.keys():
    print(k)


# for v in dic.values
for v in dic.values():
    print(v)