import requests
import time

url = 'https://azure-openai-advanced.openai.azure.com/openai/deployments/gpt-4o/chat/completions?api-version=2023-03-15-preview'
headers = {
    'api-key': 'YOUR API KEY'
}

body = {
    "messages": [
        {
            "role": "system",
            "content": "You are an AI assistant that helps people find information."
        },
        {
            "role": "user",
            "content": "Hi! Just respond with one word how you are."
        }
    ],
    "user": "3ba4b000-b1d0-432a-895e-177fd441b3c1"
}

for i in range(100):
    try:
        response = requests.post(url, headers=headers, json=body)
        print(f"Request {i+1} status code: {response.status_code} {response}")
        
    except requests.exceptions.RequestException as e:
        print(f"Request {i+1} failed: {e}")
    time.sleep(3)