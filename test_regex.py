import re
from regex import patterns  # Importing regex patterns for testing 
'''
Tasks to be performed:
1. Taking expected data from assignment, and create a dictionary to store the expected data to assess the regex patterns if they used correct format.
2. Creating a function to validate the regex patterns against the expected data.
3. calling the function to validate the regex patterns.
'''
# Down here, we define the expected data for each category to validate against the regex patterns.
expected_data = {
    "Emails": ["user@example.com", "firstname.lastname@company.co.uk"],
    "URLs": ["https://www.example.com", "https://subdomain.example.org/page"],
    "Phone Numbers": ["(123) 456-7890", "123-456-7890", "123.456.7890"],
    "Credit Cards": ["1234 5678 9012 3456", "1234-5678-9012-3456"],
    "Time": ["14:30", "2:30 PM"],
    "Hashtags": ["#example", "#ThisIsAHashtag"],
    "Currency Amounts": ["$19.99", "$1,234.56"]
}

#  let's create a function to validate the regex patterns against the expected data.
# This function will check if the regex patterns correctly match the expected data.
def validate_patterns():
    print("\n===== =====\n")
    
    for category, expected_values in expected_data.items():
        print(f"Validating {category} Format:")
        invalid_found = False

        for value in expected_values:
            if not re.match(patterns[category], value):  # Check if the regex pattern matches the expected value
                print(f"Invalid Pattern Detected for: {value}")
                invalid_found = True 

        if not invalid_found: # If no invalid patterns were found
            print(f"All {category} entries are correctly recognized!\n")
        else:
            print(f"Some {category} patterns need adjustment.\n")

# Call the function to validate the regex patterns
validate_patterns()
