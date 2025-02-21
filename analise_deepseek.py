import requests
import json

with open("respostas.json", "r", encoding="utf-8") as f:
  respostas = json.load(f)

response_gemini = respostas["gemini"]
response_deepseek = respostas["deepseek"]
response_dolphin = respostas["dolphin"]

prompt = (
    "Ranqueie os seguintes textos com base em critérios de clareza, precisão, criatividade, coerência e gramática.\n"
    "O primeiro é do Gemini:\n\n" + response_gemini + "\n\n"
    "O segundo é do Deepseek:\n\n" + response_deepseek + "\n\n"
    "O último é do Dolphin:\n\n" + response_dolphin + "\n\n"
    
)

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
        "content": prompt
      }
    ]
    
  })

response_data = response.json()

if "choices" in response_data:
    analise_deepseek = response_data["choices"][0]["message"]["content"]

    
if not analise_deepseek:
    print("Erro")
    exit()

print(analise_deepseek)

