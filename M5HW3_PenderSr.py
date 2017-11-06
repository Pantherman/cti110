def main():

    factNum = int(input('Enter a non-negative integer '))
    num = 1
    for i in range(factNum):
        num = num * (i+1)
    print('The factorial for',factNum, 'is',num)
    
main()
