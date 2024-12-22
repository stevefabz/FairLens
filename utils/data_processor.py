import pandas as pd

def load_data(file_path: str) -> pd.DataFrame:
    """Load the dataset from a CSV file."""
    try:
        data = pd.read_csv(file_path)
        return data
    except Exception as e:
        raise ValueError(f"Failed to load data: {e}")
