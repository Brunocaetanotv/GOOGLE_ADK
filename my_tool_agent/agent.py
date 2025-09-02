from datetime import datetime
from google.adk.agents import Agent 

def get_time():
    """Retorna a hora atual do sistema"""
    return datetime.now().strftime("%H:%M:%S")

def get_weekday():
    """Retorna o dia da semana atual do sistema"""
    return datetime.now().strftime("%A")

root_agent = Agent(
    name="my_tool_agent",
    model="gemini-2.0-flash",
    description="Voce e um Agente que retorna a hora atual e o dia da semana",
    instruction="""
        Voce e um agente que retorna a hora atual e o dia da semana. 
        Voce deve usar a ferramenta get_time para retornar a hora atual. 
        Voce deve usar a ferramenta get_weekday para retornar o dia da semana. 
    """,
    tools=[get_time, get_weekday],
)
