#!/usr/bin/env python
import sys
import warnings
from datetime import datetime
from dotenv import load_dotenv
import os

from crew import Larc

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# Load environment variables from .env file
load_dotenv()

# Retrieve DeepSeek configuration
deepseek_api_key = os.getenv('DEEPSEEK_API_KEY')
deepseek_api_base = os.getenv('DEEPSEEK_API_BASE')
deepseek_model = os.getenv('DEEPSEEK_MODEL')

# Check if the required configuration was loaded successfully
if not deepseek_api_key or not deepseek_api_base or not deepseek_model:
    raise ValueError("DeepSeek configuration not found in .env file")

def run():
    """
    Run the crew.
    """
    inputs = {
        'topic': 'AI LLMs',
        'current_year': str(datetime.now().year)
    }
    
    try:
        # Pass the DeepSeek configuration to the Larc class
        Larc(deepseek_api_key, deepseek_api_base, deepseek_model).crew().kickoff(inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")

run()