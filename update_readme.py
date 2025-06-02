import requests
from datetime import datetime
import random

with open("capitais.txt", "r", encoding="utf-8") as f:
    capitais = [linha.strip() for linha in f if linha.strip()]

cidade = random.choice(capitais)
def get_weather(city=cidade):
    url = f"https://wttr.in/{city.replace(' ', '%20')}?format=%l:+%c+%t\n"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            weather = response.text.strip()
        else:
            weather = "Não foi possível obter o clima."
    except Exception as e:
        weather = f"Erro: {e}"

    now = datetime.now().strftime("%d/%m/%Y %H:%M")
    return f"### 🌤️ Clima em {city}\n```\n{weather}\nAtualizado em: {now}\n```"

def update_readme(weather_text):
    with open("README.md", "w", encoding="utf-8") as f:
        f.write(f"# 👋 Bem-vindo ao meu perfil GitHub\n\n{weather_text}\n\n_Automaticamente atualizado com o clima via [wttr.in](https://wttr.in)_")

if __name__ == "__main__":
    clima = get_weather(cidade)
    update_readme(clima)

