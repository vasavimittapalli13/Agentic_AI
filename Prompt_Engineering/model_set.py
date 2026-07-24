
from openai import OpenAI

client = OpenAI()



def call_llm(email):
    response = client.chat.completions.create(
    model = 'gpt-4o-mini',
    messages = [
        {
            "role" : "user",
            "content" : "Please classify the emails into one of the category : Spam , Not spam. please just category not theory"+ email
        }
    ]

)

    return response.choices[0].message.content


emails = [ 
    'Hi Team, Please click here to send the invoice',
    'Hi Team, I am not able to login to my account',
    'Hi learner, please click here to get free course',
    'Hi, u won the lottery',
    'Hi team, please send the invoice'
]

for i in emails:
    print(call_llm(i))