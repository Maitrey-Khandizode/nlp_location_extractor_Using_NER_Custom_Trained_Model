import pytest
import sys
import os
import pytest

# Add the parent directory to sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from location_extractor import LocationExtractor

@pytest.fixture
def extractor():
    return LocationExtractor()

def test_ner_extraction(extractor):
    # Test locations recognized by NER
    text = "Visit Paris and Berlin"
    locations = extractor.extract_locations(text)
    assert set(locations) == {"Paris", "Berlin"}

def test_dependency_fallback(extractor):
    # Test fallback to dependency parsing
    text = "Show properties in Baner and Wakad"
    locations = extractor.extract_locations(text)
    assert set(locations) == {"Baner", "Wakad"}

def test_compound_location(extractor):
    # Test multi-word locations
    text = "Offices in New York and Los Angeles"
    locations = extractor.extract_locations(text)
    assert set(locations) == {"New York", "Los Angeles"}

def test_no_locations(extractor):
    # Test input with no locations
    text = "Schedule a meeting with John"
    locations = extractor.extract_locations(text)
    assert locations == []