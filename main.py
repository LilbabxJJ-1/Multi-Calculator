#More soon.
#Operation Chart

again = True
while again == True:
 with open("options.txt") as options:
  lines = options.read()
  print(lines)

  with open("credits.txt") as credit:
   line = credit.read()
   print(line)
  
 available_options = [1,2,3,4]

 while True:
  try:
   operation = int(input("Which do you want to do? "))
   if operation not in available_options:
    print('\033[1m' + 'That\'s not an option!' + '\033[0m')
   else:
     break
  except ValueError:
   print("Please select a number!")



#First Operation


 if operation == 1:
  v1 = float(input("What is your inital velocity? "))
  v2 = float(input("What is your final velocity? "))

  def velocity(v1, v2):
    vel = v2 - v1
    return vel

  velocity(v1, v2)
  print(f"Your velocity is: {velocity(v1, v2)}")
  
  another = input("Do you want to do another? (Y/N) ")
  if another == "Y" or another == "y":
    again = True
  else:
    print("Alright! Come back later")
    again = False 
#Second Operation 

 if operation == 2:
   vc = float(input("What is your velocity? "))
   tm = float(input("What is your time? "))
   def acceleration(accelertion, time):
    ac = vc / tm
    print(f"Your acceleration is: {ac}")
   acceleration(vc, tm)

   another = input("Do you want to do another? (Y/N) ")
   if another == "Y" or another == "y":
    again = True
   else:
    print("Alright! Come back later")
    again = False 

#Third Operation
 if operation == 3:
  add1 = float(input("What's your first number? "))
  add2 = float(input("What number do you wanna add? "))
  def add(num1, num2):
    sum = add1 + add2
    print(f"Your Sum: {sum}")
  add(add1, add2)

  another = input("Do you want to do another? (Y/N) ")
  if another == "Y" or another == "y":
    again = True
  else:
    print("Alright! Come back later")
    again = False 

#fourth Operation
 if operation == 4:
  sub1 = float(input("What's your first number? "))
  sub2 = float(input("What number do you wanna subtract? "))
  def subtract(num1, num2):
    sub = sub1 - sub2
    print(f"Your Sub: {sub}")
  subtract(sub1, sub2)

  another = input("Do you want to do another? (Y/N) ")
  if another == "Y" or another == "y":
    again = True
  else:
    print("Alright! Come back later")
    again = False 