# nlp_location_extractor_Using_Custom_Trained_Model
Takes a natural language text input (like a sentence).  Extracts location names (e.g., cities, areas, countries) from that input.  Uses SpaCy's Named Entity Recognition (NER) to identify locations labeled as GPE (Geo-Political Entity) or LOC (Location).

Location Extractor - NLP Application
A Python-based Natural Language Processing application that uses SpaCy to extract location entities from natural language text. This project identifies and extracts location names (cities, countries, regions) from input text using Named Entity Recognition (NER).

🎯 Project Overview
This project implements a Named Entity Recognition (NER) system using SpaCy to extract location entities from text input. The solution is enhanced with custom location patterns to ensure specific locations like "Baner", "Wakad", and "Hinjewadi" are reliably recognized even when they might not be in standard NLP models.

This application takes natural language prompts and identifies locations mentioned in the input text. For example:

Input: "List properties in Baner and Wakad"
Output: ["Baner", "Wakad"]

The project uses SpaCy's pre-trained models and Named Entity Recognition capabilities to identify entities labeled as GPE (Geopolitical entities) and LOC (Locations).

🚀 Features

1.Location Extraction: Identifies and extracts location names from text
2.Multiple Output Formats: Simple list, detailed information, or JSON format
3.Command Line Interface: Easy-to-use CLI with multiple operation modes
4.Interactive Mode: Real-time location extraction with user input
5.Batch Processing: Process multiple texts from files
6.Comprehensive Testing: Unit tests with mocking for reliable functionality
7.Clean Code Structure: Modular, readable Python code following best practices

Installation

Python 3.10+
pip package manager

SetUp:-

Step 1 :- Create and activate a virtual environment 
        conda -p venv python == 3.13.4
    To Activate the Environment
        .venv\Scripts\activate

Step 2 :-  Install dependencies:

pip install -r requirements.txt

Step 3:- Download the SpaCy model:



Sample Input/Output
Input Text	                                   Output Locations
"Visit Paris and Berlin"	                    Paris, Berlin
"Show properties in Baner and Wakad"	            Baner, Wakad
"Offices in New York"                               New York
"Schedule meeting with John"	                    No locations found
"Compare Kharadi and Viman Nagar"	            Kharadi, Viman Nagar

✅ How to Run Tests
Make sure your virtual environment is activated.

command:-  pytest tests/test_location_extractor.py -v

tests/test_location_extractor.py::test_ner_extraction PASSED                                                                        [ 25%]
tests/test_location_extractor.py::test_dependency_fallback PASSED                                                                   [ 50%]
tests/test_location_extractor.py::test_compound_location PASSED                                                                     [ 75%]
tests/test_location_extractor.py::test_no_locations PASSED                                                                          [100%]


