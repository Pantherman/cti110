# CTI-110 
# M3HW1 - Age Classifier 
# Anthony Pender Sr
# 9.17.017
# This program states by age if you are an infant, child, teen, or adult


def main():

    personAge  = int(input('How old am I? '))

    if personAge <= 1:
        print ('You are an infant')
    else:
        if personAge >1 and personAge <13:
            print ('You are a child')
        else:
            if personAge >=13 and personAge <20:
                print ('You are a teen')
            else:
                if personAge >=20:
                    print ('You are an adult')
                    
            
main ()

