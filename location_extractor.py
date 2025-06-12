import spacy
from spacy.pipeline import EntityRuler
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class LocationExtractor:
    def __init__(self, model_name="en_core_web_lg", custom_locations=None):
        logger.info("Loading SpaCy model: %s", model_name)
        self.nlp = spacy.load(model_name)
        
        # Log existing pipeline components
        logger.info("Initial pipeline components: %s", self.nlp.pipe_names)
        
        # Add EntityRuler using the component name — this is the FIX
        ruler = self.nlp.add_pipe("entity_ruler", before="ner", config={"overwrite_ents": True})
        
        # Prepare location list
        all_locations = custom_locations or []
        all_locations.extend(["Baner", "Wakad", "Hinjewadi", "Kothrud"])
        
        # Create SpaCy-style patterns for case-insensitive matching
        patterns = []
        for loc in set(all_locations):
            tokens = loc.split()
            pattern = [{"lower": token.lower()} for token in tokens]
            patterns.append({"label": "GPE", "pattern": pattern})
        
        logger.info("Adding %d patterns to EntityRuler", len(patterns))
        ruler.add_patterns(patterns)
        
        logger.info("Added EntityRuler before NER in pipeline")
        logger.info("Final pipeline components: %s", self.nlp.pipe_names)


    
    def extract_locations(self, text):
        logger.info("Processing text: '%s'", text)
        doc = self.nlp(text)
        
        # Log all entities found
        entities = [(ent.text, ent.label_) for ent in doc.ents]
        logger.info("All entities found: %s", entities)
        
        # Filter location entities
        locations = [
            ent.text 
            for ent in doc.ents 
            if ent.label_ in ["GPE", "LOC"]
        ]
        
        logger.info("Filtered locations: %s", locations)
        return locations