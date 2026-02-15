laptop={"Brand":"HP","Modal":"Pavilion","CPU":"Intel corei7 13th gen","RAM":16,"Rating":4.4}
try:
    key=input("Enter the key:")
    print(laptop[key])
except KeyError as K:
    print("Exception Caught: Invalid key",K)
else:
    print(laptop)
finally:
    pass
