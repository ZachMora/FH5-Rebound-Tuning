
#Base Tune 
def main():
     #log in
    passcode = int(input("Enter subscription key please "))  
    if passcode == 123:
     print("Welcome to the pre-alpha. Tunes for FH5 only.")

    else:
     print("Oops, that code isn't valid. Please try again or wait for the full verison. -Zach")
     main()

    #front rebound tune
    
    initial_front_bump_stiffness = float(input("Enter front bump stiffness "))
   
    fifty_percent_front = initial_front_bump_stiffness *.5
   
    seventy_five_percent_front = initial_front_bump_stiffness *.75

    final_front_rebound = (fifty_percent_front + seventy_five_percent_front) // 2

    print("Your base tune front rebound is " + (str(final_front_rebound)) )
   
    #Rear rebound tune

    initial_rear_bump_stiffness = float(input("Enter rear bump stiffness "))
    
    fifty_percent_rear = initial_rear_bump_stiffness *.5
   
    seventy_five_percent_rear = initial_rear_bump_stiffness *.75

    final_rear_rebound = (fifty_percent_rear + seventy_five_percent_rear) // 2

    print("Your base tune rear rebound is " + (str(final_rear_rebound)) )

    #Disclaimer 

    print("Calculated values may require further adjustments")
    
    #Reset
    reset = (input("Would you like to restart? "))
    if reset == "yes":
        main()
    else:
        print("Thanks for trying the calculator out.")
main()