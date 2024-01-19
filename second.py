def helper(T, test_cases):
    result = []

    for i in test_cases:
        N, K, heights = i
        count = sum(1 for j in heights if j > K)
        result.append(count)
    return result

T = int(input("Enter the number of test cases: "))
test_cases = []

for i in range(T):
    N, K = map(int, input("Enter N and K values: ").split())
    heights = list(map(int, input("Enter heights: ").split()[:N]))
    test_cases.append((N, K, heights))

output = helper(T, test_cases)
for op in output:
    print(op)

# Explanation:
# helper Function:- This function takes the number of test cases (T) and a list of test cases (test_cases). 
#                   For each test case,it counts the number of heights greater than K and appends the count to the result list.
#                   Finally, it returns the list of counts.

# Taking Input:-  The code prompts the user to input the number of test cases (T). 
#                It then iterates through each test case,taking inputs for N, K, and a list of heights.

# Calling the Helper Function:- The helper function is called with the number of test cases and the list of test cases.

# Results:- The code prints the count of heights greater than K for each test case.