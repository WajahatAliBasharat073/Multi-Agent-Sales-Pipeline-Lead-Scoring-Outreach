import json
from src.utils import load_environment
from src.crew import build_sales_pipeline_crew

def run_sales_pipeline():
    # 1. Setup Environment
    load_environment()
    
    # 2. Build Crew
    sales_crew = build_sales_pipeline_crew()
    
    # 3. Define high-value lead example (NVIDIA)
    inputs = {
        "lead_name": "NVIDIA",
        "industry": "Semiconductor & AI Hardware",
        "key_decision_maker": "Jensen Huang",
        "position": "CEO",
        "milestone": "recent record-breaking quarterly earnings and AI GPU dominance"
    }
    
    print(f"\n--- Starting Sales Pipeline for: {inputs['lead_name']} ---")
    
    # 4. Kickoff
    result = sales_crew.kickoff(inputs=inputs)
    
    print("\n--- Sales Pipeline Execution Complete ---")
    print("Final Result:")
    print(result)

if __name__ == "__main__":
    run_sales_pipeline()
