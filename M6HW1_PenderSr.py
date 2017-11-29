# This program will determine test average and letter grade
# 11/8/2017
# CTI-110 M6HW1 - Test Average and Grade
# Anthony Pender Sr

def main():

    x = 0
    total = 0
    while x < 5:
        grades = float(input('Enter grades here: '))
        print('The letter grade is', determine_grade(grades))
        x += 1
        total += grades

    average = calc_average(total)
    
    print('Your average is : ',calc_average(total))
    
        
def calc_average(total):

    average =  total / 5
    return average

def determine_grade(letter):

    if letter < 60:
        return 'F'
    elif letter < 70:
        return 'D'
    elif letter < 80:
        return 'C'
    elif letter < 90:
        return 'B'
    else:
        return 'A'
            
main()


