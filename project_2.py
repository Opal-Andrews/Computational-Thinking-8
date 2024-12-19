#Beginning:
hoodie_points = 0
shirt_points = 0

#Middle:
answer = input ("On a break would you rather A) be on summer break, or B) winter break? ")
if answer == "A":
    hoodie_points += 1
elif answer == "B":
    shirt_points += 1

answer = input ("Ordering a drink would you rather A) order soda, or B) Order juice ")
if answer == "A":
    hoodie_points += 1
elif answer == "B":
    shirt_points +=1

answer = input ("On a rainy day would you rather A) bring an umbrella, or B) bring a puffer ")
if answer == "A":
    hoodie_points
elif answer == "B":
    shirt_points +=1

answer = input ("Spending time on your phone would you rather A) use snapchat, or B) use instagram ")
if answer == "A":
    hoodie_points += 1
elif answer == "B":
    shirt_points +=1

answer = input ("listening to music would you rather A) listen to rap, or B) listen to pop ")
if answer == "A":
    hoodie_points += 1
elif answer == "B":
    shirt_points +=1

#End:
if hoodie_points > shirt_points:
    print ("You are a hoodie person")
elif shirt_points > hoodie_points:
    print ("You are a shirt person")
elif hoodie_points == shirt_points:
    print ("You like shirts and hoodies the same")