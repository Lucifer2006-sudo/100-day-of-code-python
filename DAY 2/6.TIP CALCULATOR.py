bill_amount=(float(input("what was the total bill ?")))

tip_amount=int(input("how much tip would you like to give 10 , 50 , 100 ?"))
number_of_people_to_split_with=int(input("number of people to split the bill with "))
total_bill= tip_amount/100 * bill_amount + bill_amount
split_amount_per_person=(total_bill/number_of_people_to_split_with)
print(total_bill)
print(split_amount_per_person)