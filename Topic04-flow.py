#This program reads in a students percentage
#and prints out the corresponding grade

percentage = float(input("Enter the percentage: "))

if percentage < 0 or percentage > 100: 
    print ("Please enter a number between 0 and 100")
elif percentage < 40:
    print ("fail")
elif percentage < 50:
    print("pass")
elif percentage < 60:
    print ("merit1")
elif percentage < 70:
    print ("merit2")
else: 
    print ("distinction")