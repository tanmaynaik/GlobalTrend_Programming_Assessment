'''Write a function to solve the 0/1 Knapsack problem using dynamic programming.
Sample Test Case
Input: weights = [1, 2, 3], values = [10, 15, 40], capacity = 6 Output: 55 (Maximum value that can be obtained)'''
def knapsack(weights, values, capacity):
    n = len(values)
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(values[i - 1] + dp[i - 1][w - weights[i - 1]], dp[i - 1][w])
            else:
                dp[i][w] = dp[i - 1][w]

    return dp[n][capacity]

#Output
weights = [1, 2, 3]
values = [10, 15, 40]
capacity = 6
max_value = knapsack(weights, values, capacity)
print("Maximum value:", max_value)