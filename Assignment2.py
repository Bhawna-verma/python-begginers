# write a program of python for taking two input from user and perform addition ,subtraction ,multiplication ,division operation on the inputa=int(input("Enter the value of a\n"))
b=int(input("Enter the value of b\n"))
print(a+b)
print(a*b)
print(a/b)
print(a-b)

#write a program to check the given input is integer type or not
a=int(input("Enter the value of a"))
b=20
if type(a)==type(b):
    print("it is integer")
else:
    print("it is not integer")
    

#write a program for taking the value from user in list such as your name, class, rollno., collage name, branch and print all this in one line print funtion

list = []
Name=input("Enter name")
Class=input("Enter class")
Rollno=input("Enter rollno")
Collage=input("Enter collage")
Branch=input("Enter branch")
list.append(Name)
list.append(Class)
list.append(Rollno)
list.append(Collage)
list.append(Branch)
print(list)




#write a program to check given input is the item or not
list=["nishi","shalu","bhawna","shivani"]
item=input("Enter the value of item")
if item==list:
    print("given item is in list")
else:
    print("given item is not in list")
