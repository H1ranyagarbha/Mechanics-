def kinematic_equations():

    print("Hello, what values do you know? For the value you need to find, type -69 in its place.")
    print()

    u = float(input("What is the initial velocity:"))
    print(u)
    v = float(input("What is the final velocity:"))
    print(v)
    a = float(input("What is the acceleration:"))
    print(a)
    t = float(input("What is the time taken:"))
    print(t)
    s = float(input("What is the displacement:"))
    print(s)
    print()

    if u == -69 and s == -69:

        choice_1 = input("Which value do you want to find?: ")
        print(choice_1)
        if choice_1 == u:
            print("calculating intial velocity....")
            initial_velocity_1 = float(v - a*t)
            v_1 = v - a*t
            print()
            print ("The initial velocity is " + initial_velocity_1 + "m/s")
        elif choice_1 == s:
            print ("calculating displacement.....")
            displacement_1 = float(initial_velocity_1*t + (1/2)*a*(t)^2)
            print()
            print("The displacement is:" + displacement_1 + "m")
        else:
            print ("Please rerun the code, you've selected a wrong quantity!")



    elif u == -69 and t == -69:
        choice_2 = input("Which value do you want to find: ")
        print(choice_2)
        if choice_2 == u:
            print("calculating intial velocity....")
            intial_velocity_2 = float(v - a*t)
            print()
            print ("The intial velocity is " + intial_velocity_2 + "m/s")
        else:
            print ("Please rerun the code, you've selected a wrong quantity!")


    elif v == -69 and t == -69:
        choice_3 = input("Which value do you want to find: ")
        print(choice_3)
        if choice_3 == v:
            print("calculating final velocity....")
            final_velocity_1 = float((u^2 + 2*a*s)^(1/2))
            print()
            print ("The final velocity is " + final_velocity_1 + "m/s")
        elif choice_3 == t:
            print ("calculating time taken....")
            print()
            time_1 = float((final_velocity_1 - u)/a)
            print("The time taken is " + time_1 + "s")
        else:
            print("Please rerun the code, you've selected a wrong quantity!")

    elif v==-69 and s==-69:
        choice_4 = input("Which value do you want to find: ")
        print(choice_4)
        if choice_4 == v:
            print("calculating final velocity....")
            print()
            final_velocity_2 = float(u + a*t)
            print("The final velocity is " + final_velocity_2 + "m/s")
        elif choice_4 == s: 
            print("calculating displacement....")
            print()
            displacement_2 = float(u*t + 1/s*a*t^2)
            print("The displacement is " + displacement_2 + "m")
        else:
            print("Please rerun the code, you've selected a wrong quantity!")



    elif a == -69 and s == -69:
        choice_5 = input("Which value do you want to find: ")
        print(choice_5)
        if choice_5 == a:
            print("calculating acceleration....")
            print()
            acceleration_1 = float((v-u)/t)
            print("The acceleration is " + acceleration_1 + "m/s^2")
        elif choice_5 == s:
             print ("calculating displacement....")
             print()
             displacement_3 = float(u*t + (1/2)*a*t^2)
             print("The displacement is:" + displacement_3 + "m")
        else:
            print("Please rerun the code, you've selected a wrong quantity!")

    elif a == -69 and t == -69:
        choice_6 = input("Which value do you want to find: ")
        print(choice_6)
        if choice_6 == a :
            print("calculating acceleration....")
            print()
            acceleration_2 = float((v^2 - u^2)/(2*s))
            print("The acceleration is " + acceleration_2 + "m/s^2")
        elif choice_6 == t:
            print("calculating time taken....")
            print()
            time_2= float((v - u)/a)
            print("The time taken is:" + time_2 + "s")
        else:
            print("Please rerun the code, you've selected a wrong quantity!")

    elif u == -69:
        initial_velocity_3 = v - a*t
        print("The initial velocity is:" + intial_velocity_3 + "m/s")

    elif s == -69:
        displacement_4 = float(u*t + 1/2*a*t^2)
        print("The displacement is:" + displacement_4 + "m")
    elif v == -69:
        final_velocity_3 = float(v - a*t)
        print("The final velocity is:" + final_velocity_3 + "m/s")
    elif a == -69:
        acceleration_3 = float((v - u)/t)
        print("The acceleration is:" +  acceleration_3 + "m/s^2")
    elif t == -69:
        time_4 = float((v-u)/a)
        print("The time taken is:" + time_4 + "s")

    else:
        print("ERROR, rerun code")

kinematic_equations()
