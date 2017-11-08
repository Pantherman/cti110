# CTI-110 
# M2HW2 - Tip Tax Total 
# Anthony Pender Sr
# September 12

foodCost = float(input('Enter charge of food '))
tipAmount = float(0.18 * foodCost)
salesTax = float(0.07 * foodCost)
totalCost = float(foodCost + salesTax + tipAmount)
print ('18% tip-' , format (tipAmount, '.2f'))
print ('7% sales tax-' , format (salesTax, '.2f'))
print ('Total Cost--' , format (totalCost, '.2f'))

