import spacy
import random
import logging
from pathlib import Path
from spacy.training import Example  # Import required for SpaCy 3.0+



# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

BASE_LOCATIONS = ["Paris", "Berlin", "New York", "Los Angeles"]

def minibatch(data, size):
    """Split data into minibatches"""
    for i in range(0, len(data), size):
        yield data[i:i+size]

def generate_training_data(custom_locations):
    """Generate training data with custom locations and variations"""
    templates = [
        "Properties available in {}",
        "Looking for apartments in {}",
        "Show houses in {}",
        "Real estate options in {}",
        "Best properties in {}",
        "{} properties",
        "Compare {} and {}",
        "Difference between {} and {}",
        "Properties in {} versus {}",
        "What's better: {} or {}?",
        "Nothing relevant here",
        "Schedule a meeting",
        "Contact support team"
    ]
    
    all_locations = BASE_LOCATIONS + custom_locations
    train_data = []


    # Single location examples
    for loc in all_locations:
        for template in templates[:6]:
            variations = [loc, loc.lower(), loc.upper(), loc.title()]
            for var in variations:
                text = template.format(var)
                start = text.find(var)
                end = start + len(var)
                train_data.append((text, {"entities": [(start, end, "LOC")]}))

    with open("training_data.txt", "w", encoding="utf-8") as f:
        for text, annot in train_data:
            f.write(f"{text} -> {annot['entities']}\n")

    return train_data
    
    # Multiple location examples
    for i in range(len(all_locations)):
        for j in range(i+1, len(all_locations)):
            for template in templates[6:10]:
                loc1 = all_locations[i]
                loc2 = all_locations[j]
                text = template.format(loc1, loc2)
                
                # Find first location
                start1 = text.find(loc1)
                end1 = start1 + len(loc1)
                
                # Find second location
                start2 = text.find(loc2)
                end2 = start2 + len(loc2)
                
                train_data.append((text, {"entities": [(start1, end1, "LOC"), (start2, end2, "LOC")]}))
    
    # Negative examples
    for template in templates[10:]:
        train_data.append((template, {"entities": []}))
    
    random.shuffle(train_data)
    return train_data

def train_model(custom_locations, output_dir="trained_model"):
    """Train a blank SpaCy model for location recognition"""
    logger.info("Creating blank 'en' model")
    nlp = spacy.blank("en")
    
    # Add NER pipeline
    if "ner" not in nlp.pipe_names:
        ner = nlp.add_pipe("ner")
    else:
        ner = nlp.get_pipe("ner")
    
    ner.add_label("LOC")
    
    # Generate training data
    train_data = generate_training_data(custom_locations)
    logger.info("Generated %d training examples", len(train_data))
    
    # Convert to Example objects
    examples = []
    for text, annotations in train_data:
        doc = nlp.make_doc(text)
        example = Example.from_dict(doc, annotations)
        examples.append(example)
    
    # Begin training
    optimizer = nlp.begin_training()
    
    # Training loop
    for itn in range(30):  # 30 iterations
        random.shuffle(examples)
        losses = {}
        
        # Batch training
        batches = minibatch(examples, size=8)
        for batch in batches:
            nlp.update(
                batch,
                drop=0.2,  # Dropout rate
                losses=losses,
                sgd=optimizer
            )
        
        logger.info("Iteration %d, Losses: %s", itn, losses)
    
    # Save model
    output_path = Path(output_dir)
    if not output_path.exists():
        output_path.mkdir()
    nlp.to_disk(output_path)
    logger.info("Model saved to %s", output_path)
    
    return nlp

if __name__ == "__main__":
    custom_locs = ["Baner", "Wakad", "Hinjewadi", "Kothrud", "Viman Nagar", "Kharadi"]
    train_model(custom_locs)