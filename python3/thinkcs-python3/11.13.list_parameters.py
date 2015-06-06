'''
11.13. List parameters
Passing a list as an argument actually passes a reference to the list, not a copy or clone of the list. So parameter passing creates an alias for you: the caller has one variable referencing the list, and the called function has an alias, but there is only one underlying list object. For example, the function below takes a list as an argument and multiplies each element in the list by 2:
'''

def double_stuff(a_list):
    for (idx, val) in enumerate(a_list):
        a_list[idx] = 2 * val

things = [2, 5, 8]
double_stuff(things)
print(things)