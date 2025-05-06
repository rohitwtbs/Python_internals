
A = {"min": 2}

B = {"min": 2, "max": 3}

C = {"min": 2, "max": 3, "sum": 5}


# print(A["min"] + B["min"] + C["min"])

print(A.get("min",0) + B.get("min",0) + C.get("min",0))