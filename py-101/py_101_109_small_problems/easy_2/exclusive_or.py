def xor(arg1, arg2):
    return bool((arg1 and not arg2) or (arg2 and not arg1))

print(xor(5, 0) == True)
print(xor(False, True) == True)
print(xor(1, 1) == False)
print(xor(True, True) == False)