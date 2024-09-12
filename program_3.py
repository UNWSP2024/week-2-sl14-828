#Samuel Lee - Sept 12th
#this program asks for 5 price values of 5 items, displays the subtotal, the amount of sales tax, and the total.

def calculate_total_purchase():

#prompt
    print('This program asks for 5 price values of 5 items, '
      'displays the subtotal, the amount of sales tax, '
      'and the total.')

#intializers
    counter = 0
    subtotal = 0
    tax = .07
    taxpercent = tax * 100

#user input with while loop counter
    print('(Please use 00.00 format! (example: 15.99)')
    while counter < 5:
        singleItemValue = float(input('Please Enter a Price: $'))

        #Calculations of totalAge
        subtotal += singleItemValue
        counter += 1

#Calculate Total After Tax and Display
    total = subtotal * (tax + 1)

    print('Subtotal: $', (round(subtotal, 2)),
      '\nSales Tax: ', (round(taxpercent, 2)) ,'%'
      '\nTotal: $', (round(total, 2)))



calculate_total_purchase()
