
# Project 37: Market Price Monitor
# Description: Demonstrates integers, strings, booleans, lists, and arrays in Python

import array

#Integers: quantint and price

prices = [120, 150, 90, 200, 175]   

total = sum(prices)
average = total / len(prices)
minimum = min(prices)
maximum = max(prices)

# Strings: formatted report using f-strings

report = f"""
Total Price: {total}
Average Price: {average:.2f}
Lowest Price: {minimum}
Highest Price: {maximum}
"""
print(report)

#boolean for applying threshold

threshold = 140
if average > threshold and maximum > 180:  
    print(" Status: Above Standard (High Average and High Max Price)")
else:
    print(" Status: Below Standard")

#lists: maintain, add,remove and sort.
items = ["Rice", "Beans", "Maize", "banana", "Sugar"]
print("\nOriginal Items List:", items)

items.append("Coffee")

if "Maize" in items:
    items.remove("Maize")


items.sort()

print("Modified & Sorted Items List are: ", items)

#arrays: fixed-size numerical subset.

price_array = array.array('i', [120, 150, 90, 200, 175]) 
array_sum = sum(price_array)

print("\nArray Sum:", array_sum)
print("List Sum:", total)

if array_sum == total:
    print("  Array and List sums match!")
else:
    print("  Array and List sums do NOT match!")