from flask import Flask, request, jsonify
from flask_cors import CORS
import requests
import base64
import os
from io import BytesIO
from dotenv import load_dotenv # Import load_dotenv

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)
CORS(app) # Enable CORS for all origins

# Retrieve Hugging Face Token from environment variables
# It's crucial that your .env file is configured correctly and load_dotenv() is called.
HUGGING_FACE_TOKEN = os.getenv("HUGGING_FACE_TOKEN") # <--- REPLACE THIS WITH YOUR ACTUAL HUGGING FACE TOKEN ---!

# Hugging Face Inference API URL for the image generation model
HF_IMAGE_API_URL = "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-xl-base-1.0"

def call_hf_api(api_url, payload):
    """Helper function to call Hugging Face Inference API."""
    if not HUGGING_FACE_TOKEN: # Check if token is loaded
        raise ValueError("Hugging Face API token is not configured on the backend. Please check your .env file.")

    headers = {
        "Authorization": f"Bearer {HUGGING_FACE_TOKEN}",
        "Content-Type": "application/json"
    }

    hf_response = requests.post(api_url, headers=headers, json=payload)
    hf_response.raise_for_status() # Raises HTTPError for bad responses (4xx or 5xx)
    return hf_response.content


@app.route('/generate-image', methods=['POST'])
def generate_image():
    """Generates a static image from a text prompt."""
    data = request.get_json()
    prompt = data.get('prompt')

    if not prompt:
        return jsonify({"error": "No prompt provided."}), 400

    payload = {
        "inputs": prompt,
        "options": {
            "wait_for_model": True
        }
    }

    try:
        image_bytes = call_hf_api(HF_IMAGE_API_URL, payload)
        image_base64 = base64.b64encode(image_bytes).decode('utf-8')
        return jsonify({"image_base64": image_base64})
    except ValueError as e: # Catch the ValueError from call_hf_api
        return jsonify({"error": str(e)}), 500
    except requests.exceptions.RequestException as e:
        print(f"Error calling Hugging Face Image API: {e}")
        error_detail = "Failed to communicate with the image generation model."
        if e.response is not None:
            try:
                hf_error_json = e.response.json()
                if 'error' in hf_error_json:
                    error_detail = f"Hugging Face API error: {hf_error_json['error']}"
            except ValueError:
                error_detail = f"Hugging Face API returned non-JSON error: {e.response.text[:100]}..."
        return jsonify({"error": f"Image generation failed: {error_detail}"}), 500
    except Exception as e:
        print(f"An unexpected error occurred during image generation: {e}")
        return jsonify({"error": f"An unexpected server error occurred: {str(e)}"}), 500


if __name__ == '__main__':
    app.run(debug=True, port=5000)
