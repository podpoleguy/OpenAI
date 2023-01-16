import os
import openai

api_key = os.environ.get("OPENAI_API_KEY", "type_here_ur_API")
openai.api_key = api_key

prompt = input("What is your question? ")
completions = openai.Completion.create(
    engine="text-davinci-002",
    prompt=prompt,
    max_tokens=1024,
    n=1,
    stop=None,
    temperature=0.5,
)
answer = completions.choices[0].text
print(answer)
