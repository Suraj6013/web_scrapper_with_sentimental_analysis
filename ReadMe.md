# Web Scraper
This is a simple web scraper written in Python. It reads a list of URLs from an Excel file, makes HTTP requests to each URL, extracts the article title and text from each page, and saves the extracted text to a text file.

## Requirements
- Python 3.6+
- pandas
- os

## Usage
1. Prepare an Excel file with a list of URLs to scrape. The file should have a column named 'URL' for the URLs and 'URL_ID' for unique identifiers of each URL.
2. Update the `excel_file_path` variable in `scrapper.py` with the path to your Excel file.
3. Update the `output_folder` variable in `scrapper.py` with the path to the folder where you want to save the output text files.
4. Run `scrapper.py`.

## Error Handling
If an error occurs while extracting data from a URL, the error message will be printed to the console, and the script will continue with the next URL.

## Output
The extracted text from each URL will be saved to a separate text file in the output folder. The name of the text file will be the URL_ID from the Excel file.

# Sentiment Analysis 
Here we perform sentiment analysis on a set of text files. Here's a brief overview of how it works:

## Initialization
The script starts by initializing variables to store the total positive and negative scores, and the number of files processed.

## File Processing
The script then iterates over each file in the specified folder. If the file is a text file, it reads the content of the file and converts it to lowercase.

## Sentiment Analysis
The script calculates the positive and negative scores for each file by counting the number of positive and negative words in the text.

## Score Aggregation
The script aggregates the scores by adding the positive and negative scores to the total scores. It also increments the count of processed files.

## Results Display
Finally, the script prints the number of files processed, the total positive score, the total negative score, and the total number of words.

