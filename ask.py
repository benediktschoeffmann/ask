import os
from dotenv import load_dotenv

from groq import Groq

#  load .env values
load_dotenv()

client = Groq(
    api_key=os.environ.get("GROQ_API_KEY"),
)

question = input("Enter your question: ")

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": question,
        }
    ],
    model="llama-3.3-70b-versatile",
)

content = chat_completion.choices[0].message.content
filename = "questions/" + question.replace(" ", "_").replace(":", "").replace("?", "").replace(",", "").replace(".", "") + ".md"

with open(filename, "w") as file:
    file.write("# " + question + "\n\n")
    file.write("## Answer\n")
    file.write(content)

file.close()
print(chat_completion.choices[0].message.content)
print(chat_completion.choices[0].message)