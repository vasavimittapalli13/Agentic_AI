marks = [85, 90, 78, 92, 88]
print(marks[0])


sales_data = [100, 200, 150, 300, 250, 340, 213, 125]
avg_odd_day_sales = sum(sales_data[1::2])/ len(sales_data[1::2])
print(avg_odd_day_sales)

avg_even_day_sales = sum(sales_data[0::2])/ len(sales_data[0::2])
print(avg_even_day_sales)

if avg_odd_day_sales > avg_even_day_sales:
    print('Average sales on odd days are higher')
else:
    print('Average sales on even days are higher')


def test(x,y):
    z = x + y
    return z

print(test(4,7))


def sales_comparison(sales_data):
    if len(sales_data) < 2:
        return "Not enough data to compare"
    avg_odd_day_sales = sum(sales_data[1::2])/ len(sales_data[1::2])
    avg_even_day_sales = sum(sales_data[0::2])/ len(sales_data[0::2])
    if avg_odd_day_sales > avg_even_day_sales:
        return 'Odd days are performing better'
    elif avg_even_day_sales > avg_odd_day_sales:
        return 'Even days are performing better'
    else:
        return 'Both are performing equally well'

print(sales_comparison([100, 200, 150, 300, 250, 340, 213, 125]))


toxic_text = 'You are very Bad person, I really hate you'

if 'bad' in toxic_text.lower():
    print('Toxic content detected')

template = """
Classify the below email
{email_content}
"""

prompt = template.format(email_content = 'I am facing the login issue with the application.')
print(prompt)

template = """
Classify the below email
Subject : {sub}
Body : {body}
"""

prompt = template.format(sub = 'Login Issue', body = 'I am facing the login issue with the application.')
print(prompt)

for i in [23,34,56]:
    if i == 34:
        print("Found 34")
    print(i)

for i in [23,34,56]:
    if i == 34:
        print("Found 34")
        break
    print(i)

for i in [23,34,56]:
    if i == 34:
        print("Found 34")
        continue
    print(i)