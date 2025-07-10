# 🤖 AI Assistant Development

## 📌 Overview

This project focuses on the **design and development of a basic AI Assistant** using Python (Flask) and Google's **Gemini 1.5 Flash API**. The assistant is capable of:
- Answering questions
- Summarizing text
- Generating creative content (stories, poems, essays)
- Providing advice

It also features a **chat-style user interface** with a built-in feedback system to enhance user experience and continually refine prompt performance.

---

## 🎯 Objective

The goal of this project is to demonstrate:
- **Prompt Engineering Skills**: Crafting effective prompts and understanding AI response patterns.
- **System Integration**: Combining frontend and backend for interactive AI usage.
- **User-Centric Design**: Creating a clean, functional interface with real-time feedback collection.

---

## 🛠️ Tech Stack

| Layer      | Tools & Libraries Used                             |
|------------|----------------------------------------------------|
| Frontend   | HTML, CSS (Bootstrap), JavaScript (jQuery)         |
| Backend    | Python (Flask), Google Generative AI (`gemini-1.5-flash`) |
| API        | Google Generative AI (Gemini 1.5 Flash)            |

---

## 🧩 Features

### ✅ Functionalities
- **Ask a Question**: Provides clear, concise answers.
- **Summarize Text**: Summarizes content, highlighting main points.
- **Generate Creative Content**: Crafts poems, stories, or essays.
- **Get Advice**: Offers helpful suggestions on a given topic.

### 🌐 Web Interface
- Chat-style layout with:
  - Dropdown to select task
  - Text input box and send button
  - Clear distinction between user and AI responses
  - Feedback buttons ("Yes" / "No") for each response

### 🔁 Feedback Mechanism
- Collects user feedback for each response
- Used for refining prompts and improving future outputs

---

## 🧱 System Architecture

### Frontend
- **HTML/CSS**: Structured UI with responsive styling via Bootstrap
- **JavaScript/jQuery**: AJAX for async communication with Flask backend

### Backend
- **Flask**: Manages routing and request handling
- **Google Generative AI**: Gemini API processes user prompts and returns AI responses
- **Dynamic Prompt Templates**:
  - `Answer the following question clearly and concisely: {user_input}`
  - `Summarize the following text...`
  - `Generate creative content based on this idea...`
  - `Provide helpful advice on...`

---

## ⚙️ How to Run

1. Clone the repository
2. Install dependencies:
   ```bash
   pip install flask google-generativeai
   ```
3. Set your Google API Key in the backend file:
   ```python
   GOOGLE_API_KEY = "your-api-key"
   ```
4. Run the Flask app:
   ```bash
   python app.py
   ```
5. Open the app in your browser at `http://127.0.0.1:5000`

---

## 🚧 Challenges Faced

| Challenge                         | Solution                                                        |
|----------------------------------|-----------------------------------------------------------------|
| Frontend–Backend Communication   | AJAX + JSON-based async handling                               |
| Prompt Crafting Consistency      | Iterative refinement of prompts and format                      |
| API Error Handling               | Try-except blocks with console logging for easier debugging     |

---

---
---

## 📬 Feedback

The project includes a feedback system where users can rate the helpfulness of each response. Feedback data helps in:
- Improving prompt accuracy
- Refining AI interactions

---

## 📌 Author

**Sirisha** – Developer & Designer of the AI Assistant
