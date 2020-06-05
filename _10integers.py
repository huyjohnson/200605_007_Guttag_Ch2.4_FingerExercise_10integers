# - Finger exercise - Guttag chapter 2.4 - break loop
attempts = 9
origInput = int(input('Please enter an integer: '))

while attempts != 0:
    numInput = int(input('You have {} inputs left. Please enter an integer: '.format(attempts)))
    if numInput % 2 == 1 and numInput > origInput:
        origInput = numInput
    else:
        origInput
    attempts -= 1
    
if origInput % 2 == 0:
    print('Sorry, no odd number was entered.')
else:
    print('{} is the largest odd number entered.'.format(origInput))
