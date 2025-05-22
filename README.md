# Regex Data Extraction Tool

## Cloning This Project in VS Code
Hello! Welcome to my **Regex Data Extraction Tool** repository.  
To get started, **clone this repository** and open it in **VS Code**:
git clone https://github.com/your-repo-name/Regex-Data-Extraction-Tool.git

Once inside the project folder, open **VS Code** and navigate to the workspace.

## Setup Instructions

### **Prerequisites**
Before running this tool, make sure you have **Python 3.x** installed.

## Project Overview
This project is designed to **extract, validate, and categorize data** from website files using **regular expressions (regex).** It processes various data types, including:
- **Emails**
- **URLs**
- **Phone Numbers**
- **Credit Card Numbers**
- **Currency Amounts**
- **Hashtags**
- **Time Formats**

Additionally, it lets users **manually enter data** for extraction.

---

## Folder Structure
```
|── Regex-Data-Extraction-Tool
│   ├── regex.py         # Main script handling extraction and user input
│   ├── test_regex.py    # Script for validating regex patterns
│   ├── sample_websites  # Folder containing website files for testing
│   ├── error_log.txt    # Stores invalid extracted data
│   ├── README.md        # Documentation file (this one!)
```

---

## Running the Tool in **VS Code**
1. **Open VS Code** and navigate to the project folder.
2. Open the **Integrated Terminal** (`Ctrl + ~`).
3. **Run the extraction script**:
   ```sh
   python regex.py
   ```
4. Follow the interactive prompts to **extract or validate data**.

---

** How Files Are Generated  
Once you run regex.py, the script will automatically extract and categorize data into separate files. These files are created inside the project directory, depending on the type of data found.
For example:
- Extracted email addresses will be saved in emails_data.txt.
- Extracted URLs will be stored in urls_data.txt.
- Invalid or misformatted entries will be logged in error_log.txt.
After running the script, these files will be visible in the same directory. You can open and review them using any text editor.


## Running Regex Tests
To test whether the regex patterns correctly validate expected data, run:
```sh
python test_regex.py
```
This will assess if the regex patterns match the expected formats.

---

## How to Test the Extraction Process
 **Extracts data from sample website files** (`sample_websites` folder)  
 **Logs extracted data into categorized files** (`emails_data.txt`, `urls_data.txt`, etc.)  
 **Detects format errors and logs them into `error_log.txt`**  
 **Allows manual user input for validation**  

### **Expected Output Example**
```
Welcome to the Regex Data Extraction Tool! 
Processing: example.html...
 Extracted Emails: user@example.com
 Extracted URLs: https://www.example.com
 Extracted Phone Numbers: (123) 456-7890

Enter data manually or display extracted results.
```

---

## Contributing
If you’d like to improve this project, feel free to **fork the repository and submit pull requests!**

---

## License
This project is licensed under the MIT License, meaning you are free to:
- Use it for personal or commercial projects.
- Modify and distribute it as needed.
- Share your own improvements through contributions.

  

```

---
