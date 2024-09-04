# write a program to sort a dictonary according to its values

d = {"Bangalore":25, "leh":-2,"Delhi":45,"Chennai":43}
print(d)
print(d.items())
print(sorted(d.items()))
sorted_dict = dict(sorted(d.items(), key=lambda item: item[1], reverse=False))
print(sorted_dict)
