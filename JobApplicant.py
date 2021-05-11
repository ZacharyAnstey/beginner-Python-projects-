"""
This program will calculate wether or not job applicant 
can qualfiy for a job. 
The requirements for the job are 
Age limit = 25 years
Experience = 5 years
Skill = Programmer
"""

Age_limit = 25
Experience = 5 
Skill = 'Programmer'
skill = input('Enter you skill set')
skill = skill.lower() # So it is not case sensitive 
age = int(input('Enter your age'))
exp = int(input('Enter how many years of experience you have'))
if ((skill == Skill) and (age >= Age_limit) or (exp> Experience)):
	print('You qualify for the job')
else:
	print('you do not qualify for the job ')