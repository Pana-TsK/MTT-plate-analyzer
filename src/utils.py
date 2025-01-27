import pandas
import os

def create_directory(filepath):
    """Ensure the directory exists for the given filepath."""
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
