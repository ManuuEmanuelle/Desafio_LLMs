import json 
import requests
from google import genai


client = genai.Client(api_key="AIzaSyAqwybS-M_QmzJYwf0XJOKqEXcW-e6XlHY")
response_gemini = client.models.generate_content(
    model="gemini-2.0-flash",
    contents="O que são algoritmos de Machine Learning?"
).text

API_KEY = "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"
response = requests.post(
  url="https://openrouter.ai/api/v1/chat/completions",
  headers={
    "Authorization": f"Bearer {API_KEY}",
    
  },
  
  json = {
    "model": "gpt-3.5-turbo", 
    "messages": [
      {
        "role": "user",
        "content": "O que são algoritmos de Machine Learning?"
      }
    ]
  })

response_deepseek_data = response.json()
response_deepseek = response_deepseek_data["choices"][0]["message"]["content"]



API_KEY = "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"
response = requests.post(
  url="https://openrouter.ai/api/v1/chat/completions",
  headers={
    "Authorization": f"Bearer {API_KEY}"
  },
  json = {
    "model": "gpt-3.5-turbo",
    "messages": [
      {
        "role": "user",
        "content": "O que são algoritmos de Machine Learning?"
      }
    ],
  })

response_dolphin_data = response.json()
response_dolphin = response_dolphin_data["choices"][0]["message"]["content"]



respostas = {
    "gemini": response_gemini,
    "deepseek": response_deepseek,
    "dolphin": response_dolphin
}


with open("respostas.json", "w", encoding="utf-8") as f:
    json.dump(respostas, f, ensure_ascii=False, indent=4)