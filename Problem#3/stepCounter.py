def feet_to_steps(user_feet):
   return(user_feet/2.5)

if __name__ == '__main__':
    #take input feet steps here
    #store it into the function
    user_feet = float(input()) 
    #print your steps here
    print(int(feet_to_steps(user_feet)))