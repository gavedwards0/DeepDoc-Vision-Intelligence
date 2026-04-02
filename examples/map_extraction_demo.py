import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.engine import DeepDocExtractor
from src.schemas import MapElement

def main():
    print("--- DeepDoc Vision Intelligence: Historical Map Extraction ---\n")
    
    # Initialize the simulated engine
    extractor = DeepDocExtractor(model_id="microsoft/Florence-2-large")
    
    # Run the extraction on a mock image
    results = extractor.extract_structured(
        image_path="examples/data/london_1850_map.jpg",
        query="Extract all significant landmarks and their coordinates.",
        response_model=MapElement
    )
    
    print("\n--- Extraction Results ---")
    for i, item in enumerate(results, 1):
        print(f"{i}. {item.name} ({item.type})")
        print(f"   Coordinates: {item.coordinates}")
        print(f"   BBox: {item.bbox}")

if __name__ == "__main__":
    main()
