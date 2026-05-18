'''Create a tuple named product containing the following items: "Laptop", 50000, Black ,'Samsung' and "Electronics". Print the tuple.
Access and print the second element of the tuple product.
Slice and print the last two elements of the product tuple.
Check whether "Electronics" is present in the product tuple and print a message.
Create a tuple of 5 product prices: (1000, 1500, 1200, 1100, 900). Count how many times 1000 appears.
Find and print the maximum and minimum price from the prices tuple.
Use a loop to print each item from the product tuple on a new line.
Convert the product tuple to a list. Change the price to 55000, then convert it back to a tuple. Print the updated tuple.
Add a new item "In Stock" to the product tuple (simulate adding by concatenation).
Remove "Electronics" from the product tuple (by converting to list, removing, and converting back).
Unpack the tuple product into three variables and print each variable.
Create a nested tuple that contains three product tuples inside it. Access and print the name of the second product in the nested tuple'''

product = ("Laptop", 50000, "Black", 'Samsung', "Electronics")
print("Product tuple:", product)

print("Second element of the product tuple:", product[1])

print("Last two elements of the product tuple:", product[-2:])
if "Electronics" in product:
    print("ELECTRONICS is present in the product tuple.")

prices = (1000, 1500, 1200, 1100, 900)
print("Count of 1000 in prices tuple:", prices.count(1000))

print("Maximum price:", max(prices))
print("Minimum price:", min(prices))

for item in product:
    print("Item:", item)

product_list = list(product)
product_list[1] = 55000

product = tuple(product_list)
print("Updated(price) in product tuple:", product)

product = product+("In Stock",)
print("Product tuple after adding 'In Stock':", product)

p_list=list(product)
p_list.remove("Electronics")
product = tuple(p_list)
print("Product tuple after removing 'Electronics':", product)

name, price, color, *rest = product
print("Unpacked values - \nName:", name)
print("Price:", price) 
print("Color:", color)

product_nested = (("Laptop", 50000, "Black"), ("Smartphone", 30000, "White"), ("Tablet", 20000, "Gray"))
#print("Nested product tuple:", product_nested)
print("Second product name in nested tuple:", product_nested[1][0])

