"""
Exercise 3.11 (Miles Per Gallon)
Drivers are concerned with the mileage obtained by their automobiles. 
One driver has kept track of several tankfuls of gasoline by recording miles driven and gallons used for each tankful.
Develop a sentinel-controlled-repitition script that prompt the user to input the miles driven and gallons used for each tankful.
The script should calculate and display the miles per gallon obtained for each tankful. 
After processing all input information, the script should calculate and display the combined miles per gallon obtained for all tankfulls (that is, total miles driven divided by total gallons used).
"""

# Modifier to stop while loop once user is done inputting all information
continue_input = True
# Assign variables empty lists
total_miles = []
total_gallons = []
mpg = []

# While loop to input Miles and Gallons
while continue_input:
    miles = input('Enter the miles driven: ')
    # Ensures user input is a digit and greater than 0 (Miles)
    if miles.isdigit():
        if int(miles) > 0:
            print(f'Miles Inputed: {int(miles):,}')
            # Adds miles to total_miles list
            total_miles.append(int(miles))

            # Ensures user input is a digit and greater than 0 (Gallons)
            while True:
                gallons = input('Please enter number of gallons used: ')
                if gallons.isdigit():
                    if int(gallons) > 0:
                        print(f'Gallons Inputed: {int(gallons):,}')
                        # Adds gallons to total_gallons
                        total_gallons.append(int(gallons))
                        # Calculates MPG and adds to mpg list
                        mpg.append(int(miles)/int(gallons))
                        print(f'MPG Usage: {int(miles)/int(gallons):.2f}')

                        # Ensures user input is either y or n
                        while True:
                            input_more = input('Would you like to add more miles and gallons?: (Y or N)')
                            if input_more.lower() == 'y':
                                break
                            elif input_more.lower() == 'n':
                                # If user does not want to continue, stops while loop for continued input
                                continue_input = False
                                break
                            
                        # Breaks out of gallon while loop
                        break

print('Total Results Below: \n')
print(f'Total Miles Driven: {sum(total_miles):,}')
print(f'Total Gallons Used: {sum(total_gallons):,}')
print(f'Average MPG: {sum(mpg)/len(mpg):.2f}')