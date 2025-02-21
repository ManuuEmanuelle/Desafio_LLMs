import requests
import json

from google import genai 

with open("respostas.json", "r", encoding="utf-8") as f:
    respostas = json.load(f)


response_gemini = respostas["gemini"]
response_deepseek = respostas["deepseek"]
response_dolphin = respostas["dolphin"]



prompt = f"Ranqueie os seguintes textos com base em critérios de clareza, precisão, criatividade, coerência e gramática. O primeiro texto é do Gemini, o segundo é do Deepseek e o último é do Dolphin. Seja consciso na resposta\n\n{response_gemini, response_deepseek, response_dolphin}"

client = genai.Client(api_key="AIzaSyAqwybS-M_QmzJYwf0XJOKqEXcW-e6XlHY")

response = client.models.generate_content(
    model="gemini-2.0-flash",
    contents=prompt
)


analise_gemini = response.text
print(analise_gemini)




            

    





