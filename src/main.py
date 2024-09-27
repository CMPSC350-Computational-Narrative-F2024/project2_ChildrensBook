#!/usr/bin/python

import os
import openai
from dotenv import dotenv_values

# Set up OpenAI credentials

CONFIG = dotenv_values(".env")

OPEN_AI_KEY = CONFIG["KEY"] or os.environ["OPEN_AI_KEY"]
OPEN_AI_ORG = CONFIG["ORG"] or os.environ["OPEN_AI_ORG"]

openai.api_key = OPEN_AI_KEY
openai.organization = OPEN_AI_ORG

def load_file(filename: str = "") -> str:
    """Loads an arbitrary file name"""
    with open(filename, "r") as fh:
        return fh.read()

def main():

    # Load source file
    prompt = load_file("data/prompt.txt")

    response = openai.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "user", "content": prompt}
        ],
        # "Level of risk" associated with model predictions
        temperature = 0.9,
        top_p = 1,
        # Maximum size of requests (this is already max size)
        max_tokens = 100, #(4097 - len(prompt))
        # Number of results to attempt and return
        n = 10
    )
    #print(response.choices[0].message)

    # Extract the response text
    result = response.choices[0].message.content.strip()

    print(result)
    
if __name__ == "__main__":
    main()