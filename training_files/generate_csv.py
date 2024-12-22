import pandas as pd
import os

def generate_combined_csv():
    """
    Process the raw UCI Adult Dataset files (`adult.data`, `adult.test`)
    and save a cleaned combined dataset as `adult_combined.csv` in `training_files/`.
    """
    # Define column names
    columns = [
        "age", "workclass", "fnlwgt", "education", "education_num", "marital_status",
        "occupation", "relationship", "race", "sex", "capital_gain", "capital_loss",
        "hours_per_week", "native_country", "income"
    ]

    try:
        # File paths
        base_path = r"C:\Users\steve\Documents\Github\FairLens\training_files"
        train_file_path = os.path.join(base_path, 'adult.data')
        test_file_path = os.path.join(base_path, 'adult.test')
        output_file_path = os.path.join(base_path, 'adult_data.csv')

        # Load the raw training dataset
        train_data = pd.read_csv(train_file_path, header=None, names=columns, na_values=" ?", skipinitialspace=True)

        # Load the raw test dataset (skip metadata lines)
        test_data = pd.read_csv(test_file_path, header=None, names=columns, na_values=" ?", skipinitialspace=True, skiprows=1)

        # Combine train and test data
        full_data = pd.concat([train_data, test_data], axis=0).reset_index(drop=True)

        # Save the combined dataset as a CSV
        full_data.to_csv(output_file_path, index=False)

        print(f"Combined CSV generated successfully: {output_file_path}")
        print(f"Dataset shape: {full_data.shape}")
    except Exception as e:
        print(f"Error generating combined CSV: {e}")

if __name__ == "__main__":
    generate_combined_csv()
