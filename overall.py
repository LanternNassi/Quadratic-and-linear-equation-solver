import math
from Equation import Quadratic_Equation
from Equation import cubic_equation
print("WELCOME TO THE EQUATIONS HUB.")
print("Enter what u want to be solved whether (1) for quadratic equation or (2) for cubic equation.")
user_provision=int(input("Enter the kind of equation(1,2):"))
if user_provision==1:
    w=input("\nENTER YOUR NAME PLEASE:")
    a=int(input("\nEnter the first coefficient:"))
    b=int(input("Enter the second coefficient:"))
    c=int(input("enter".title()+" "+"the constant:"))
    Quad=Quadratic_Equation(a,b,c,w)
    Quad.initialisation()
else:
    w=input("\nENTER YOUR NAME PLEASE:")
    d=int(input("\nEnter the first coefficient:"))
    a=int(input("Enter the second coefficient:"))
    b=int(input("Enter the third coefficient:"))
    c=int(input("enter".title()+" "+"the constant:"))
    cubic=cubic_equation(a,b,c,w,d)
    gotten=cubic.division()
    Quad=Quadratic_Equation(gotten[0],gotten[1],gotten[2],w)
    Quad.initialisation()
    
     
        


    
        
    
            
    
