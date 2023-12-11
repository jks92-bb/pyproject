# news_scraper.py

import requests
from bs4 import BeautifulSoup

def get_fashion_codi_news(num_articles=5):
    search_url = 'https://search.naver.com/search.naver'
    params = {
        'query': '셀럽 코디',
        'where': 'news',
        'start': 1,
    }
    response = requests.get(search_url, params=params)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        articles = soup.select('.news_area')[:num_articles]
        news_data = []

        for article in articles:
            title = article.select_one('.news_tit').get('title')
            link = article.select_one('.news_tit').get('href')

            # 기사 내용 페이지로 이동
            article_page = requests.get(link)
            article_soup = BeautifulSoup(article_page.text, 'html.parser')

            # 기사 내용 페이지에서 이미지 URL, 요약, 날짜 가져오기
            image_tag = article_soup.find('meta', {'property': 'og:image'})
            image_url = image_tag['content'] if image_tag else None

            description_tag = article_soup.find('meta', {'name': 'description'})
            description = description_tag['content'] if description_tag else None

            date_tag = article_soup.find('meta', {'property': 'article:published_time'})
            date = date_tag['content'] if date_tag else None

            # 기사 내용 가져오기
            content_tag = article_soup.find('div', {'id': 'articleBodyContents'})
            content = content_tag.text.strip() if content_tag else None

            news_data.append({
                'title': title,
                'link': link,
                'image_url': image_url,
                'description': description,
                'date': date,
                'content': content
            })

        return news_data
    else:
        return None
