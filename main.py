from flask import Flask, request
import requests
import os

app = Flask(__name__)

N8N_WEBHOOK_URL = os.getenv("N8N_WEBHOOK_URL", "https://n8n.srv848053.hstgr.cloud/webhook-test/lead-telegram")

@app.route("/", methods=["POST"])
def telegram_proxy():
    data = request.json
    print("Received from Telegram:", data)
    try:
        response = requests.post(N8N_WEBHOOK_URL, json=data)
        return {"status": "forwarded", "n8n_response": response.text}, 200
    except Exception as e:
        return {"error": str(e)}, 500

@app.route("/", methods=["GET"])
def test_route():
    return "✅ Proxy Flask for Telegram → n8n is running."

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
