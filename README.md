# Google ADK Agent - My Tool Agent

Este projeto contém um **agente Python** usando o **Google ADK** que retorna a hora atual e o dia da semana.  

---

## Estrutura do Projeto
.
├── agent.py # Código do agente
├── requirements.txt # Dependências do projeto
├── .github/
│ └── workflows/
│ └── google_adk.yml # Workflow do GitHub Actions
└── README.md




---

## Requisitos

- Python 3.13+
- Google ADK (`pip install google-adk`)

---

## Como usar localmente

1. Crie e ative o ambiente virtual:

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1


Instale as dependências:

pip install --upgrade pip
pip install -r requirements.txt
# ou pip install google-adk



Rode o agente:

adk web
# ou python -m google.adk.cli run agent.py
~


Funções do agente

get_time(): Retorna a hora atual no formato HH:MM:SS.

get_weekday(): Retorna o dia da semana atual.

O agente principal é definido em agent.py como root_agent.