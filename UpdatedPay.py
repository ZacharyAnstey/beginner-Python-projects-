"""
This is a program to update a employs pay
Assuming that there company gives a 5% raise a 5 years and 10% after that 
"""
Raise1 = 0.1 # 10% raise 
Raise2 = 0.05 # 5% raise 
Year_Limit = 5 
pay = float(input('Plese enter the current pay rate of the employee'))
years = float(input('Enter the number of years that the person has worked with you '))
if (years > Year_Limit):
	pay = pay * (1+Raise1)
else:
	pay = pay * (1+Raise2)
print('The updated pay is $%.2f.'%pay 'Per hour ')