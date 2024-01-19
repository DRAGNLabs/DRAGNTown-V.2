import os
from openai import OpenAI
from dotenv import load_dotenv as ld

ld()  # Loads in local environmental variables from the '.env' file
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))  # This is the default and can be omitted.
def query_openai(prompt:str, model="gpt-3.5-turbo", max_tokens=150):
    chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
            model=model,
        )
    
    ## See all the attributes of the chat_completion object
    # f = [att for att in dir(chat_completion)if not att.startswith('_')]
    # for i in f:
    #     print("\n", f"{i}:\n", getattr(chat_completion, i))
    
    return chat_completion.choices[0].message.content


## Example usage
prompt= "knock knock!"
print(query_openai(prompt))

