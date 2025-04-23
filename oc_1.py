from ollama import chat
"""
response = chat(model='gemma3:1b', messages=[
  {
    'role': 'user',
    'content': 'Hey you!',
  },
])
# notice your exact answer could be different due to some random processes in the model (learn about that later)
print(response.message.content)

response_2 = chat(model='gemma3:1b', messages=[
  {
    'role': 'user',
    'content': 'Hey I am tester and I am happy to participate in this exciting new llm and ai agents course at opencampus!',
  },
])

print(response_2.message.content)


response_3 = chat(model='gemma3:1b', messages=[
  {
    'role': 'user',
    'content': 'Who am I?',
  },
])

print(response_3.message.content)

"""
tease_response = chat(model='gemma3:1b', messages=[
  {
    'role': 'user',
    'content': 3000*'Hi',
  },
])

print(tease_response.message.content)