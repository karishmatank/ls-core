"""
Our countdown to launch isn't behaving as expected. Why? Change the code so that our program successfully counts 
down from 10 to 1 before launching.

It didn't work because counter still had value 10 through all iterations of the for loop. We need to reassign 
counter to make this work with a value of one less than its starting value. 
Otherwise, we aren't capturing the return value of the decrease function anywhere. Integers are immutable in Python, so even
though we pass by object reference, we can't mutate the object that counter is pointing to.

"""

def decrease(counter):
    return counter - 1

counter = 10

for _ in range(10):
    print(counter)
    counter = decrease(counter)

print('LAUNCH!')