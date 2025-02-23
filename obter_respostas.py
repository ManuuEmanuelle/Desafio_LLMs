import json 
import requests
from google import genai
import os
from dotenv import load_dotenv

load_dotenv()

gemini_key = os.getenv("GEMINI_KEY")

client = genai.Client(api_key = gemini_key)
response_gemini = client.models.generate_content(
    model="gemini-2.0-flash",
    contents="O que são algoritmos de Machine Learning?"
).text



deepseek_key = os.getenv("DEEPSEEK_KEY")
response = requests.post(
  url="https://openrouter.ai/api/v1/chat/completions",
  headers={
    "Authorization": f"Bearer {deepseek_key}",
    
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



dolphin_key = os.getenv("DOLPHIN_KEY")
response = requests.post(
  url="https://openrouter.ai/api/v1/chat/completions",
  headers={
    "Authorization": f"Bearer {dolphin_key}"
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