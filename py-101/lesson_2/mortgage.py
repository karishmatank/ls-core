def prompt(message):
    message = f"==> {message}"
    print(message)

def clean_up_symbols(str_num):
    # Take a string representing a number, clean up , or % symbols
    symbols = ['%', ',', '$']
    for symbol in symbols:
        str_num = str_num.replace(symbol, '')
    return str_num

def check_float(num):
    try:
        num = float(clean_up_symbols(num))
        return num
    except ValueError:
        prompt("Hmm, that's not a valid number. Please try again!")
        return None

def check_pos(num):
    if num > 0:
        return True

    prompt("Hmm, this input shouldn't be negative or zero, try again!")
    return False

def check_validity():
    number_valid = False

    while not number_valid:
        # Check that user input is a float
        num = check_float(input())
        if num is None:
            continue

        # Check that number is positive and non-zero
        if not check_pos(num):
            continue

        number_valid = True

    return num

def check_validity_duration():
    number_valid = False

    while not number_valid:
        # Check years
        prompt("Years: ")
        while True:
            # Check that user input is a float
            num_yr = check_float(input())
            if num_yr is not None:
                break

        # Check months
        prompt("Months: ")
        while True:
            # Check that user input is a float
            num_mo = check_float(input())
            if num_mo is not None:
                break

        # Check combined figure
        # Calculate loan duration in months
        num = num_yr * 12 + num_mo

        # Check that number is positive and non-zero
        if check_pos(num):
            number_valid = True

    return num

def get_inputs():
    # Get loan amount, APR, and loan duration from user
    prompt("What is your total loan amount in $?")
    amt = check_validity()

    prompt("What is your APR, in percent? i.e. [ ]%")
    rate = check_validity()

    prompt("What is the loan duration?")
    dur = check_validity_duration()

    return amt, rate, dur

def calculate_payment(amt, rate, dur):
    return amt * (rate / (1 - (1 + rate) ** (-dur)))

def print_amount(result):
    prompt(f"Your monthly payment is ${result:,.2f}")


prompt("Welcome to the mortgage payment calculator!")

loan_amount, apr, duration = get_inputs()

# Calculate monthly interest rate
int_monthly = (apr / 100) / 12

# Calculate monthly payment using loan amount,
# monthly interest rate, and loan duration in months
monthly_payment = calculate_payment(loan_amount, int_monthly, duration)

# Print result for user
print_amount(monthly_payment)