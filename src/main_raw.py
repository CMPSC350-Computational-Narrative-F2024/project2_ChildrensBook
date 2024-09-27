from openai import OpenAI
client = OpenAI()

# Set your API key here (Alternatively, use environment variables)
client.api_key = ""
client.organization = ""

# Define the prompt and model
prompt = "write a haiku about ai"

completion = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role": "user", "content": prompt}
    ]
)
print(completion.choices[0].message)
