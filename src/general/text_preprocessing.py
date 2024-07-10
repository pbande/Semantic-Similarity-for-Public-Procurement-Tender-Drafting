import nltk
from nltk.corpus import stopwords
import spacy
import re

# Load spaCy's Spanish language model
nlp = spacy.load('es_core_news_sm')

# Download NLTK stop words
nltk.download('stopwords')

# Download NLTK data
nltk.download('punkt')
nltk.download('stopwords')

# Define Spanish stop words
spanish_stopwords = set(stopwords.words('spanish'))

# Load spaCy's Spanish language model
nlp = spacy.load('es_core_news_sm')

def preprocess_text(text):
    # Tokenization
    tokens = nltk.word_tokenize(text, language='spanish')
    
    # Remove unnecessary information (personal information, days, months)
    tokens = [re.sub(r'\b\d{2,}\b|(?:\d{1,2}[\/\-\.]){2,}\d{2,4}|\b(?:tel|email)\b', '', token) for token in tokens]
    tokens = [token for token in tokens if token.lower() not in ['lunes', 'martes', 'miércoles', 'jueves', 'viernes', 'sábado', 'domingo', 'enero', 'febrero', 'marzo', 'abril', 'mayo', 'junio', 'julio', 'agosto', 'septiembre', 'octubre', 'noviembre', 'diciembre']]
    
    # Remove non-alphabetic characters
    tokens = [re.sub(r'[^a-zA-ZáéíóúÁÉÍÓÚñÑüÜ]', '', token) for token in tokens]
    
    # Lowercasing
    tokens = [token.lower() for token in tokens]
    
    # Remove stop words
    tokens = [token for token in tokens if token not in spanish_stopwords]
    
    # Lemmatization
    doc = nlp(' '.join(tokens))
    tokens = [token.lemma_ for token in doc]
    
    return ' '.join(tokens)
