import numpy as n 

print("Hello, what values do you know? For the value you need to find, type x in it's place.")
print()

u = input("What is the initial velocity:")
print(u)
v = input ("What is the final velocity:")
print(v)
a = input("What is the acceleration:")
print(a)
t = input ("What is the time taken:")
print(t)
s = input ("What is the displacement:")
print(s)
print()

if (u = x and s = x):

    choice_1 = input("Which value do you want to find?: ")
    print(choice_1)
    if (choice_1 = u):
        print("calculating intial velocity....")
        intial_velocity_1 = v - a*t
        print()
        print ("The intial velocity is " + intial_velocity_1)
    elif (choice_1 = s):
        print ("calculating displacement.....")
        displacement_1 = intial_velocity_1*t + (1/2)*a*(t)^2
        print()
        print("The displacement is:" + displacement_1)
    else:
        print ("Please rerun the code, you've selected a wrong quantity!")

     

elif (u = x and t = x): 
    choice_2 = input("Which value do you want to find: ")
    print(choice_2)
    if (choice_2 = u):
        print("calculating intial velocity....")
        intial_velocity_2 = v - a*t
        print()
        print ("The intial velocity is " + intial_velocity_2)
    else:
        print ("Please rerun the code, you've selected a wrong quantity!")

elif (v = x and t=x):
    print ("So the final velocity is unknown")
    print("So the initial velocity is " + u + "m/s")
    print("So the acceleration is " + a + "m/s^2")
    print("So the time  is " + t + "s")
    print("So the displacement is " + s + "m")
    print()
    print("calculating final velocity....")
    final_velocity = u + a*t
    print()
    print ("The final velocity is " + final_velocity)

elif a = x 
