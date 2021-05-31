#List for the pizza toppings 
toppings=['pepperoni','pineapple','cheese','sausage','olives','anchovies','mushrooms']

#list for the prices 
prices=['2','6','1','3','2','7','2']

#find the length of the toppings list and store it in num_pizzas

num_pizzas=len(toppings)

#print we sell x different kinds of pizzas 
print("we sell", num_pizzas, "different kinds of pizza!")

#Combine the two lists into a list called pizzas 
pizzas = list(zip(prices,toppings))


#Sort pizzas with the lowest at the start of the list 
pizzas.sort()

#Store the first element of pizzas in a variable called:
cheapest_pizza=pizzas[0]

#most expensive pizza 
priciest_pizza=pizzas[6]

#Cheapest Pizza 
three_cheapest=pizzas[0:3]

#occurence of 2 dollar slices 
num_two_dollar_slices=prices 
substring = '2'
count=num_two_dollar_slices.count(substring)
print(count)