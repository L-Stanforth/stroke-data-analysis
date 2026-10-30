import pandas as pd

file_path = "healthcare-dataset-stroke-data.csv"

# Load data from the CSV file using the specified file path but also handles potential errors such as missing file path or incorrect file format. If file is in different folder to script please update path.
def load_data(file_path):
    try:
        data = pd.read_csv(file_path)
        return data
    except FileNotFoundError:
        print(f"Error: The file at {file_path} was not found.")
        return None
    except pd.errors.EmptyDataError:
        print(f"Error: The file at {file_path} is empty.")
        return None
    except pd.errors.ParserError:
        print(f"Error: The file at {file_path} could not be parsed.")
        return None

# Takes loaded data and cleans column values and data types.
def data_cleaning(data):
    if data is not None:
        data["age"] = data["age"].astype(int)

        data["hypertension"] = data["hypertension"].replace([0,1], ["No","Yes"])
        data["hypertension"] = data["hypertension"].astype(str)

        data["heart_disease"] = data["heart_disease"].replace([0,1], ["No","Yes"])
        data["heart_disease"] = data["heart_disease"].astype(str)

        data["bmi"] = data["bmi"].fillna(0)

        data["stroke"] = data["stroke"].replace([0,1], ["No","Yes"])
        
        return data

    else:
        print("Data missing unable to clean")
    
def main():
    data = load_data(file_path)
    cleaned_data = data_cleaning(data)
    print(cleaned_data)


if __name__ == "__main__":
    main()