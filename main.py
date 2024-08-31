import requests
from bs4 import BeautifulSoup


KEYWORDS = ['дизайн', 'фото', 'web', 'python']

response = requests.get('https://habr.com/ru/all/')
soup = BeautifulSoup(response.text, 'html.parser')

posts = soup.find_all('article', class_='tm-articles-list__item')
for post in posts:
    date_element = post.find('time')
    date = date_element.attrs.get('title') if date_element else 'Неизвестно'
    title_element = post.find('a', class_='tm-article-snippet__title-link')
    title = title_element.text if title_element else 'Без названия'
    link = 'https://habr.com' + title_element.attrs.get('href') if title_element else '#'
    preview_text = post.text.lower()
    if any(keyword.lower() in preview_text for keyword in KEYWORDS):
        print(f'{date} – {title} – {link}')
