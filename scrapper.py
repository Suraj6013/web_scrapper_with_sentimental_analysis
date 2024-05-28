import os
import pandas as pd
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse, urljoin

# Function to extract article text from a given URL
def extract_article_text(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Extract article title
    title = soup.title.text.strip()

    # Extract article text
    article_text = ''
    article_body = soup.find('body')
    if article_body:
        paragraphs = article_body.find_all('p')
        for paragraph in paragraphs:
            article_text += paragraph.text.strip() + '\n'

    return title, article_text

# Load URLs from the Excel file
excel_file_path = r'C:\Users\suraj\OneDrive\Desktop\web_crawler\Input.xlsx'
df = pd.read_excel(excel_file_path)


output_folder = r'C:\Users\suraj\OneDrive\Desktop\web_crawler\output_txt_files'
os.makedirs(output_folder, exist_ok=True)

# Loop through each row in the DataFrame
for index, row in df.iterrows():
    url = row['URL']
    url_id = row['URL_ID']  # Use the URL_ID from the Excel file

    # Make a request to the URL and extract article title and text
    try:
        title, article_text = extract_article_text(url)
    except Exception as e:
        print(f"Error extracting data from {url}: {str(e)}")
        continue

    # Save the extracted article text to a text file in the output folder
    output_file_path = os.path.join(output_folder, f'{url_id}.txt')
    with open(output_file_path, 'w', encoding='utf-8') as file:
        file.write(f'Title: {title}\n\n')
        file.write(article_text)

    print(f"Article from {url} saved to {output_file_path}")
