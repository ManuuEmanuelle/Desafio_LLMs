# Comparador de Respostas de LLMs

Este projeto tem como objetivo comparar as respostas geradas por três diferentes modelos de linguagem (LLMs) para uma mesma pergunta. Ele utiliza os modelos **Gemini**, **Deepseek** e **Dolphin** para gerar respostas, e depois implementa um mecanismo para comparar e ranquear essas respostas com base em critérios de qualidade, utilizando os próprios modelos para avaliar as respostas uns dos outros.

### Pré-requisitos

Instale as seguintes ferramentas e bibliotecas:

- Python 3.8 ou superior
- Bibliotecas Python: `requests`, `google-generativeai`, `json`

Você pode instalar as dependências usando o `pip`:

```bash
pip install requests google-generativeai 
```

### Configuração

1. Clone este repositório:

```bash
git clone https://github.com/ManuuEmanuelle/Desafio_LLMs/tree/main
cd Desafio_LLMs
```

2. Configure as chaves de API:
   - Crie um arquivo `.env` na raiz do projeto e adicione suas chaves de API:

```bash
GEMINI_API_KEY=sua_chave_gemini_aqui
DEEPSEEK_API_KEY=sua_chave_deepseek_aqui
DOLPHIN_API_KEY=sua_chave_dolphin_aqui
MISTRAL_API_KEY=sua_chave_mistral_aqui
```

3. Substitua as chaves de API nos arquivos `obter_respostas.py`, `comparacao_pelo_mistral.py`, `analise_gemini.py`, `analise_dolphin.py` e `analise_deepseek.py` pelas suas chaves reais.

### Execução do Projeto

1. **Obtenha as respostas dos modelos**:
   - Execute o script `obter_respostas.py` para enviar a pergunta "O que são algoritmos de Machine Learning?" para os três modelos e salvar as respostas em um arquivo `respostas.json`.

```bash
python obter_respostas.py
```

2. **Compare as respostas**:
   - Execute o script `comparacao_pelo_mistral.py` para comparar as respostas usando o modelo Mistral e exibir a análise.

```bash
python comparacao_pelo_mistral.py
```

3. **Analise as respostas com cada modelo**:
   - Execute os scripts `analise_gemini.py`, `analise_dolphin.py` e `analise_deepseek.py` para que cada modelo ranqueie as respostas dos outros modelos.

```bash
python analise_gemini.py
python analise_dolphin.py
python analise_deepseek.py
```

## Funcionalidades

- **Integração com múltiplos LLMs**: O projeto suporta a integração com os modelos **Gemini**, **Deepseek** e **Dolphin**.
- **Comparação de respostas**: As respostas geradas pelos modelos são comparadas com base em critérios de qualidade, como clareza, precisão, criatividade, coerência e gramática.
- **Autoavaliação**: Os próprios modelos avaliam e ranqueiam as respostas uns dos outros.


## Autora

- **Emanuelle de Carvalho Brito** - 
    (https://github.com/ManuuEmanuelle)

