import requests
import flask
from flask import Flask, request, jsonify
from flask_cors import CORS

API_BASE_URL = "https://api.cloudflare.com/client/v4/accounts/eaf701e6189bbc4cabff6741a7e65cbe/ai/run/"
headers = {"Authorization": "Bearer oLbxwfXSc2CvJIr31YWLMpFyV-6GPn-ny-79UI5J"}

def run(model, inputs):
    input_data = {"messages": inputs}
    response = requests.post(f"{API_BASE_URL}{model}", headers=headers, json=input_data)
    return response.json()

app = Flask(__name__)
CORS(app)  

# Function to assert the authorization header
def assert_authorization_header():
    if "Authorization" not in request.headers:
        return jsonify({"error": "Authorization header missing"}), 401

    if request.headers["Authorization"] != headers["Authorization"]:
        return jsonify({"error": "Invalid authorization header"}), 401

# Register the function to run before each request
# app.before_request(assert_authorization_header)

@app.route("/generate", methods=['POST'])
def generate():

    print(request.form["content"])
    content = request.form["content"]
    inputs = [
    {
        "role": "system",
        "content": """You are an expert coder that knows how to interpret code and generate perfect code with all the best practices, security, and performance stuff in mind."""
    },
        {"role": "user", "content": content},
    ]
    output = run("@cf/mistral/mistral-7b-instruct-v0.1", inputs)
    return jsonify(output)

if __name__ == "__main__":
    app.run(debug=True)
