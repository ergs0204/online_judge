# n=int(input())

# def buy(n1,n3,n10):
#     if n10>=1:
#         return 1,n1+2,n5,n10-1
#     elif 0<n5<=c:
#         # print("mmm")
#         return 4,n1-3,n5-1,n10
#     elif n5>=2:
#         # print("abc")
#         return 2,n1+2,n5-2,n10
#     elif n5:
#         # print("hi")
#         return 4,n1-3,n5-1,n10
#     else:
#         return 8,n1-8,n5,n10
# for _ in range(n):
#     c,n1,n5,n10=map(int,input().split())
#     used=0
#     while c>0:
#         c-=1
#         a,n1,n5,n10=buy(n1,n5,n10)
#         used+=a
#     print(used)

# def min_coins_to_buy_coke(cokes, n1, n5, n10):
#     usage_data={}
#     def dfs(remaining_cokes, coins1, coins5, coins10, used_coins):
#         if remaining_cokes == 0:
#             return used_coins
        
#         min_coins = float('inf')
        
#         # Try using a 10-crown coin
#         if coins10 > 0:
#             change = 2
#             if (remaining_cokes - 1, coins5, coins10 - 1) in usage_data:
#                 min_coins=min(min_coins,usage_data[(remaining_cokes - 1, coins5, coins10 - 1)])
#             else:
#                 min_coins = min(min_coins, dfs(remaining_cokes - 1, coins1 + change, coins5, coins10 - 1, used_coins + 1))
#             usage_data[(remaining_cokes - 1, coins5, coins10 - 1)]=min_coins
#         # Try using two 5-crown coins
#         if coins5 >= 2:
#             change = 2
#             if (remaining_cokes - 1, coins5 - 2, coins10) in usage_data:
#                 min_coins=min(min_coins,usage_data[(remaining_cokes - 1, coins5 - 2, coins10)])
#             else:
#                 min_coins = min(min_coins, dfs(remaining_cokes - 1, coins1 + change, coins5 - 2, coins10, used_coins + 2))
#             usage_data[(remaining_cokes - 1, coins5 - 2, coins10)]=min_coins
#         # Try using one 5-crown coin and three 1-crown coins
#         if coins5 >= 1 and coins1 >= 3:
#             if (remaining_cokes - 1, coins5 - 1, coins10) in usage_data:
#                 min_coins=min(min_coins,usage_data[(remaining_cokes - 1, coins5 - 1, coins10)])
#             else:
#                 min_coins = min(min_coins, dfs(remaining_cokes - 1, coins1 - 3, coins5 - 1, coins10, used_coins + 4))
#             usage_data[(remaining_cokes - 1, coins5 - 1, coins10)]=min_coins
#         # Try using eight 1-crown coins
#         if coins1 >= 8:
#             if (remaining_cokes - 1, coins5, coins10) in usage_data:
#                 min_coins=min(min_coins,usage_data[(remaining_cokes - 1, coins5 , coins10)])
#             else:
#                 min_coins = min(min_coins, dfs(remaining_cokes - 1, coins1 - 8, coins5, coins10, used_coins + 8))
#             usage_data[(remaining_cokes - 1, coins5 - 1, coins10)]=min_coins
#         print(usage_data)
#         return min_coins
    
#     return dfs(cokes, n1, n5, n10, 0)

# # Read input
# num_cases = int(input())
# for _ in range(num_cases):
#     cokes, n1, n5, n10 = map(int, input().split())
#     result = min_coins_to_buy_coke(cokes, n1, n5, n10)
#     print(result)

def min_coins_to_buy_coke(cokes, n1, n5, n10):
    # Initialize the DP table
    # dp[i][j][k] represents the minimum number of coins needed
    # to buy i cokes with j 5-crown coins and k 10-crown coins remaining
    dp = [[[float('inf')] * (n10 + 1) for _ in range(n5 + 1)] for _ in range(cokes + 1)]
    
    # Base case: 0 cokes bought
    for j in range(n5 + 1):
        for k in range(n10 + 1):
            dp[0][j][k] = 0
    
    # Fill the DP table
    for i in range(1, cokes + 1):
        for j in range(n5 + 1):
            for k in range(n10 + 1):
                # Option 1: Use 8 1-crown coins
                dp[i][j][k] = min(dp[i][j][k], dp[i-1][j][k] + 8)
                
                # Option 2: Use 1 5-crown coin and 3 1-crown coins
                if j > 0:
                    dp[i][j][k] = min(dp[i][j][k], dp[i-1][j-1][k] + 4)
                
                # Option 3: Use 2 5-crown coins
                if j > 1:
                    dp[i][j][k] = min(dp[i][j][k], dp[i-1][j-2][k] + 2)
                
                # Option 4: Use 1 10-crown coin
                if k > 0:
                    dp[i][j][k] = min(dp[i][j][k], dp[i-1][j][k-1] + 1)
    
    return dp[cokes][n5][n10]

# Read input
num_cases = int(input())
for _ in range(num_cases):
    cokes, n1, n5, n10 = map(int, input().split())
    result = min_coins_to_buy_coke(cokes, n1, n5, n10)
    print(result)