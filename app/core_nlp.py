# app/core_nlp.py

import spacy
from collections import Counter
from spacy import displacy  # <<< IMPORT displacy
from typing import Dict, List, Tuple

# --- CRITICAL: Load SpaCy model ONCE globally ---
try:
    nlp = spacy.load('en_core_web_sm')
    print("SpaCy model 'en_core_web_sm' loaded successfully.")
except Exception as e:
    print(
        f"Error loading SpaCy model: {e}. Please ensure it is installed: python -m spacy download en_core_web_sm")
    nlp = None

# --- Custom Type Aliases for Clarity ---
EntityTuple = Tuple[str, str]
SpaCyResult = Dict[str, any]


def spacy_ner_from_text(text: str) -> SpaCyResult:
    """
    Performs Named Entity Recognition and generates both a raw list of entities
    and a clean HTML visualization.
    """
    if nlp is None:
        # Return a structured error response
        return {
            'error': "NLP model not loaded.",
            'entities': [],
            'counts': {},
            'highlighted_html': "<p style='color:red;'>NLP model not available.</p>"
        }

    doc = nlp(text)

    # 1. Extract raw entities: (text, label_)
    entities: List[EntityTuple] = [(ent.text, ent.label_) for ent in doc.ents]

    # 2. Analyze counts
    entity_counts = Counter([entity[1] for entity in entities])

    # 3. Create clean HTML representation using displacy
    # We render it 'manual' style so the output is a clean string of HTML
    # The 'displacy.render' function returns HTML for embedding.
    highlighted_html = displacy.render(
        doc,
        style="ent",
        page=False,  # Important: Don't render full HTML page structure
        minify=True  # Optional: compress the HTML output
    )

    return {
        'entities': entities,
        'counts': dict(entity_counts),
        'text': text,
        'highlighted_html': highlighted_html  # <<< New, clean HTML output
    }


# Optional: Run a test
if __name__ == '__main__':
    TEST_CORPUS = "Apple is looking at buying U.K. startup for $1 billion."
    results = spacy_ner_from_text(TEST_CORPUS)
    print("\n--- Raw Entities ---")
    print(results['entities'])
    print("\n--- Highlighted HTML (To be displayed on webpage) ---")
    print(results['highlighted_html'])
