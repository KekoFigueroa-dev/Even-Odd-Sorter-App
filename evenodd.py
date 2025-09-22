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
    break




    # ------------------------------------------
    # SORT AND DISPLAY RESULTS
    # ------------------------------------------

    # TODO: Sort the evens list numerically

    # TODO: Sort the odds list numerically

    # TODO: Display even numbers with count
    # Format: "The following [count] numbers are even:"
    # Then print each even number on its own line

    # TODO: Display odd numbers with count
    # Format: "The following [count] numbers are odd:"
    # Then print each odd number on its own line


    # ------------------------------------------
    # CONTINUATION PROMPT
    # ------------------------------------------

    # TODO: Ask user if they want to run program again

    # TODO: Check user response
    # If they don't want to continue:
        # TODO: Set active flag to False
        # TODO: Print goodbye message


# ==========================================
# PROGRAM STRUCTURE NOTES
# ==========================================
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
