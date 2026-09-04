from model import call_llm

template = '''
Please classify the below email
{email}
Category should be only below type:
- Technical
- Billing
- General Inquiry

Output should like below
Category
'''
prompt = template.format(email = 'Hi team I am facing the issue.')
output = call_llm(prompt)

print(output)

