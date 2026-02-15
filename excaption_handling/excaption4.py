l=[25,77,88,65,88,54,54,365,74,665,44]
try:
    print(l[0])
except IndexError as I:
    print("Invalid Index Error:",I)
else:
    print(l)
finally:
    pass