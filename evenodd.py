"""
Even Odd Number Sorter App
Sorts comma-separated numbers into even and odd categories, then displays them in numerical order.

"""
# SETUP AND WELCOME MESSAGE
print("Welcome to my Even Odd Number Sorter App!")
#active flag variable to control main program loop
active = True

# MAIN PROGRAM LOOP
# TODO: Create while loop using the active flag
while active:
    # USER INPUT AND STRING CLEANING
    user_input = input("Please enter comma-separated numbers: ")
    unwanted_chars = [" ",".","!","@","#","$","%","^","&","*",
                                    "(",")","-","_","+","=","{","}","[","]","|","\\",
                                    ":",";","'","\"", "<",">","/","?"]
    for char in unwanted_chars:
        user_input = user_input.replace(char, ",")
    user_input = user_input.strip(",")                                    
    # Removes all spaces, punctuation and special characters using .replace()
    num_list = user_input.split(",") # Converts string to list using .split(",")
    # INITIALIZE STORAGE LISTS
    evens = []
    odds = []
    #Result summary header
    print("---- Result Summary ----")
    #Sort odds and evens
    for number in num_list:
        num = int(number)
        if num % 2 == 0:
            evens.append(num)
            print(f"{num} is even!")
        else:
            odds.append(num)
            print(f"{num} is odd!")
    # SORT AND DISPLAY RESULTS
    evens.sort()
    odds.sort()
    # Display even numbers with count
    print(f"\nThe following {len(evens)} numbers are even:")
    for even in evens:
        print(even)

    # Display odd numbers with count
    print(f"\nThe following {len(odds)} numbers are odd:")
    for odd in odds:
        print(odd, end="\n")
    # CONTINUATION PROMPT
    user_response = input("\nDo you want to sort another list? (yes/no): ").strip().lower()
    if user_response == "yes":
        continue
    elif user_response == "no":
        active = False
    else:
        print("Invalid response. Please enter 'yes' or 'no'.")
# EXIT MESSAGE
print("Thank you for using my Even Odd Number Sorter App! Goodbye!")
    


"""
Key Python concepts used:
- String methods: .replace() and .split()
- Type conversion: int() casting
- List operations: .append() and .sort()
- Modulo operator (%) for even/odd detection
- List length with len()
- While loops with flag control

Data processing pipeline:
Input String → Clean Spaces → Split to List → Convert & Categorize → Sort → Display
"""
