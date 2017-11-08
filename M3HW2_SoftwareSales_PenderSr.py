# CTI 110
# M3_HW2_SoftwareSales
# Anthony Pender Sr
# 9.17.2017
#

def main ():

    packageNumber = int(input('Enter number of packages '))
    package = 99
    
    
    
    if packageNumber >=10 and packageNumber <=19:
        print ('-You will recieve a 10% discount-')
        discount = .1
    else:
        if packageNumber >=20 and packageNumber <=49:
            print ('-You will recieve a 20% discount-')
            discount = .2
        else:
            if packageNumber >=50 and packageNumber <=99:
                print ('-You will recieve a 30% discount-')
                discount = .3
            else:
                if packageNumber >=100:
                    print ('-You will recieve a 40% discount-')
                    discount = .4
                else:
                    if packageNumber <10:
                        print ('-No discount applied-')

    subTotal = package * packageNumber
    discountTotal = subTotal * discount 
    total = subTotal - discountTotal

    print ('Subtotal $', format (subTotal, '.2f'), sep='')
    print ('Discount total $', format (discountTotal, '.2f'), sep='')
    print ('Total $', format (total, '.2f'), sep='')
    
    
    
                        
        
        
    
main()
