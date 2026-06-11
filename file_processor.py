# --- Step 1: EXTRACT (Read the csv file) ---
with open("inventory_data.csv", "r") as input_file:
    #.readlines() reads every line of the file into a list of strings
    raw_lines = input_file.readlines()

# Extract the header row ('name,price') so we don't mess up our math
header = raw_lines[0].strip()
# Keep only the actual data rows
data_rows = raw_lines[1:]

processed_rows = []

# --- Step 2: TRANSFORM (Loop and apply calculations)
for line in data_rows:
    # Remove hidden spaces/newlines and split line by the comma
    # Example: "Laptop,45000" becomes ["Laptop", "45000"]
    parts = line.strip().split(",")

    name = parts[0]
    price = float(parts[1]) # convert the string "45000" to a number for math

    # Apply conditional rules
    if price > 10000:
        price = price * 0.9

    elif price < 2000:
        price = price + 500

        # Recombine the name and the new price back into a CSV format string
        updated_line = f"{name},{price}"
        processed_rows.append(updated_line)

# --- Step 3: LOAD (Write out the new CSV file) ---
with open("updated_inventory.csv", "w") as output_file:
    # write the header row first
    output_file.write(header + "\n")

    # Write each processed data row
    for row in processed_rows:
        output_file.write(row + "\n")

print("pipeline executed successfully! Check your file sidebar.")