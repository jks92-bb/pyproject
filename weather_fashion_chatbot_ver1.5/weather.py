# weather.py

from bs4 import BeautifulSoup
import urllib
import ssl
import random

def get_weather_info(city):
    # 입력받은 지역에 대한 날씨 정보 검색
    search_url = f'https://search.naver.com/search.naver?sm=top_hty&fbm=0&ie=utf8&query={urllib.parse.quote(city + "날씨")}'
    context = ssl._create_unverified_context()
    webpage = urllib.request.urlopen(search_url, context=context)
    soup = BeautifulSoup(webpage, 'html.parser')

    # 날씨 정보 추출
    location = soup.find('h2', 'title')
    temps = soup.find('div', 'temperature_text')
    c_temp = soup.find('strong', {'class': ''}).text
    summary = soup.find('p', 'summary')
    #misegroup = soup.find('div', {'class': 'report_card_wrap'})
    #mise2 = misegroup.findAll('li')

    # 온도 정보에서 숫자와 소수점만 추출하여 temperature 변수에 저장
    temperature = ''.join(filter(lambda x: x.isdigit() or x == '.', c_temp))

    # 추출한 온도 문자열을 실수형으로 변환
    try:
        temperatures = float(temperature)
    except ValueError:
        temperatures = None

    # 날씨 정보 변수 초기화
    weather = ''

    # 계절 설정
    if temperatures is not None:
        if 7 < temperatures < 20:
            # 랜덤으로 '가을' 또는 '봄' 선택
            weather = random.choice(['가벼운', '따스한'])
        elif temperatures <= 7:
            weather = '따뜻한'
        elif temperatures >= 20:
            weather = '시원한'

    return {
        'location': location.text.strip() if location else "지역 정보를 찾을 수 없습니다.",
        'city': city,
        'temperature': temps.text.strip() if temps else '온도 정보를 찾을 수 없습니다.',
        'weather_status': summary.text.strip() if summary else '날씨 상태 정보를 찾을 수 없습니다.',
        'season': weather,
    }
