salvananame=input("Student Name: ")
salvanagrade=float(input("Enter Grade:"))

match salvanagrade:
    case n if 90 <= salvanagrade <= 100:
        print("Excellent")
    case n if 80 <= salvanagrade <=89:
        print("Very Good")
    case n if 75 <= salvanagrade <=79:
        print("Passed")
    case n if 0 <= salvanagrade <= 74:
        print("Failed")
    case _:
        print("Invalid Grade")



