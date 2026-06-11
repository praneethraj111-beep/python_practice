import pandas as pd

# Define our reusable cleaning engine
def clean_inventory_data(input_filename):
    print(f"=== Processing File: {input_filename}===")

    # 1. Load the specific file passed into the function
    df = pd.read_csv(input_filename)

    # 2. Run the cleaning steps you mastered
    df = df.drop_duplicates().reset_index(drop=True)
    df['price'] = pd.to_numeric(df['price'], errors='coerce')
    df['price'] = df['price'].fillna(0)

    # 3. Return the clean dataframe out of the function
    return df

# --- USING THE FUNCTION (Calling the machine) ---
# We can now process our file by simply passing its name into our tool!
cleaned_df = clean_inventory_data("dirty_inventory.csv")

print("\n=== Cleaned Output Recieved===")
print(cleaned_df)