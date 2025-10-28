# app/main.py

from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from app.core_nlp import spacy_ner_from_text # Assuming app.core_nlp.py is accessible
import uvicorn


# --- Configuration ---
app = FastAPI(
    title="NER FastAPI App",
    description="A simple web application for Named Entity Recognition using SpaCy."
)

# Use the 'templates' folder for HTML files
templates = Jinja2Templates(directory="templates")

# --- Routes ---

@app.get("/", name="home")
async def home(request: Request):
    """Render the main NER input form."""
    return templates.TemplateResponse("index.html", {"request": request, "results": None})

@app.post("/analyze", name="analyze_text")
async def analyze_text(request: Request, text_input: str = Form(...)):
    """Handle text submission, run NER, and display results."""
    
    if not text_input or text_input.strip() == "":
        # Pass the input back so the user doesn't lose their original text
        return templates.TemplateResponse("index.html", 
                                          {"request": request, "results": None, 
                                           "error": "Input text cannot be empty.",
                                           "original_text": text_input})

    # Call the core NLP function (which returns a dict with 'error' or 'highlighted_html')
    results = spacy_ner_from_text(text_input)
    
    # FIX 2: Check for the explicit 'error' key added in the core_nlp.py fix.
    if "error" in results:
        return templates.TemplateResponse("index.html", 
                                          {"request": request, "results": None, 
                                           "error": results['error'], 
                                           "original_text": text_input})
    
    # Also pass the original text back so it remains in the text area
    results['original_text'] = text_input
    return templates.TemplateResponse("index.html", {"request": request, "results": results})


# --- Run the application (for local testing) ---
if __name__ == "__main__":
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
