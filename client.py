from openai import OpenAI

client = OpenAI(
    api_key="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",  # Replace with your actual API key, keep it secret!
)

completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a virtual assistant named Sonu, skilled in general tasks like Alexa and Google Cloud."},
        {"role": "user", "content": "Compose a poem that explains the concept of recursion in programming."}
    ]
)

print(completion.choices[0].message.content)