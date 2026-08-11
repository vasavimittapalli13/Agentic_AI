
name = 'Rahul'
print(type(name))

age = 24
random__value = 40
result = age + random__value
print(result) 

#type casting
final_result = float(random__value)
print(final_result)
print(type(final_result)) # <class 'int'>

test = 56
output = str(test)
print(output) # "56"
print(type(output)) # <class 'str'>

s1 = 23
s2 = 45
s3 = 12
s4 = 67
s5 = 89
s6 = 54
s7 = 34

avg_marks = (s1 + s2 + s3 + s4 + s5 + s6 + s7) / 7
print(avg_marks) # 46.2

marks = [23, 45, 12.4, 67, 89, 34, 34,56, 78, 
         90, 100, 45, 67, 89, 23, 
         45, 67, 89, 34, 56,21,23,99]
print(type(marks)) # <class 'list'>
print(sum(marks)) 
print(len(marks)) 
result = sum(marks) / len(marks)
final_result = round(result,3)
print(final_result) 


sales_data = [23.45, 67.89, 12.34, 56.78, 90.12, 34.56, 78.90, 45.67, 89.01, 23.45]

print(sales_data[8]) 
print(sales_data[-2]) 


avg_odd_day_sales = sum(sales_data[0::2])/len(sales_data[0::2])
avg_even_day_sales = sum(sales_data[1::2])/len(sales_data[1::2])
print(round(avg_odd_day_sales, 2)) 
print(round(avg_even_day_sales, 2)) 

# % compute the %difference
percentage_difference = ((avg_odd_day_sales - avg_even_day_sales) / avg_even_day_sales) * 100
print(round(percentage_difference, 2))
