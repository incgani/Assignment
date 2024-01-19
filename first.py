def converter(number):
    s = str(number)
    l = []

    for x in range(-3, -len(s), -2):
        l.append(s[x - 2:x])
    l = l[::-1]
    result = ",".join(l + [s[-3:]])

    return result

n = int(input("Enter a number: "))
output=converter(n)
print(output)

# Explanation:

# The converter function takes an integer input, converts it to a string,and then formats 
# it using commas as separators to represent the number in a more readable way.

# s = Here i used str(number) which converts the number to a string.

# l = [] creating an empty list to store groups of digits.

# The for loop iterates through the string  starting from the end (-3),
# moving backwards (-2 steps at a time) until the string is exhausted (-len(s)).
# Each two-digit group is appended to the list l.

# l = (By using slicing method l[::-1]). Reverse the list to get the correct order of groups.

# result = ",".join(l + [s[-3:]]): Joins the groups with commas and adds 
# the remaining three digits to the end.

# Then result returned to the functioncall.where functioncall stored in output variable.

# By using print keyword we print the values.
