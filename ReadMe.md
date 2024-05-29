# Web Scraper
This is a simple web scraper written in Python. It reads a list of URLs from an Excel file, makes HTTP requests to each URL, extracts the article title and text from each page, and saves the extracted text to a text file.

# Requirements
- Python 3.6+
- pandas
- os

# Usage
1. Prepare an Excel file with a list of URLs to scrape. The file should have a column named 'URL' for the URLs and 'URL_ID' for unique identifiers of each URL.
2. Update the `excel_file_path` variable in `scrapper.py` with the path to your Excel file.
3. Update the `output_folder` variable in `scrapper.py` with the path to the folder where you want to save the output text files.
4. Run `scrapper.py`.

# Error Handling
If an error occurs while extracting data from a URL, the error message will be printed to the console, and the script will continue with the next URL.

# Output
The extracted text from each URL will be saved to a separate text file in the output folder. The name of the text file will be the URL_ID from the Excel file.