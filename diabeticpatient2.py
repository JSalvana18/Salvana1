patients={"Rhea": (96,120,105),
          "Ana" : (70,180,100) }
print(patients)
normal= 120
for key, value in patients.items():
    #print(key,value)
    print(value)
    for v in value:
        if v>normal:
            print(key, "diabetic")
        else:
            print(v,"normal")

