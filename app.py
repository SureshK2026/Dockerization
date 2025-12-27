from flask import Flask
from datetime import datetime
import requests

app = Flask(__name__)

@app.route("/")
def home():
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    try:
        ip = requests.get("https://api.ipify.org?format=json").json()["ip"]
    except:
        ip = "Unable to fetch IP"
    return f"<h1>Current Time: {current_time}</h1><h2>My Public IP: {ip}</h2>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)