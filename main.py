import pandas as pd

file_path = "healthcare-dataset-stroke-data.csv"

def load_data(file_path):
    # Load data from the CSV file using the specified file path but also handles potential errors such as missing file path or incorrect file format. If file is in different folder to script please update path.
    try:
        data = pd.read_csv(file_path)
        return pd.DataFrame(data)
    except FileNotFoundError:
        print(f"Error: The file at {file_path} was not found.")
        return None
    except pd.errors.EmptyDataError:
        print(f"Error: The file at {file_path} is empty.")
        return None
    except pd.errors.ParserError:
        print(f"Error: The file at {file_path} could not be parsed.")
        return None