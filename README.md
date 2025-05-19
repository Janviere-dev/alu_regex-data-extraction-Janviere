# **Business Data Extraction API (Regex-Powered)**

## **Project Overview**
This project is a **Regex-based API** designed to **automatically extract structured data** from a sample business website.  
It scans website content and identifies key business-related information, including:

- **Emails** – Contact details used in the business website.  
- **URLs** – Links to different pages of the company website.  
- **Phone Numbers** – Customer support or official contact numbers.  
- **Credit Card Numbers** – Example payment details for secure transactions.  
- **Currency Amounts** – Extracted financial pricing details from the website.  
- **HTML Tags** – Useful for analyzing the webpage structure.  

The extracted data is **saved in a text file (`extracted_info.txt`)** for future reference.

## **How This Project Works**
1** It defines regex patterns** to locate business-related information inside web content.  
2**It applies these patterns** to a simulated business website (Rwanda Business Hub).  
3 **Extracted data is displayed on the console** and saved automatically.  

The main goal of this API is to **simulate a real-world business data extraction process**  
using **Python's Regular Expressions (`re` module)** for structured information retrieval.

---

## **Setup Instructions**

### **1. Install Python**
Ensure you have **Python 3.x** installed. You can check by running:
```bash
python --version
```
If you don’t have Python installed, download it from [Python's official website](https://www.python.org/downloads/).

### **2. Clone or Download the Project**
If the project is hosted on **GitHub**, run the following command:
```bash
git clone <repository-url>
cd <repository-folder>
```
Alternatively, you can **download the ZIP file** and extract it manually.

### **3. No Additional Dependencies Required!**
This script **only uses Python’s built-in `re` module**, meaning you **don’t need to install anything extra**.

### **4. Run the Script**
Once inside the project folder, execute:
```bash
python regex_extractor.py
```
This will **process the business website content and extract key details**.

### **5. View the Extracted Data**
After running the script, extracted data will be saved in:
```plaintext
extracted_info.txt
```
You can open the file to see structured business details extracted from the web content.

---

## **Example of Extracted Data**
```
===== Extracted Information from Rwanda Business Hub =====

Emails:
   - info@rwandabusiness.rw

URLs:
   - https://www.rwandabusiness.rw/home
   - https://www.rwandabusiness.rw/services
   - https://www.rwandabusiness.rw/contact

Phone Numbers:
   - (250) 789-456-123
   - 250-123-456789

 Credit Cards:
   - 1234-5678-9012-3456

 Currency Amounts:
   - $49.99
   - $299.99

🏷 HTML Tags:
   - `<h1>Welcome to Rwanda Business Hub</h1>`
```

---

## **Understanding How Regex Works in This Project**
### **Regular Expressions Used**
| **Data Type** | **Regex Pattern Used** |
|--------------|----------------------|
| Emails | `\b[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}\b` |
| URLs | `\b(?:https?|ftp)?://(?:www\.)?[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}(?:\/[^\s]*)?\b` |
| Phone Numbers | `\+?\d{1,3}?[\s-]?\(?\d{3}\)?[\s.-]?\d{3}[\s.-]?\d{4}\b` |
| Credit Cards | `\b(?:\d{4}[- ]?){3}\d{4}|\d{16}\b` |
| Currency Amounts | `(?:\$|RWF|USD|EUR)\s?\d{1,3}(?:,\d{3})*(?:\.\d{2})?` |
| HTML Tags | `<[^>]+>` |

Each pattern is **optimized** to recognize different formats and **handle edge cases** for maximum accuracy.

---

## **Future Enhancements**
- **Allow real-time web scraping** for live websites using `BeautifulSoup`.  
-  **Expand currency formats** to support additional symbols (GBP, KES, etc.).  
- **Improve regex accuracy** with more advanced patterns for better extraction.

---

## **Contributions**
Feel free to **fork**, **improve**, or **suggest new features** for this project!  
If you’d like to **collaborate**, submit a pull request or contact me  

---

## **License**
This project is **open-source** and licensed under the **MIT License**.  
Use it freely for **educational, research, or personal development purposes**.

---


