total=float(input("enter the total mark percentage:"))
if(total>90):
    print("A")
elif(total>=80 and total<=89):
    print("B")
elif(total>=70 and total<=79):    
    print("C")
elif(total>=60 and total<=69):       
    print("D")
elif(total>=50 and total<=59):          
    print("E")
else:
    print("Failed")    