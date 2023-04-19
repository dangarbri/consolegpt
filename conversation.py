from key import api_key
import openai
import sys

openai.api_key = api_key

def send_conversation_to_chatgpt(messages):
    # create a completion
    return openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages)

def get_message_from_user():
    content = input("You: ")
    if content == "exit":
        sys.exit()
    return {
        "role": "user",
        "content": content
    }

def print_response(response: dict):
    print("---------------------------")
    print("GPT: " + response["content"])
    print("---------------------------")

messages = []
while True:
    query = get_message_from_user()
    messages.append(query)
    completion = send_conversation_to_chatgpt(messages)
    response = completion.choices[0].message
    messages.append(response)
    print_response(response)
