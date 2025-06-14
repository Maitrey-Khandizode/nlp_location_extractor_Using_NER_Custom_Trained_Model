import spacy
import logging
from pathlib import Path

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class LocationExtractor:
    def __init__(self, model_path="trained_model"):
        logger.info("Loading trained model from: %s", model_path)
        
        # Verify model exists
        model_path = Path(model_path)
        if not model_path.exists():
            raise FileNotFoundError(f"Trained model not found at {model_path}. Please train first.")
        
        self.nlp = spacy.load(model_path)
        logger.info("Pipeline components: %s", self.nlp.pipe_names)
    
    def extract_locations(self, text):
        logger.info("Processing text: '%s'", text)
        doc = self.nlp(text)
        
        # Log all entities found
        entities = [(ent.text, ent.label_) for ent in doc.ents]
        logger.info("Entities found: %s", entities)
        
        # Filter location entities
        locations = [
            ent.text 
            for ent in doc.ents 
            if ent.label_ == "LOC"
        ]
        
        logger.info("Filtered locations: %s", locations)
        return locations