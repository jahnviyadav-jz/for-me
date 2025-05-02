from openai import OpenAI 
#if you saved the key under a different evironment 
#variable name , you can do something like : 
client = OpenAI(
 api_key= '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'
)
 completion = client.chat.completions.create(
  model = "gpt-3.5-turbo", 
  messages = [
  {'role': 'system','content': 'you are a virtual assistant named Jarvis skilled in general tasks like Alexa and Google Cloud '}, 
  {'role':'user','content':'wht is coding '}
  ]
 )

print(completion.choices[0].message.content)