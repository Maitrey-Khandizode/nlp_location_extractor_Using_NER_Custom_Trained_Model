from location_extractor import LocationExtractor
import os

def main():
    print("Location Extractor NLP Application")
    print("Enter text prompt (type 'exit' to quit):")
    
    # Custom locations
    custom_locations = ["Baner", "Wakad", "Viman Nagar", "Kharadi"]
    
    # Train model if not exists
    model_dir = "trained_model"
    if not os.path.exists(model_dir):
        print("Training model... (this may take 1-2 minutes)")
        from train_model import train_model
        train_model(custom_locations, model_dir)
    
    # Initialize extractor
    extractor = LocationExtractor(model_path=model_dir)
    
    while True:
        user_input = input("\nInput: ")
        if user_input.lower() == 'exit':
            break
        
        locations = extractor.extract_locations(user_input)
        
        if locations:
            print("Locations found:", ", ".join(locations))
        else:
            print("No locations found")

if __name__ == "__main__":
    main()