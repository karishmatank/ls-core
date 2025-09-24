def get_input(message): 
    while True: 
        try: 
            num = float(input(message)) 
            break 
        except ValueError: 
            print("Value is not an valid number") 
            continue 
    return num

length = get_input("Enter the room length in meters: ") 
width = get_input("Enter the room width in meters: ")

sq_m = length * width 
sq_ft = sq_m * 10.7639 
print(f"Room area in square meters: {sq_m:.2f}") # Added on formatting after viewing solution
print(f"Room area in square feet: {sq_ft:.2f}") # Added on formatting after viewing solution

# print('{:.2f}'.format(sq_m))