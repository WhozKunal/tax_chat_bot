import requests
from bs4 import BeautifulSoup

# URL of the FAQ page
url = 'https://incometaxindia.gov.in/pages/faqs.aspx'

# Fetch the page content
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

# Debugging: Print the page to understand its structure
print(soup.prettify())  # This will print the entire HTML structure

# Look for specific elements after inspecting HTML
faq_sections = soup.find_all('div', class_='faq-content-class')  # Replace with correct class name

# Extract FAQ content
faqs = []
for section in faq_sections:
    question = section.find('h3').get_text(strip=True)
    answer = section.find('p').get_text(strip=True)
    faqs.append({'question': question, 'answer': answer})

# Print the FAQ content
for faq in faqs:
    print(f"Q: {faq['question']}")
    print(f"A: {faq['answer']}")
    print("-" * 40)
