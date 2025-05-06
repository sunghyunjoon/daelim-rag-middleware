from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

API_URL = "https://daelim-chat-openai-westus.openai.azure.com/openai/deployments/gpt-4o-mini/chat/completions?api-version=2025-01-01-preview"
API_KEY = "7UG4Kmizh8aWGzPfrI4cJLt40U9kpo8oHXg6FVQeICA0Kw3Z2ppPJQQJ99BEAC4f1cMXJ3w3AAABACOGdZoM"

@app.route("/api/messages", methods=["POST"])
def handle_message():
    data = request.get_json()
    user_input = data.get("text", "안녕하세요")

    headers = {
        "api-key": API_KEY,
        "Content-Type": "application/json"
    }

    payload = {
        "messages": [
            {"role": "user", "content": user_input}
        ],
        "max_tokens": 1000,
        "temperature": 1.0
    }

    response = requests.post(API_URL, headers=headers, json=payload)
    result = response.json()
    answer = result['choices'][0]['message']['content']

    return jsonify({
        "type": "message",
        "text": answer
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
