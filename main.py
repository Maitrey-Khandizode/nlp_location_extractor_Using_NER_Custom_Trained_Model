from location_extractor import LocationExtractor

def main():
    print("Location Extractor NLP Application")
    print("Enter text prompt (type 'exit' to quit):")
    
    # Add your custom locations here
    custom_locations = ["Baner", "Wakad", "Viman Nagar", "Kharadi"]
    extractor = LocationExtractor(custom_locations=custom_locations)
    
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