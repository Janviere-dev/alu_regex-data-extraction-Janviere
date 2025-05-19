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
# Sample business website data where information would be extracted from
sample_data = """
<!DOCTYPE html>
<html>
<head>
    <title>Welcome to Rwanda Business Hub</title>
    <meta name="description" content="Connecting businesses in Rwanda to growth opportunities.">
</head>
<body>
    <header>
        <h1>Rwanda Business Hub</h1>
        <nav>
            <a href="https://www.rwandabusiness.rw/home">Home</a> |
            <a href="https://www.rwandabusiness.rw/services">Services</a> |
            <a href="https://www.rwandabusiness.rw/contact">Contact</a>
        </nav>
    </header>

    <main>
        <h2>About Rwanda Business Hub</h2>
        <p>Rwanda Business Hub is committed to driving innovation, supporting entrepreneurship, and fostering business growth across Rwanda.</p>

        <h2>Our Services</h2>
        <p>We offer specialized business consulting, investment support, and technology solutions.</p>
        <p>Pricing: Basic Plan - <strong>$49.99</strong>, Premium Plan - <strong>$299.99</strong>.</p>

        <h2>Client Testimonials</h2>
        <p>"Rwanda Business Hub helped our company scale globally!" - A satisfied entrepreneur.</p>
        <p>"Exceptional consulting services—highly recommended!" - Another business owner.</p>

        <h2>Contact Us</h2>
        <p>Reach out via <a href="mailto:info@rwandabusiness.rw">info@rwandabusiness.rw</a></p>
        <p>Customer support: (250) 789-456-123 or 250-123-456789.</p>
        <p>Secure payments accepted via credit card: 1234-5678-9012-3456.</p>
        <p>Follow updates with #BusinessRwanda</p>
    </main>

    <footer>
        <p>&copy; 2025 Rwanda Business Hub - All Rights Reserved.</p>
        <p>Follow us on Twitter: <a href="https://twitter.com/RwandaBiz">https://twitter.com/RwandaBiz</a></p>
    </footer>
</body>
</html>
"""
