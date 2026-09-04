#step1: model
from model import call_llm
import pandas as pd

#step2: write your template
template = '''
Please classify the below email
{email}
Category should be only below type:
- Technical
- Billing
- General Inquiry

Rules:
- Return ONLY the category name and confidance score ( between 1-10). Nothing else.
- No explanation, no punctuation, no extra words.
- If unsure, return "Other".

Output should like below
Category
'''

data = pd.read_excel("C:\\Users\\vasav\\OneDrive\\Desktop\\Agentic_AI\\Prompt_Engineering\\emails.xlsx")

emails = list(data['Body'])

output = []
for i in emails:
    prompt = template.format(email=i)
    output.append(call_llm(prompt))

# print(output)

data['model_output'] = output
data.to_csv("final-result.csv")