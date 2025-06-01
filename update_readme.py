import requests
from datetime import datetime

def get_weather(city="São Paulo"):
    url = f"
https://wttr.in/Sao%20Paulo?format=%l:+%c+%t\n"
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
    clima = get_weather("São Paulo")
    update_readme(clima)
