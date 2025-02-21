
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
    "Authorization": f"Bearer {API_KEY}"
  },
  json = {
    "model": "gpt-3.5-turbo",
    "messages": [
      {
        "role": "user",
        "content": prompt
      }
    ],
  })

response_data = response.json()

if "choices" in response_data:
  analise_dolphin = response_data["choices"][0]["message"]["content"]
        
if not analise_dolphin:
  print("Erro")
  exit()

print(analise_dolphin)

