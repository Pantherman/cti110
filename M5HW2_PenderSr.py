def main():

    runningTotal = 0
    number = 0
    while number >= 0:
        number = int(input('Enter a number: '))
        runningTotal += number
        if number < 0:
            runningTotal = runningTotal - number
            print('Total: ',runningTotal)


        
main()
