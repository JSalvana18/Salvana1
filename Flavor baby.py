flavor=input("Enter pizza flavor (Hawaiian/Pepperoni/oreo):").lower()
quantity=int(input("Enter quantity of pizza:"))
if flavor=="hawaiian":
    print("You selected Hawaiian Pizza. ")

    size=input("Enter size (Small/Medium/Large):").lower()

    if size=="small":
        price = 250
    elif size=="medium":
        price =350
    elif size=="large":
        price = 450
    else :
        price = 0
        print("Invalid choice of size :)")


total = price * quantity

print("Total price is $",total)