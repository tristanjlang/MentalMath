from decimal import *
import random
from timeit import default_timer as timer

'''
Randomly generate two numbers:
-50% chance the number is a whole number vs percent with 1 decimal place

Prompt user for input:
-If the result is "quit" then end the loop
-If the result is correct, tell them
-Display the total time the user took to work on the problem

Wait 3-5 seconds, then loop back through and get two new numbers
'''

userinput = ''
numtype = ('whole', 'percent')
times = []

while True:
    choice = random.choice(numtype)
    n1 = Decimal(random.randint(0, 1000)) if choice == 'whole' else Decimal(random.randint(0, 100)) / Decimal(100)
    n2 = Decimal(random.randint(0, 100)) / Decimal(100)
    print('Solve: ' + str(n1) + ' x ' + str(n2))
    start = timer()

    userinput = input('Input: ')
    if userinput.lower() == 'quit': break

    try:
        userinput = Decimal(userinput)
        end = timer()
        elapsed = round(end - start, 1)
        if userinput == n1 * n2: print('CORRECT')
        else: print('INCORRECT...' + str(n1 * n2))
        print('Time to solve: ' + str(elapsed) + ' seconds\n')
        times.append(elapsed)
    except:
        print('Improper entry, next problem...\n')

print('Average time to solve: ' + str(round(sum(times) / len(times), 1)) + ' seconds')