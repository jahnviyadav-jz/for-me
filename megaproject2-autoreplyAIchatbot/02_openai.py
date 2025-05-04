from openai import OpenAI 
#if you saved the key under a different evironment 
#variable name , you can do something like : 
client = OpenAI(
 api_key= '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'
)
command = "" # yaha copied conversation dedi 
 completion = client.chat.completions.create(
  model = "gpt-3.5-turbo", 
  messages = [
  {'role': 'system','content': 'you are a person named jahnvi who speaks hindi as well as english. she is from india and is a coder . You analyze chatt history and talk like jahnvi .  '}, 
  {'role':'user','content':command }
  ]
 )

print(completion.choices[0].message.content)