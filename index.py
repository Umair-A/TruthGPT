import openai
from dotenv import load_dotenv
import os

load_dotenv()

# Initialize the OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

def is_tweet_true(tweet_text):
    prompt = f"Is the following Twitter post true, false or uncertain? '{tweet_text}'"

    response = openai.Completion.create(engine="text-davinci-002", prompt=prompt, max_tokens=50)
    answer = response.choices[0].text.strip()

    if "true" in answer.lower():
        return "True"
    elif "false" in answer.lower():
        return "False"
    else: 
        return "Uncertain"

# Test the function
tweet_text = "Biggest source of success is luck."   
print(is_tweet_true(tweet_text))
    
  