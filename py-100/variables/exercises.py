# Q8: Interest after 5 years with a 5% interest rate assuming you start with $1,000. Simple interest calculation

start = 1000
balance = 1000 * (1.05 ** 5)
print(balance)

# Q9: Repeat Q8 but use augmented assignment to calculate one year at a time
start = 1000
start *= 1.05
start *= 1.05
start *= 1.05
start *= 1.05
start *= 1.05
print(start)

# Q10: 