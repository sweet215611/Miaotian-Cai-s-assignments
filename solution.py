# Sales Data Analysis - 2023

## Problem Statement As a data analyst for a computer retail company, I was asked to find the consecutive months in 2023 that contributed the highest sales. This is to help guide advertising strategies targeting high-revenue periods.

## Approach - We used a sliding window algorithm to calculate the total sales over all consecutive 2-month and 3-month periods. - The months with the highest cumulative sales were then selected.

## Result **Best Months:** January, February, March   **Total Sales:** 323 million USD
months = [
    "Jan", "Feb", "Mar", "Apr", "May", "Jun",
    "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"
]
sales = [100, 113, 110, 85, 81, 101, 94, 106, 105, 102, 86, 63]

def find_max_consecutive_sales(months, sales, window_size=2):
    max_sum = 0
    max_range = (0, 0)
    for i in range(len(sales) - window_size + 1):
        current_sum = sum(sales[i:i+window_size])
        if current_sum > max_sum:
            max_sum = current_sum
            max_range = (i, i+window_size-1)
    return max_range, max_sum

best_2_months, sum_2 = find_max_consecutive_sales(months, sales, 2)
best_3_months, sum_3 = find_max_consecutive_sales(months, sales, 3)

if sum_2 >= sum_3:
    best_months = months[best_2_months[0]:best_2_months[1]+1]
    best_sum = sum_2
else:
    best_months = months[best_3_months[0]:best_3_months[1]+1]
    best_sum = sum_3

print("Best consecutive months with highest sales:", best_months)
print("Total sales during this period (in millions):", best_sum)
