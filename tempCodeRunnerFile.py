from flask import Flask, request, jsonify
from flask_cors import CORS
import google.generativeai as genai
import os

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

API_KEY = "AIzaSyCMNFRg6MLEVOzRycsZKqLlNivGpGwba5oq6u4KYWPb4"
if not API_KEY:
    raise ValueError("API key not found! Set GOOGLE_API_KEY as an environment variable.")

genai.configure(api_key=API_KEY)
model = genai.GenerativeModel('gemini-1.5-pro-latest')

@app.route('/get_recommendations', methods=['POST'])
def get_recommendations():
    data = request.json
    prompt = data.get("prompt", "")
    
    if not prompt:
        return jsonify({"error": "No prompt provided"}), 400
    
    try:
        response = model.generate_content(f"Provide detailed software recommendations for: {prompt}. Include name, description, key features, pricing (if applicable), and official website links.")
        return jsonify({
            "recommendations": response.text,
            "status": "success"
        })
    except Exception as e:
        return jsonify({
            "error": str(e),
            "status": "error"
        }), 500

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
