"""
Even Odd Number Sorter App
Sorts comma-separated numbers into even and odd lists, then displays them in order.

"""
# SETUP AND WELCOME MESSAGE
print("Welcome to my Even Odd Number Sorter App!")  # Welcome message

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
    user_input = user_input.strip(",")  # Remove leading/trailing commas

    # Split input into list and remove empty entries
    num_list = user_input.split(",")
    num_list = [num for num in num_list if num]

    evens = []  # Store even numbers
    odds = []   # Store odd numbers

    #Result summary header
    print("---- Result Summary ----")  # Summary header

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
    # Sort and display even numbers
    evens.sort()
    print(f"\nThe following {len(evens)} numbers are even:")
    for even in evens:
        print(even)

    # Sort and display odd numbers
    odds.sort()
    print(f"\nThe following {len(odds)} numbers are odd:")
    for odd in odds:
        print(odd)

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
print(r"""
      .-''''-.
     /        \
    /_        _\
   // \      / \\
   |\__\    /__/|
    \    ||    /
     \        /
      \  __  /
       '.__.'
        |  |
        |  |
        |  |
        |  |
      __|  |__
     /__|  |__\
Even Odd Sorting
""")

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
