print("Rollercoster check.")
height = int(input("Please enter your height (cm): "))
bill = 0

if height > 120:
    print("You can ride!")
    age = int(input("Please enter your age: "))
    if age < 12:
        bill = 5
        print("Child ticket = 5$.")
    elif age <= 18:
        bill = 7
        print("Youth ticket = 7$.")
    elif age >= 45 & age <= 55:
        print("Yo dude, get well with your crisis. Go ride for free.")
# 2 строки сверху появились для нового elif >45 <55 - bill не используется, так как не меняется
    else:
        bill = 12
        print("Adult ticket = 12$.")
    photo = input("Do you want a photo? It's 3$ extra. Type Y / N ")
    if photo == "Y":
        bill += 3
    print(f"Your final bill is {bill}$")

else:
    print("You can't ride.")
