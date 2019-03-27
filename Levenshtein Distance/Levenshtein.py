def Levenshtein(str1, str2):
  m = len(str1) + 1
  n = len(str2) + 1

  dp = [[0 for _ in range(n)] for _ in range(m)]
  for i in range(m):
    dp[i][0] = i
  for j in range(n):
    dp[0][j] = j

  for i in range(1, m):
    for j in range(1, n):
      if (str1[i-1] == str2[j-1]):
        dp[i][j] = dp[i-1][j-1]
      else:
        dp[i][j] = 1 + min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1])
  
  return dp[m-1][n-1]

word1 = "horse"
word2 = "ros"
print(Levenshtein(word1, word2))

word1 = "intention"
word2 = "execution"
print(Levenshtein(word1, word2))
