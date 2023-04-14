import json

# Load the content of the original output file
with open("original_output.json", "r") as f:
    original_data = json.load(f)

# Load the content of the new output file
with open("new_output.json", "r") as f:
    new_data = json.load(f)

# Combine the data from both files
combined_data = original_data + new_data

# Save the combined data into a single JSON file
with open("combined_output.json", "w") as f:
    json.dump(combined_data, f)
