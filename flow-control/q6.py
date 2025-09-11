def capitalize_long_str(x):
    if len(x) < 10:
        return x
    else:
        return x.upper()
    
print(capitalize_long_str('goodbye'))
print(capitalize_long_str('hello world'))