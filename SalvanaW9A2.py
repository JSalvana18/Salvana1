#The Score Grader by Salvana
salvananame=input("Enter Student Name:")
salvanatotalitems=int(input("Enter total items:"))
salvanascore=float(input("Enter Score:"))

scorepercentage=(salvanatotalitems/salvanascore) * 100
salvanapassinggrade= salvanatotalitems * 0.60

if scorepercentage >=65 and scorepercentage <=100:
    salvanaResult=salvanacolor="Orange"
    salvanaRemarks="Passed"
else:
    salvanaResult=salvanaColor="Red"
    salvanaRemarks="Failed"

print(f"Student Name: {salvananame}")
print(f"Total Items : {salvanaResult}")
print(f"Score:{salvanaRemarks}")

