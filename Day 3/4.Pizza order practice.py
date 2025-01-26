print ("Welcome to the indian pizzas! j")
size=input("what size of pizza do you want S , M OR L ?")
peperoni=str(input("do you want extra peperoni Y / N ? "))
cheese=str(input("do you want extra Cheese Y / N ?"))

bill=0
if size=="S":
    bill += 90
elif size=="M":
    bill += 180
elif size=="L":
    bill += 210
else:
    print("invallid input")

if peperoni=="Y":
    bill +=25
else:
    peperoni =="N"
    bill +=0
if cheese=="Y":
    bill +=20
else:
    cheese =="N"
    bill +=0
print(f"your final bill is {bill}")
