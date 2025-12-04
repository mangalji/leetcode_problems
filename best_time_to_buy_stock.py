prices = [7,1,5,3,6,4]

max_profit = 0

# min_price = float("inf")
min_price = max(prices)

#you also can do both steps to put the value of min_price

n = len(prices)

for i in range(0,n):
	min_price = min(min_price,prices[i])
	# print(min_price)
	max_profit = max(max_profit,prices[i]-min_price)

print(max_profit)

