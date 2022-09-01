#Nikola Petreski
#M02 Lab
#This program will ask you to enter your name and GPA, and inform you if you have made either the Honor Roll or the Dean's List.

def gpaReturn():

  firstName = input("Please enter your first name: ")
  gpaInput = float(input("Please enter your GPA: "))
  if (gpaInput>=3.5):   
    print(f"Congratulations, {firstName}! You have made the Dean's List.")
  elif (3.5>gpaInput>=3.25):
    print(f"Congratulations, {firstName}! You have made the Honor Roll.")
  else:    
    print(f"Sorry, {firstName}! You have not made the Dean's List or the honor roll.")

def gpaFunction():
  lastName = input("Please enter your last name. If you would like to exit, please type 'ZZZ': ")   
  while lastName == 'ZZZ':
    print('Thank You.')
    break
  else: gpaReturn()

gpaFunction()
