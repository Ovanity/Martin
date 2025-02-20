from flask import Flask, render_template, jsonify
import random
import socket
from datetime import datetime

app = Flask(__name__)

# Statuts en fonction de l'heure et des activités de Martin
STATUSES = [
    {"time_range": (0, 7), "status": "Martin dort paisiblement 💤"},
    {"time_range": (7, 10), "status": "Martin se réveille doucement avec un café ☕"},
    {"time_range": (10, 13), "status": "Martin travaille sur sa musique 🎶"},
    {"time_range": (13, 15), "status": "Martin prend une pause déjeuner 🍽️"},
    {"time_range": (15, 18), "status": "Martin fait du montage vidéo/photo 🎥"},
    {"time_range": (18, 21), "status": "Martin bidouille du code 💻"},
    {"time_range": (21, 23), "status": "Martin écrit des pensées ✍️"},
    {"time_range": (23, 24), "status": "Martin se détend en pensant à toi 🌙"},
]

# Messages réconfortants et aléatoires
COMFORT_MESSAGES = [
    "Même occupé, tu es toujours dans un coin de ma tête. 💖",
    "Je sais que je ne réponds pas toujours vite... mais tu comptes beaucoup pour moi. 😊",
    "Parfois je suis perdu dans mes projets, mais jamais trop loin de toi. 🌟",
    "Ce petit bout de moi est là pour te rappeler que tu es importante. ✨",
    "Je suis peut-être silencieux, mais jamais indifférent. 🙌",
    "Je voulais que tu puisses sentir que je suis là, même quand je ne parle pas. 🍀",
    "Si tu lis ça, c’est que tu penses à moi... et tu sais quoi ? Moi aussi je pense à toi. 💫"
]

def get_current_status():
    current_hour = datetime.now().hour
    for status in STATUSES:
        start, end = status["time_range"]
        if start <= current_hour < end:
            return status["status"]
    return "Martin pense à toi, peu importe l'heure. ❤️"

@app.route('/')
def index():
    return render_template('chat.html')

@app.route('/get_status_and_message')
def get_status_and_message():
    status = get_current_status()
    message = random.choice(COMFORT_MESSAGES)
    return jsonify({"status": status, "message": message})

if __name__ == '__main__':
    # Obtenir l'adresse IP locale pour permettre l'accès via le réseau Wi-Fi
    hostname = socket.gethostname()
    local_ip = socket.gethostbyname(hostname)

    # L'application sera accessible sur le réseau local via http://<votre_ip_locale>:5000
    app.run(debug=True, host='0.0.0.0')
