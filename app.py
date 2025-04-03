"""
import google.generativeai as genai
import os

API_KEY = "AIzaSyAqJXj39JAabzqLXsPykvwe6q6u4KYWPb4"
if not API_KEY:
    raise ValueError("API key not found! Set GOOGLE_API_KEY as an environment variable.")

genai.configure(api_key=API_KEY)

model = genai.GenerativeModel('gemini-1.5-pro-latest')

def chat_with_gemini(prompt):
    try:
        response = model.generate_content(prompt)
        return response.candidates[0].content if response.candidates else "No response received."
    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == "__main__":

    while True:
        user_input = input("You: ")
        if user_input.lower() in ["quit", "exit", "bye"]:
            print("Goodbye!")
            break

        response = chat_with_gemini(user_input)
        print("Gemini:", response)

# List available models
try:
    models = genai.list_models()
    for model in models:
        print(model.name)
except Exception as e:
    print(f"Error fetching models: {str(e)}")
"""
# from flask import Flask, request, jsonify
# from flask_cors import CORS
# import google.generativeai as genai
# import os

# app = Flask(__name__)
# CORS(app)  # Enable CORS for all routes

# API_KEY = "AIzaSyCMNFRg6MLEVOzRycsZKqLlNivGpGwba5o"
# if not API_KEY:
#     raise ValueError("API key not found! Set GOOGLE_API_KEY as an environment variable.")

# genai.configure(api_key=API_KEY)
# model = genai.GenerativeModel('gemini-1.5-pro-latest')

# @app.route('/get_recommendations', methods=['POST'])
# def get_recommendations():
#     data = request.json
#     prompt = data.get("prompt", "")
    
#     if not prompt:
#         return jsonify({"error": "No prompt provided"}), 400
    
#     try:
#         response = model.generate_content(f"Provide detailed software recommendations for: {prompt}. Include name, description, key features, pricing (if applicable), and official website links.")
#         return jsonify({
#             "recommendations": response.text,
#             "status": "success"
#         })
#     except Exception as e:
#         return jsonify({
#             "error": str(e),
#             "status": "error"
#         }), 500

# if __name__ == "__main__":
#     app.run(debug=True, host="0.0.0.0", port=5001)



# from flask import Flask, request, jsonify, render_template
# import google.generativeai as genai
# import os

# app = Flask(__name__)

# # Configure the API key
# API_KEY = os.getenv("GOOGLE_API_KEY")
# if not API_KEY:
#     raise ValueError("API key not found! Set GOOGLE_API_KEY as an environment variable.")
# genai.configure(api_key=API_KEY)

# # Route to serve the homepage
# @app.route('/')
# def home():
#     return render_template('index.html')  # Ensure you have an index.html in the templates folder

# # Route to handle API requests
# @app.route('/get_recommendations', methods=['POST'])
# def get_recommendations():
#     data = request.json
#     prompt = data.get("prompt", "")
    
#     if not prompt:
#         return jsonify({"error": "No prompt provided"}), 400
    
#     try:
#         # Use the Google Generative AI API to generate recommendations
#         response = genai.generate_text(
#             model="models/gemini-1.5-pro-latest",
#             prompt=f"Provide detailed software recommendations for: {prompt}. Include name, description, key features, pricing (if applicable), and official website links."
#         )
#         return jsonify({
#             "recommendations": response.candidates[0]['output'] if response.candidates else "No recommendations found.",
#             "status": "success"
#         })
#     except Exception as e:
#         return jsonify({"error": str(e)}), 500

# if __name__ == "__main__":
#     app.run(debug=True)



from flask import Flask, request, jsonify, send_file
import google.generativeai as genai
import os

app = Flask(__name__)

# Configure the API key
API_KEY = os.getenv("GOOGLE_API_KEY")
if not API_KEY:
    raise ValueError("API key not found! Set GOOGLE_API_KEY as an environment variable.")
genai.configure(api_key=API_KEY)

# Route to serve index.html from the root directory
@app.route('/')
def home():
    return send_file('index.html')  # Serve index.html from the root directory

# Route to handle API requests
@app.route('/get_recommendations', methods=['POST'])
def get_recommendations():
    data = request.json
    prompt = data.get("prompt", "")
    
    if not prompt:
        return jsonify({"error": "No prompt provided"}), 400
    
    try:
        # Use the Google Generative AI API to generate recommendations
        response = genai.generate_text(
            model="models/gemini-1.5-pro-latest",
            prompt=f"Provide detailed software recommendations for: {prompt}. Include name, description, key features, pricing (if applicable), and official website links."
        )
        return jsonify({
            "recommendations": response.candidates[0]['output'] if response.candidates else "No recommendations found.",
            "status": "success"
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
