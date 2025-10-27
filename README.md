# TextVision-AI-Intelligence

TextVision AI is a powerful web application designed to analyze and extract key entities from text using advanced Natural Language Processing (NLP) techniques. This project identifies entities like people, organizations, locations, dates, monetary values, and more, and provides a user-friendly web interface to visualize the results.

## 📋 Features:
- **Named Entity Recognition (NER)**: Extracts and classifies entities such as names, organizations, locations, dates, monetary values, and other relevant data.
- **Interactive User Interface**: Provides a simple and effective way for users to input text and get instant analysis of the highlighted entities.
- **Entity Categorization**: Displays entities in various categories like PERSON, ORGANIZATION, GPE (Geopolitical Entity), DATE, MONEY, and others with color-coded highlights.
- **Detailed Results**: Offers insights into the frequency and types of entities detected in the provided text.

## 🛠️ Tech Stack:
- **Frontend**:
  - HTML
  - CSS
  - JavaScript (with Tailwind CSS for styling)

- **Backend**:
  - Python
  - FastAPI (Flask/FastAPI for the web server)
  - SpaCy for NER

- **Development Environment**:
  - Visual Studio Code (VS Code)

- **Local Deployment**:
  - Uvicorn (ASGI server)

## 📥 Installation:
1. **Clone the repository**:
    ```bash
    git clone https://github.com/your-username/TextVision-AI.git
    ```
2. **Navigate into the project folder**:
    ```bash
    cd TextVision-AI
    ```
3. **Create and activate the virtual environment**:
    - For Windows:
      ```bash
      python -m venv venv
      venv\Scripts\activate
      ```
    - For macOS/Linux:
      ```bash
      python3 -m venv venv
      source venv/bin/activate
      ```
4. **Install the dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

## 🚀 Run Locally:
1. **Start the application**:
    ```bash
    uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
    ```
2. Open your browser and navigate to `http://localhost:8000` to see the app in action.

## 📜 License:
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

**Created by**: Shafiul Opee
