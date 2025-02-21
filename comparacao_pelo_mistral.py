import requests
import json

with open("respostas.json", "r", encoding="utf-8") as f:
  respostas = json.load(f)

response_gemini = respostas["gemini"]
response_deepseek = respostas["deepseek"]
response_dolphin = respostas["dolphin"]

API_KEY = "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"

prompt = f"Analise os seguintes textos em relação à clareza, precisão, criatividade, coerência e gramática, atribuindo a porcentagem correpondente a cada critério. O primeiro é do Gemini, o segundo é do Deepseek e o último é do Dolphin\n\n{response_gemini, response_deepseek, response_dolphin}"

response = requests.post(
  url="https://openrouter.ai/api/v1/chat/completions",
  headers={
    "Authorization": f"Bearer {API_KEY}",
  },
  json={
    "model": "gpt-3.5-turbo",
    "messages": [
      {
        "role": "user",
        "content": prompt
      }
    ]
  })

response_data = response.json()


print(response_data.get("choices", [{}])[0].get("message", {}).get("content", "").strip())