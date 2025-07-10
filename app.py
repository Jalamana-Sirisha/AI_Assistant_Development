from flask import Flask, render_template, request, jsonify
import google.generativeai as genai
import os

GOOGLE_API_KEY = "AIzaSyCa-YnjBmkSKJywMhyduIOujIck7IK3MKs" 

if not GOOGLE_API_KEY:
    raise ValueError("GOOGLE_API_KEY is not set. Please provide your API key or ensure it's in environment variables.")

try:
    genai.configure(api_key=GOOGLE_API_KEY)
    
    model = genai.GenerativeModel('gemini-1.5-flash')
    
    chat = model.start_chat(history=[])
    print("Gemini model and chat session configured successfully!")
except Exception as e:
    print(f"Error during Gemini API configuration or model initialization: {e}")
    
    raise


app = Flask(__name__)

@app.route('/')
def index():
    """
    Renders the main HTML page for the AI Assistant application.
    This serves the index.html file located in the 'templates' folder.
    """
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat_response():
    """
    Handles POST requests from the frontend to send user messages to the Gemini API
    and return the bot's response based on the selected function.
    """
    
    user_input = request.json.get('message')
    function_type = request.json.get('function_type')

    if not user_input or not function_type:
        print("Error: Missing message or function type in the request.")
        return jsonify({"error": "Missing message or function type"}), 400

   
    prompt = ""
    if function_type == "Youtube":
        
        prompt = f"Answer the following question clearly and concisely: {user_input}"
    elif function_type == "summarize_text":
        
        prompt = f"Summarize the following text, highlighting the main points: {user_input}"
    elif function_type == "creative_content":
       
        prompt = f"Generate creative content based on this idea: {user_input}. For example, write a short story, a poem, or a short essay."
    elif function_type == "provide_advice":
        
        prompt = f"Provide helpful advice on the following topic: {user_input}"
    else:
        return jsonify({"error": "Invalid function type selected"}), 400

    try:
        print(f"Received user message for {function_type}: '{user_input}'")
        print(f"Sending prompt to Gemini: '{prompt}'")
        
        response = chat.send_message(prompt).text
        print(f"Generated Gemini response: '{response[:100]}...'") # Log first 100 chars
        
        
        return jsonify({"response": response})
    except Exception as e:
        
        print(f"Error during Gemini API call: {e}")
        
        return jsonify({"error": str(e)}), 500

@app.route('/feedback', methods=['POST'])
def receive_feedback():
    
    data = request.json
    message_id = data.get('message_id') 
    feedback = data.get('feedback') 
    user_message = data.get('user_message')
    bot_response = data.get('bot_response')

    
    print(f"--- FEEDBACK RECEIVED ---")
    print(f"User Message: '{user_message}'")
    print(f"Bot Response: '{bot_response}'")
    print(f"Feedback: {feedback.upper()} (Helpful)")
    print(f"-------------------------")

    return jsonify({"status": "Feedback received!"}), 200

if __name__ == '__main__':
    app.run(debug=True)
