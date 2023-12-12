import requests

url = "http://localhost:5000/generate"
headers = {"Authorization": "Bearer oLbxwfXSc2CvJIr31YWLMpFyV-6GPn-ny-79UI5J"}
data = {"content": "your_content_here"}  # Adjust the content as needed

# Assuming your Flask server is running locally on the default port 5000
response = requests.post(url, headers=headers, data=data)

# Print the response
print(response.status_code)
print(response.json())
