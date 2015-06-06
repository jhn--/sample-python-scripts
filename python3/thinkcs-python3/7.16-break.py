'''
use break to leave the loop
'''

total = 0
while True:
    response = input("Enter a number. (Leave blank to exit) ")
    if response == "":
        break
    total += int(response)
print("The total of the numbers you have entered: ", total)