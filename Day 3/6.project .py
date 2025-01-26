print("Wellcome to the tresure hunt \nLets Get started with your adventure !")
direction=(input("where do you want to go Left or Right ?"))
choise_2=(input("craft a boat or swim across"))
choise_3=(input("Which door whould you open only one has tressure RED, YELLOW, WHITE?"))

if direction== "left":
    print("my be you are going in right direction!")
elif choise_2=="BOAT":
    print("nice!")
elif choise_2=="SWIM":
    print("game over \nYou were attacked by sharks")
if choise_3=="YELLOW":
    print("you found the devine tresure")
if choise_3=="RED":
    print("GAME OVER \nsucked by eternity")    
if choise_3=="WHITE":
    print("GAME OVER \nDemons ate you")
else:
    direction== "Right"
    print("game over \nIt was a lava pool")



