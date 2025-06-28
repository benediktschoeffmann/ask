import os
from dotenv import load_dotenv

from groq import Groq

#  load .env values
load_dotenv()

client = Groq(
    api_key=os.environ.get("GROQ_API_KEY"),
)

question = "Explain the advantages of non-sql databases over sql databases"

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": question,
        }
    ],
    model="llama-3.3-70b-versatile",
)

print(chat_completion.choices[0].message.content)