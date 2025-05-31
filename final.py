import functions

# loops the action call so users can continuously utilize the program
runner=True
while runner:
    functions.action()
    a=input("Do you want to find another song(y/n)? ")
    if a=='n':
        print('Exiting program')
        runner=False

