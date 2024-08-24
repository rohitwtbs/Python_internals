country = ["india", "usa", "uk", "armenia"]

city = ["a","b","c","d"]


zipped = zip(country,city)

print(zipped)

for i in enumerate(zipped,start=65):
    print(i)
    print(i[0])
    print(type(i))

for j in zipped:
    print(j)