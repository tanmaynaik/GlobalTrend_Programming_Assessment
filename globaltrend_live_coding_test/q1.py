'''Write a function to find the longest common subsequence of two given strings
Sample Test Case
Input: str1 = "abcde", str2 = "ace" Output: 3 (The LCS is "ace")'''

def longest_subsequence(s1,s2):
    m = len(s1)
    n = len(s2)
    arr1 = [[0] * (n+1) for _ in range(m+1)]

    for i in range(1, m+1):
        for j in range(1, n+1):
            if s1[i-1] == s2[j-1]:
                arr1[i][j] = arr1[i-1][j-1] + 1
            else:
                arr1[i][j] = max(arr1[i-1] [j], arr1[i][j-1])
    return arr1[m][n]


#Output
str1 = "abcde"
str2 = "ace"
print(longest_subsequence(str1,str2))
