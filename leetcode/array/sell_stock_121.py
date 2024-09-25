

# def sort(d):
#     sorted_dict = dict(sorted(d.items(), key=lambda item: item[1]))
#     return sorted_dict

# def maxProfit(prices) -> int:
#     n = len(prices)
#     price_map = {}
#     for i in range(0,n):
#         price_map[i] = prices[i]
        
#     sort_price_map = sort(price_map)
#     maxx = 0
#     print(sort_price_map)
#     for i in range(0,n):
#         j = i+1
#         while sort_price_map.get(j,0) > price_map[i]:
            
#             diff = sort_price_map.get(j) - price_map[i]
#             print(j)
#             maxx = max(maxx,diff)
#             j+=1
        
#     print(maxx)


def maxProfit(prices) -> int:
    if not prices:
        return 0
    
    min_price = prices[0]
    max_profit = 0
    
    for price in prices:
        if price < min_price:
            min_price = price
        
        profit = price - min_price
        
        max_profit = max(max_profit,profit)
            
    print(max_profit)
    return max_profit



# 7,1,5,3,6,4

# p = 7
# min_p = 7
# profit = 7-7 = 0
# max_p = 0

# p = 1
# min_p = 1
# profit = 0
# max_p = 0

# p = 5
# min_p = 1
# profit = 5-1 = 4
# max_profit = 4


# p = 3
# min_p = 1
# profit = 3-1 = 2
# max_profit = 4

# p = 6
# min_p = 1
# profit = 6-1 = 5
# max_profit = 5

# p = 4
# min_p = 1
# profit = 4-1 = 3
# max_profit = 5

prices = [7,1,5,3,6,4]
maxProfit(prices)
# {2: 1, 4: 3, 6: 4, 3: 5, 5: 6, 1: 7}

# [7,1,5,3,6,4]