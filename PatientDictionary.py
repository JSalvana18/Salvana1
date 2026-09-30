patients={"Rhea": (96,120,105),
          "Ana" : (70,180,100) }
normal= 120
for pn,bs in patients.items():
    #print(pn, *bs)
    if(pn=="Rhea"):
        print("Blood sugar summary")
    for value in bs:

        if value<120:
            print(value,"diabetic")
        else:
            print(value,"normal")
highest=max(bs)
print("Highest blood sugar count",highest,"-",pn)
lowest=min(bs)
print(lowest,pn)
diff=highest-lowest
print(diff)