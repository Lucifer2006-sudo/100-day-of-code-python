'''height = int(input("enter your height in cm "))

if height >=120 :
   print("you can go ahead")
else:
   print("you can not go ahead")
age = int(input("enter your age "))
if age >=18:
  print("you have to pay 60rs")
else:
  print("you have to pay 30rs ")'''
#############################################################################
'''height = int(input("enter your height in cm "))
age = int(input("enter your age "))
if height >=120 :
   print("you can go ahead")
   if age >=18:
     print("you have to pay 20$ to ride ")
   else:
     print("you have to pay 15$ to ride ")
else:
   print("you can not go ahead")'''
##############################################################################
'''height = int(input("enter your height in cm "))
age = int(input("enter your age "))
if height >=120 :
   print("you can go ahead")
else:
   print("you can not go ahead")
if age <=12:
  print("you have to pay 15rs")
elif age >=18:
  print("you have to pay 60rs")
else:
  print("you have to pay 30rs ")'''
##############################################################################
print ("Welcome to the rollercoaster! j")
height=int(input("What is your height in cm? "))
bill=0
if height>= 120:
   print("You can ride the rollercoaster")
   age = int(input("What is your age? " ) )
   if age <= 12:
    bill= 15
    print("tickets are rs 15.")
   elif age <= 18:
    bill= 30
    print("Youth tickets are rs 30. ")
   elif 45 <= age <=55:
    bill=0
    print("no need to py its on us") 
   else : 
    bill= 60
    print ("Adult tickets are rs 60.")

   want_photo=input("do you want to have a photo ?Type y for Yes and n for No. ")
   if want_photo =="y":
     bill += 3
     print(f"your final bill is {bill}")
else:
  print("you have to grow tatter before you can ride. ")