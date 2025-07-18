## ✨ AI Art Studio - Image Generator ✨
A user-friendly web application that leverages Generative AI to create unique images from text descriptions, enhanced with various artistic styles. This project demonstrates a full-stack approach, featuring an interactive frontend and a Python Flask backend that securely interacts with a powerful image generation model.

## 🚀 Features
Text-to-Image Generation: Transform your textual ideas into captivating visual art.

Artistic Style Filters: Choose from a diverse range of artistic styles (e.g., Impressionistic, Cyberpunk, Watercolor) to apply a unique aesthetic to your generated images. These styles act as creative "filters" for your vision.

Attractive & User-Friendly Interface: A clean, vibrant, and intuitive design built with Tailwind CSS and interactive elements.

Image Download: Easily download your generated artwork as a PNG file to your local storage.

Secure API Handling: Uses a Python Flask backend to securely manage API calls to the Generative AI model, keeping your API token safe from client-side exposure.

## 🛠️ Technical Stack
This application is built using a modern web stack:

# Frontend:

HTML5: Provides the core structure of the single-page application.

Tailwind CSS: A utility-first CSS framework for rapid and responsive UI development, ensuring an attractive and consistent design.

Vanilla JavaScript: Powers all interactive elements, handles user input, manages UI state, and communicates with the backend API.

Google Fonts (Inter): For modern and legible typography.

# Backend:

Python 3.x: The programming language for the server-side logic.

Flask: A lightweight and flexible Python web framework used to create the REST API endpoint that serves image generation requests from the frontend.

requests: A Python library for making HTTP requests to the Hugging Face Inference API.

base64: Used for encoding/decoding image data for transmission between the backend and frontend.

python-dotenv: Securely loads environment variables (like API tokens) from a .env file, preventing sensitive information from being committed to version control.

flask-cors: Enables Cross-Origin Resource Sharing, allowing the frontend (served from a different origin, e.g., file:// or Live Server) to communicate with the Flask backend.

# Generative AI Model:

stabilityai/stable-diffusion-xl-base-1.0: A state-of-the-art text-to-image diffusion model. This model is accessed via the Hugging Face Inference API.

## 🚀 How to Run the Application
Follow these steps to set up and run the AI Art Studio on your local machine:

Prerequisites
Python 3.x installed on your system.

pip (Python package installer).

Git (for cloning the repository, if applicable).

VS Code (recommended IDE) with the Live Server extension.

1. Clone the Repository (Optional, if you haven't already)
If you're starting from scratch, clone this repository:

git clone <your-repository-url>
cd AI_Art_Studio

2. Backend Setup (app.py)
Install Python Dependencies:
Open your terminal or command prompt, navigate to your project directory (where app.py is located), and install the required Python libraries:

pip install Flask requests python-dotenv flask-cors

Get Your Hugging Face API Token:

Go to huggingface.co and sign up or log in.

Navigate to your Settings (click your profile picture in the top right).

Go to Access Tokens.

Click "New token".

Give it a name (e.g., AIArtStudioToken).

For "Role," choose "read".

Crucially, ensure the "Make calls to Inference Providers" permission is enabled. This is often a separate checkbox below the role selection.

Click "Generate a token" and copy the token immediately. You won't see it again.

Create a .env file:
In the same directory as your app.py file, create a new file named .env (note the leading dot). Add the following line to it, replacing the placeholder with your actual Hugging Face token:

HUGGING_FACE_TOKEN="hf_YOUR_ACTUAL_HUGGING_FACE_TOKEN_HERE"

Make sure there are no spaces around the = sign.

Run the Flask Backend:
In your terminal, from your project directory, run the Flask application:

python app.py

You should see output indicating that the Flask server is running, typically on http://127.0.0.1:5000/. Keep this terminal window open as long as you want the application to be functional.

3. Frontend Setup (index.html)
Open the Project in VS Code:
Open VS Code and go to File > Open Folder.... Select the folder where you saved index.html and app.py.

Open with Live Server:

In the VS Code Explorer, right-click on index.html.

Select "Open with Live Server".

This will open the web page in your default browser. Live Server automatically reloads the page when you make and save changes, which is great for development.

### 📸 Screenshots

<img width="1036" height="912" alt="image" src="https://github.com/user-attachments/assets/b7f1b6e9-917e-46d5-b423-17d8172c0b6d" />


### ⚠️ Important Notes
Hugging Face Free Tier: The Hugging Face Inference API offers a free tier for many models, including Stable Diffusion XL. However, there might be rate limits or occasional delays, especially for popular models, as it's a shared resource.

API Key Security: The .env file is crucial for keeping your API token out of your Git history. Ensure you have a .gitignore file with /.env in it to prevent accidental commits.

Local Backend: The Python backend runs locally on your machine. The frontend communicates with http://127.0.0.1:5000. If you deploy the frontend to a web server, you'll need to deploy the backend separately and update the BACKEND_API_URL in index.html accordingly.

### 💡 Future Enhancements
More Style Options: Expand the variety of artistic styles.

Image Upload for Style Transfer: Allow users to upload their own images to use as style references.

Advanced Parameters: Add options for image resolution, guidance scale, negative prompts, etc.

User Gallery: Implement a way to save and view previously generated images.

Motion Generation (Paid Tier): If a paid API is accessible, re-integrate the motion generation feature.

Error Handling Improvements: More specific user-facing error messages for API failures.

### 📄 License
This project is open-source and available under the MIT License. 

### contact
Email : gopireddynithishkumar@gmail.com
