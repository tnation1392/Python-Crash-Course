#import the get formatted name function
from names_function import get_formatted_name

#Create a loop to continuously enter first and last names
#add an exit strategy of typing q
print("Enter 'q' to quit.")
while True:
    first_name = input("\nEnter first name: ")
    if first_name == 'q':
        break
    last_name = input("Enter last name: ")
    if last_name == 'q':
        break

#Call the function in the variable and print the results
    formatted_name = get_formatted_name(first_name, last_name)
    print(f"\nNeatly formatted name: {formatted_name}.")
