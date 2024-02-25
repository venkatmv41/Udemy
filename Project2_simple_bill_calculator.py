#If the bill was $150.00, split between 5 people, with 12% tip. 
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60
#Write your code below this line 👇
bill = input("What is the total bill? ")
n = input("How many people are splitting the bill? ")
add_tip = input("What percentage tip would you like to give? ")
tip = (int(add_tip)/100)*float(bill)
total_bill = (float(bill)+tip)/int(n)
print(f"Each person should pay: {round(total_bill,2)}")

#NOTE :  declare the data type of input beforehand, for easier and smooth calculations later 
#like float(input("What is the total bill? "))
#n = int(input("How many people are splitting the bill? "))
#add_tip = int(input("What percentage tip would you like to give? "))

#another way to take percentages of a number and calculate total bill is :
tip = (int(add_tip)+100)/100
total_bill = (float(bill)*tip)/int(n)
print(f"Each person should pay: {round(total_bill,2)}")
