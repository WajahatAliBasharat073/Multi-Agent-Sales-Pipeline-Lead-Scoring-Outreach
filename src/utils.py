import os
from dotenv import load_dotenv

def load_environment():
    """
    Load environment variables and set the OpenAI model name.
    """
    load_dotenv()
    
    # Ensure OPENAI_MODEL_NAME is set, default to gpt-4-turbo for hierarchical process
    if not os.getenv("OPENAI_MODEL_NAME"):
        os.environ["OPENAI_MODEL_NAME"] = "gpt-4-turbo"
        
    return {
        "openai_api_key": os.getenv("OPENAI_API_KEY"),
        "serper_api_key": os.getenv("SERPER_API_KEY")
    }

def get_model_name():
    return os.getenv("OPENAI_MODEL_NAME", "gpt-4-turbo")
