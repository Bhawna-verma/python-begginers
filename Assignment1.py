 #write a prog. find factorialof any numbern=int(input("Enter the value of n"))       
fac=1
for i in range(1,(n+1)):
    fac=fac*i                                                                 
    print("the factorial of n is=",fac)
    
    
    #write a prog. to take 10 integer from keyboard using loop and
#and print their average value on the screen
Totalnum=10
Sum=0
for i in range(1,11):
    n=int(input("Enter the values"))
    Sum=Sum+n
    avg=Sum/Totalnum
    print("avg=",avg)
    
    
 #write a prog. for finding Even number between 1to100
i=1
while i<=100:
   if i%2==0:
       print(i)
   i+=1
   
   
   
   #write a prog. for printing A table by user input number in the follwing formate
#2*1=2 and also calculate the sum of result after the multipliying of table
#such as 2*1=2
         #2*2=4
 #the sum is =6
n=int(input("Enter any number"))
sum=0
for i in range (1,10+1):
    print(n,"*",i,"=",n*i)
    sum=n*i+sum
    print("sum=",sum)




   
