# Conditional if/else logic- these are keywords that instruct your
# Program to do specific instructions based on specific data
# or conditions

# conditiional syntax (how it is written)
bill_amount = int(input( Please type in a bill tender (1s ,5s, or 10s): "))

# is usally indicates that something is a posssible option
if bill_amount == 1:
    print("here are 4 quaters")
    # else is Always your last option.
    else:
        print("sorry that type of bill is not accepted. ")

        # elif allows us to indicate that there are more posible options
        # you can have as many elif as you want
        elif bill_amount == 5:
            print("here are 20 quaters")

            elif bill_amount == 10:
                print ("here are 40 quaters")

                elif bill_amount == 20:
                    print("sorry we do not accepts 20s.please enter an accepted amount")

                    elif bill_amount == 50:
                        print("sorry we do not accepts 50s. please enter an accpted amount")

                        elif bill_amount == 100:
                            print ("sorry we do not accepts 100s. please enter an accepted amount")
                            # elese is always your last option
                            else: ("sorry that type of bill is not accpted.")

   # create a calulator function that uses if/else logic to
   # allow the user
   # to change or select differnt arithmetic operations. 
   # additon, 2 will do subtaction
   # 3 will so multiplication and 4 divison 

elif choice == '2':
            result = num1 - num2
            print(f"The result of subtraction is: {result}")
            
        elif choice == '3':
            result = num1 * num2
            print(f"The result of multiplication is: {result}")
            
        elif choice == '4':
            # Handle potential division by zero error
            if num2 == 0:
                print("Error: Division by zero is not allowed.")
            else:
                result = num1 / num2
                print(f"The result of division is: {result}")
    else:
        print("Invalid Input. Please select a valid operation (1-4).")

if selction == 1:
    calculate_add()
elif selction == 2:
    calculate_subtract()
elif selction == 3:
    calculate_multiply()
elif selction == 4:
    calculate_divide ()
    else: print("sorry somthing went wrong")

  # 1. Under 4 years old: Free
    if age < 4:
        price = 0.00
    
    # 2. Ages 4 to 12: Child price ($8.00)
    elif age <= 12:
        price = 8.00
        
    # 3. Ages 13 to 64: Standard Adult price ($15.00)
    elif age <= 64:
        price = 15.00
        
    # 4. Ages 65 and older: Senior discount ($10.00)
    else:
        price = 10.00



        def check_trip_eligibility(permission_slip, gpa):
    if permission_slip == True and gpa > 90:
        print("Confirmed: You can go on the trip!")
    elif permission_slip == False and gpa > 90:
        print("You have a free day!")
    else:
        print("You will attend regular classes.")
        

