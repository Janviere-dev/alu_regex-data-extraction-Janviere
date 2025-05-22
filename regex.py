import re
import os

print("welcome to the Regex Data Extraction Tool! \n")
print("This tool extracts various data types from sample website files using regex patterns.")
print("It categorizes the extracted data and logs any invalid formats separately.")
print("The script also allows users to input data for extraction and displays the extracted data.")
print("The regex patterns are defined for different data types, including emails, URLs, phone numbers, credit cards, currency amounts, hashtags, and time formats.\n")
print("Here you can see the regex power for data extraction.")
# Defining regex patterns for various data types in a dictionary

patterns = {
    "Emails": r'\b[a-zA-Z0-9]+(?:\.[a-zA-Z0-9]+)?@[a-zA-Z0-9.-]+\.(?:com|co\.uk|edu|org|net)\b',
    "URLs": r'\b(?:https?|ftp)://(?:www\.)?[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}(?:\/[^\s]*)?\b',
    "Phone Numbers": r'\(?\d{3}\)?[\s.-]?\d{3}[\s.-]?\d{4}',
    "Credit Cards": r'\b(?:\d{4}[- ]?){3}\d{4}|\d{16}\b',
    "Currency Amounts": r'(?:[$€£¥RWFUSDGBPKES])\s?\d{1,3}(?:,\d{3})*(?:\.\d{2})?',
    "Hashtags": r'#\w+',
    "Time": r'\b(?:[01]\d|2[0-3]):[0-5]\d\b|\b(?:1[0-2]|[1-9]):[0-5]\d\s?(?:AM|PM)\b' 

}

# Extracting data from all sample websites in the folder
folder_path = "sample_websites"
extracted_data = {key: set() for key in patterns}  # Store extracted values
invalid_data = {key: set() for key in patterns}  # Store invalid data separately

for filename in os.listdir(folder_path):
    file_path = os.path.join(folder_path, filename)
    print(f"\nProcessing: {filename}...")

    # Read content from each website file
    with open(file_path, "r", encoding="utf-8") as file:
        sample_data = file.read()

    # Extract data based on regex patterns
    for category, pattern in patterns.items():
        found_values = re.findall(pattern, sample_data)
        extracted_data[category].update(found_values)


        for word in sample_data.split():
            if word not in found_values and re.match(pattern, word):
                invalid_data[category].add(word)
# Save extracted data into separate files
for category, values in extracted_data.items():
    file_name = f"{category.replace(' ', '_').lower()}_data.txt"
    with open(file_name, "w", encoding="utf-8") as file:
        file.write(f"===== Extracted {category} =====\n")
        for value in sorted(values):
            file.write(f"{value}\n")

# Save errors separately with proper formatting
error_file = "error_log.txt"
with open(error_file, "w", encoding="utf-8") as file:
    file.write("===== Categorized Invalid Data =====\n")
    for category, errors in invalid_data.items():
        if errors:
            file.write(f"\n{category}:\n")
            for value in sorted(errors):
                file.write(f"{value}\n")


