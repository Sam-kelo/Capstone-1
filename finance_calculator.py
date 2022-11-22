import math

print("Choose either investment or bond from the menu below to proceed:")

print("Investment - to calculate the amount of interest you'll earn on interest.") 

print("Bond - to calculate the amount you'll have to pay on a home loan.")


investment = "investment" 

bond = "bond"

choice = input("Enter your choice here:").lower ()


#When the user chooses investment, the following prompts will appear in order to get information from the user for the interest calculations

if choice == investment :

    print("Please fill in the following:")
                    
    deposit = float(input("Enter the amount you would like to deposit:"))

    interest_rate = float(input("Enter your prefered interest rate:"))

    years = int(input("Enter the amount of years you want to invest for:"))
        
    interest = str(input("Would you like your investment to run with simple or compound interest?").lower () )


    compound_ = "compound"

    simple_ = "simple"
    
    compound = round(deposit * math.pow((1 + interest_rate) , years))

    simple = round(deposit * (1 + interest_rate * years))


#Depending on the users choice of interest type, whether simple or compound, would require it's own calculation

#A nested if statement allows for the final calculation of interest depending on the users choice for the "interest" prompt
    
    if interest == compound_ :

      print("You will receive R{} interest." . format(compound))

    else:

     if interest == simple_ :

       print("You will receive R{} interest." . format(simple))


#Should the user choose the bond option, the following prompts appear in order to get more information from the user

#Once the information is given, a calculation will be made on how much the user needs to pay monthly
       
elif choice == bond :

    print("Please fill in the following:")

    house_value = int(input("The current value of the house:"))

    interest_rate = float(input("The interest rate of the bond:"))

    months = int(input("Number of months needed to pay off the bond:"))

    bond_calculation = round(interest_rate * house_value / (1 - (1 + interest_rate) * (- months)))

    print("R{} would need to be paid monthly." . format(bond_calculation))


#Should the user input anything other than investment or bond, the user will be prompted to choose again

else:

    print("Oops! Please choose from the options above.")
