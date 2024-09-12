#Samuel Lee - Sept 9th
#program that calculates and displays the Average age of 5 people

def average_age():
# Get User Input
    counter = 0
    totalAge = 0
    while counter < 5:
        age = float(input('Please enter an Age: '))

#Calculations of totalAge/sum
        totalAge += age
        counter += 1

# Average the ages
    Average = totalAge / counter

# Print the results
    print('The Average of the ages is', Average, 'years.')

# Line which calls the above function.
average_age()
