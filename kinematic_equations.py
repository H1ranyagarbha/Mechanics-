import time

def kinematic_equations():
    time.sleep(1)
    print("Hello, what physical kinematic quantities do you know the value of? For the value(s) you need to find, type -69 in its place.")
    print()
    time.sleep(1)

    u = float(input("What is the initial velocity:"))
     time.sleep(1)
    v = float(input("What is the final velocity:"))
     time.sleep(1)
    a = float(input("What is the acceleration:"))
     time.sleep(1)
    t = float(input("What is the time taken:"))
     time.sleep(1)
    s = float(input("What is the displacement:"))
     time.sleep(1)
    print()

    if u == -69 and s == -69:
        time.sleep(1)
        choice_1 = input("Which value do you want to find? initial velocity or displacement: ")
        print(choice_1)
        if choice_1 == "initial velocity":
            print("calculating intial velocity....")
            initial_velocity_1 = float(v - a*t)
            time.sleep(1)
            v_1 = v - a*t
            print()
            print ("The initial velocity is " + str(initial_velocity_1) + "m/s")
        elif choice_1 == "displacement":
            print ("calculating displacement.....")
            time.sleep(1)
            displacement_1 = float(initial_velocity_1*t + (1/2)*a*(t)^2)
            print()
            print("The displacement is:" + str(displacement_1) + "m")
        else:
            print ("Please rerun the code, you've selected a wrong quantity!")



    elif u == -69 and t == -69:
        time.sleep(1)
        choice_2 = input("Which value do you want to find, initial velocity or time: ")
        print(choice_2)
        if choice_2 == "initial velocity":
            print("calculating intial velocity....")
            time.sleep(1)
            intial_velocity_2 = float(v - a*t)
            print()
            print ("The intial velocity is " + str(intial_velocity_2) + "m/s")
        else:
            print ("Please rerun the code, you've selected a wrong quantity!")


    elif v == -69 and t == -69:
        time.sleep(1)
        choice_3 = input("Which value do you want to find, final velocity or time: ")
        print(choice_3)
        if choice_3 == "final velocity":
            print("calculating final velocity....")
            time.sleep(1)
            final_velocity_1 = float((u^2 + 2*a*s)^(1/2))
            print()
            print ("The final velocity is " + str(final_velocity_1) + "m/s")
        elif choice_3 == "time":
            print ("calculating time taken....")
            time.sleep(1)
            print()
            time_1 = float((final_velocity_1 - u)/a)
            print("The time taken is " + str(time_1) + "s")
        else:
            
            print("Please rerun the code, you've selected a wrong quantity!")

    elif v==-69 and s==-69:
        time.sleep(1)
        choice_4 = input("Which value do you want to find: ")
        print(choice_4)
        if choice_4 == "final velocity":
            print("calculating final velocity....")
            time.sleep(1)
            print()
            final_velocity_2 = float(u + a*t)
            print("The final velocity is " + str(final_velocity_2) + "m/s")
        elif choice_4 == "displacement": 
            print("calculating displacement....")
            time.sleep(1)
            print()
            displacement_2 = float(u*t + 1/s*a*t^2)
            print("The displacement is " + str(displacement_2) + "m")
        else:
            print("Please rerun the code, you've selected a wrong quantity!")



    elif a == -69 and s == -69:
        time.sleep(1)
        choice_5 = input("Which value do you want to find, acceleration or displacement: ")
        print(choice_5)
        if choice_5 == "acceleration":
            
            print("calculating acceleration....")
            time.sleep(1)
            print()
            acceleration_1 = float((v-u)/t)
            print("The acceleration is " + str(acceleration_1) + "m/s^2")
        elif choice_5 == "displacement":
             print ("calculating displacement....")
             time.sleep(1)
             print()
             displacement_3 = float(u*t + (1/2)*a*t^2)
             print("The displacement is:" + str(displacement_3) + "m")
        else:
            print("Please rerun the code, you've selected a wrong quantity!")

    elif a == -69 and t == -69:
        time.sleep(1)
        choice_6 = input("Which value do you want to find, acceleration or time taken?: ")
        print(choice_6)
        if choice_6 == "acceleration" :
            time.sleep(1)
            print("calculating acceleration....")
            print()
            time.sleep(1)
            acceleration_2 = float((v^2 - u^2)/(2*s))
            print("The acceleration is " + str(acceleration_2) + "m/s^2")
        elif choice_6 == "time":
            time.sleep(1)
            print("calculating time taken....")
            time.sleep(1)
            print()
            time_2= float((v - u)/a)
            print("The time taken is:" + str(time_2) + "s")
        else:
            time.sleep(1)
            print("Please rerun the code, you've selected a wrong quantity!")

    elif u == -69:
        initial_velocity_3 = float(v - a*t)
        time.sleep(1)
        print("The initial velocity is:" + str(intial_velocity_3) + "m/s")

    elif s == -69:
        displacement_4 = float(u*t + 1/2*a*t^2)
        time.sleep(1)
        print("The displacement is:" + str(displacement_4) + "m")
    elif v == -69:
        final_velocity_3 = float(u + a*t)
        time.sleep(1)
        print("The final velocity is:" + str(final_velocity_3) + "m/s")
    elif a == -69:
        acceleration_3 = float((v - u)/t)
        time.sleep(1)
        print("The acceleration is:" +  str(acceleration_3) + "m/s^2")
    elif t == -69:
        time_4 = float((v-u)/a)
        time.sleep(1)
        print("The time taken is:" + str(time_4) + "s")

    else:
        time.sleep(1)
        print("ERROR, rerun code!")

kinematic_equations()
time.sleep(1)
print ("This was written by #Nosferatu4066, if you found any errors, please contact me!")
