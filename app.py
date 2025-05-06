from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# 설정값
AGENT_ID = "asst_UCRnBi1k1NHN9gL9oUxfi8X"
API_URL = f"https://westus.api.azureml.ms/agents/asst_UCRnBi1k1NHN9gL9oUxfi8X/chat"
API_KEY = "7UG4Kmizh8aWGzPfrI4cJLt40U9kpo8oHXg6FVQeICA0Kw3Z2ppPJQQJ99BEAC4f1cMXJ3w3AAABACOGdZoM" 

@app.route("/api/messages", methods=["POST"])
def handle_message():
    data = request.get_json()
    user_input = data.get("text", "안녕하세요")

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {"input": user_input}
    response = requests.post(API_URL, headers=headers, json=payload)
    result = response.json()
    answer = result.get("result", "죄송합니다. 다시 말씀해 주세요.")

    return jsonify({
        "type": "message",
        "text": answer
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
