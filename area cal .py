import math
print("area calculator") 
print("select shape:")
print("1. rectangle")
print("2. triangle")
print("3. circle")
print("4.square")
answer= int(input ("enter your choice(1-4):"))
base= float(input("enter base:"))
height= float(input("enter height:"))
radius= float(input("enter radius:"))
if answer==1:
    area=base*height
    print("area OF rectangle is:", area)
elif answer==2:
    area=0.5*base*height
    print("area OF triangle is:", area)     
elif answer==3:
    area=math.pi*radius*radius
    print("area OF circle is:", area)
elif answer==4:
    area=base*base
    print("area OF square is:", area)
else:
    print("invalid choice")