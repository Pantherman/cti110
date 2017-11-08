#This program will determine which rectangle has the bigger area.
#Anthony Pender Sr
#CTI 110
#William Buckwell
#September 13 2017

# Get the lenght and width of both rectangles.
length1 = int(input('Enter length of Rectangle 1 '))
width1 = int(input('Enter width of Rectangle 1 '))
length2 = int(input('Enter lenght of Rectangle 2 '))
width2 = int(input('Enter width of Rectangle 2 '))

#Calculate area of both rectangles.
area1 = int( length1 * width1 )
area2 = int( length2 * width2 )

#Determine which rectangle is larger or equal area.
if area1 > area2:
    print ('Rectangle 1 is larger')
else:
    if area2 > area1:
        print ('Rectangle 2 is larger')
    else:
        print ('Both have same area')
        
