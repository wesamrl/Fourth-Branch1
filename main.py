name=input(" Enter your name" " ")
age=input("Enter your age "" ")
address=input("Enter your address "" ")
if name.isdigit():
    name=int(name)
    print("name ivalid value")
    if age.isdigit():
       age=int(age)
    else:print("age ivalid value")

else: print("Hello Mr/Ms", name,"age",age,"\n","located in",address)






