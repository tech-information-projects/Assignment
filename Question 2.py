t = int(input("How many test cases do you have? "))

test_cases = []

for no in range(t):
    print(f"Enter the values for test case {no+1}:")

    N, K = map(int, input("Enter no of players between Gi-Hun and Ali and their height:").split())

    heights = []
    for p_no in range(N):
        height = int(input(f"Enter the height of player {p_no+1}: "))
        heights.append(height)

    test_cases.append((N, K, heights))



def Gi_Hun_Ali(t, test_cases):
    result = []
    for c in test_cases:
        N, K = c[0], c[1]
        heights = c[2]
        count = 0
        for height in heights:
            if height > K:
                count += 1
        result.append(count)
    return result


output = Gi_Hun_Ali(t, test_cases)
for i in output:
    print(i)