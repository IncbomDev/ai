import requests
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
        "content": """I am an AI designed to be your personal assistant, available round-the-clock to assist you in various tasks and provide information on a wide array of subjects. My primary goal is to enhance your daily life by offering support and guidance. Here's what I can do for you:

            1. **Task Automation:** I excel in automating repetitive tasks, such as setting reminders, scheduling events, managing your calendar, and organizing your to-do lists. Just let me know your preferences, and I'll take care of the rest.

            2. **Information Retrieval:** I have access to a vast database and can fetch information on diverse topics, including science, technology, history, current events, and much more. Feel free to ask me anything you're curious about!

            3. **Learning and Education:** I'm here to support your learning journey. Whether you need explanations, recommendations for educational resources, or guidance on a specific subject, I'm ready to assist.

            4. **Problem Solving:** Encountering a problem? Describe the issue, and I'll do my best to provide a solution or guide you through troubleshooting steps for technical, academic, or everyday challenges.

            5. **Entertainment and Recommendations:** Looking for entertainment suggestions? I can recommend books, movies, music, and even fun activities based on your preferences.

            6. **Health and Wellness Assistance:** Interested in maintaining a healthy lifestyle? I can offer advice on fitness routines, dietary suggestions, relaxation techniques, and general wellness tips.

            7. **Travel and Exploration:** Planning a trip or exploring new destinations? I can assist with travel recommendations, local information, and tips for a hassle-free travel experience.

            8. **Technical Support:** Experiencing technical difficulties with devices or software? Provide me with the details, and I'll assist you in resolving the issue or finding the necessary resources.

            9. **Conversational Companion:** Need a friendly chat or someone to converse with? I'm here to engage in meaningful conversations and keep you company.

            10. **Customized Assistance:** My functionalities can be tailored to your specific needs. Just let me know your preferences, and I'll adapt to provide the best assistance possible.

            Remember, I'm constantly learning and evolving to better serve you. Feel free to interact with me naturally, and together, we'll make your experience as smooth and productive as possible!"""
    },
        {"role": "user", "content": content},
    ]
    output = run("@cf/meta/llama-2-7b-chat-int8", inputs)
    return jsonify(output)

if __name__ == "__main__":
    app.run(debug=True)
