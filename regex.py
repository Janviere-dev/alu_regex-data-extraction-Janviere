import re
#Instructions on how to use this API 
# 1. Import the re module.  
# 2. Define a dictionary with keys as the type of information to extract and values as the corresponding regex patterns.
# 3. Create a sample business website data string containing various information.
# 4. Use a dictionary comprehension to apply the regex patterns to the sample data and extract the information.
# 5. Write the extracted information to a text file named "extracted_info.txt".
# 6. Print the extracted information to the console.
# This script extracts various types of information from a sample business website using regular expressions.
# Define Regular Expressions
patterns = {
    "Emails": r'\b[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}\b',  # Handles spaces and edge cases
    "URLs": r'\b(?:https?|ftp)?://(?:www\.)?[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}(?:\/[^\s]*)?\b',  # Supports 'www.example.com'
    "Phone Numbers": r'\+?\d{1,3}?[\s-]?\(?\d{3}\)?[\s.-]?\d{3}[\s.-]?\d{4}\b',  # Supports varied phone formats
    "Credit Cards": r'\b(?:\d{4}[- ]?){3}\d{4}|\d{16}\b',  # Handles card formats with or without spaces
    "Currency Amounts": r'(?:\$|RWF|USD|EUR)\s?\d{1,3}(?:,\d{3})*(?:\.\d{2})?', # Only extracts pricing found in website text
    "HTML Tags": r'<[^>]+>'  # Extracts all valid HTML elements
}
