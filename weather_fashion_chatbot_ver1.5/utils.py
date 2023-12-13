# utils.py

from modules.news_scraper import get_fashion_codi_news

def create_weather_response(weather_info):
    return {
        'version': "2.0",
        'template': {
            'outputs': [
                {
                    'basicCard': {
                        'title': f"({weather_info['city']}) {weather_info['location']} 정보",
                        'description': f"온도: {weather_info['temperature']}\n날씨 상태: {weather_info['weather_status']}",
                        'thumbnail': {
                            'imageUrl': 'https://img.freepik.com/premium-vector/set-of-weather-doodles-illustration_6997-2189.jpg',
                        },
                        'buttons':[
                            {'action': "message",
                            'label': '남자 추천 코디 보기',
                            "messageText": f"남자 {weather_info['season']} 코디"
                            },
                            {'action': "message",
                             'label': '여자 추천 코디 보기',
                             "messageText": f"여자 {weather_info['season']} 코디"
                             }
                        ]
                    }
                }
            ]
        }
    }

def create_codi_response(recommended_codi, image_url, item_link):
    return {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "basicCard": {
                        'title': f"{recommended_codi} 코디 추천",
                        "description": f"오늘 같은 날엔 이런 코디 어때요?\n",
                        "thumbnail": {
                            "imageUrl": image_url
                        },
                        'buttons': [
                            {
                                "action": "webLink",
                                "label": "구매링크",
                                "webLinkUrl": item_link
                            }
                        ]
                    }
                }
            ]
        }
    }

def create_HowToUse_response(image_url):
    return {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "basicCard": {
                        'title': f"패션 예보 사용법",
                        "description": f"날씨에 따른 패션을 추천해드립니다. \n채팅방 메뉴에 '날씨&코디'를 눌러서 \n사용 할 수 있습니다. \n자세한 사용법은 사용법을 확인해주세요!",
                        "thumbnail": {
                            "imageUrl": 'https://images.pexels.com/photos/5428836/pexels-photo-5428836.jpeg?auto=compress&cs=tinysrgb&w=1600'
                        }
                    }
                }
            ]
        }
    }

def create_UserInput_response(image_url):
    return {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "basicCard": {
                        'title': f"현재 계신 곳을 말씀해주세요!",
                        "description": f"예시) 서울 날씨 \n이런 식으로 말씀해주시면 좋아요!",
                        "thumbnail": {
                            "imageUrl": 'https://img.freepik.com/premium-vector/breaking-news-reporter-background-vector-illustration-with-broadcaster-or-journalist-on-the-monitor-about-information-incident-activities-weather-and-announcements_2175-872.jpg'
                        }
                    }
                },
                {
                    "basicCard": {
                        'title': "기상 캐스터를 보낼 준비 중 입니다!",
                        "description": "현장에 있는 기자와 연결하기 위해 \n말씀 후, 5초만 기다려주세요!\n",
                        "thumbnail": {
                            "imageUrl": 'https://img.freepik.com/premium-vector/breaking-news-reporter-background-vector-illustration-with-broadcaster-or-journalist-on-the-monitor-about-information-incident-activities-weather-and-announcements_2175-873.jpg'
                        }
                    }
                }
            ]
        }
    }

def create_fallback_response():
    return {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "basicCard": {
                        'title': f"너무 죄송해요...",
                        "description": f"제가 아직 모자른가봐요 ㅠㅠ \n원하시는 것을 좀 더 정확하게 \n말씀해주시면 더 좋을 것 같아요!",
                        "thumbnail": {
                            "imageUrl": 'https://media.istockphoto.com/id/1431297006/ko/%EB%B2%A1%ED%84%B0/%EC%96%91%EB%B3%B5%EC%9D%84-%EC%9E%85%EA%B3%A0-%EC%A0%88%ED%95%98%EA%B3%A0-%EC%82%AC%EA%B3%BC%ED%95%98%EB%8A%94-%EC%97%AC%EC%84%B1%EC%9D%98-%EA%B7%B8%EB%A6%BC.jpg?s=612x612&w=0&k=20&c=KhYUITknvHgv-hGGL7vEknC8_ylM-uKeeNBk5bnmU50='
                        }
                    }
                }
            ]
        }
    }

def create_not_signal_response():
    return {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "basicCard": {
                        'title': f"캐스터를 파견 할 수 없습니다.",
                        "description": f"파견 가능한 지역을 말씀해주세요!",
                        "thumbnail": {
                            "imageUrl": 'https://www.urbanbrush.net/web/wp-content/uploads/edd/2021/04/urbanbrush-20210413210546217768.jpg'
                        }
                    }
                }
            ]
        }
    }

def create_news_response(news_data):
    if news_data:
        cards = []
        for article in news_data:
            cards.append({
                "title": article['title'],
                "description": article['description'],
                "thumbnail": {
                    "imageUrl": article['image_url']
                },
                "buttons": [
                    {
                        "action": "webLink",
                        "label": "기사 읽기",
                        "webLinkUrl": article['link']
                    }
                ]
            })

        return {
            "version": "2.0",
            "template": {
                "outputs": [
                    {
                        "carousel": {
                            "type": "basicCard",
                            "items": cards
                        }
                    }
                ]
            }
        }
    else:
        return {
            "version": "2.0",
            "template": {
                "outputs": [
                    {
                        "simpleText": {
                            "text": "코디 관련 기사를 찾을 수 없습니다."
                        }
                    }
                ]
            }
        }

def create_HowToCodi_response(image_url):
    return {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "basicCard": {
                        'title': f"코디 잘 하는 법",
                        "description": f"코디가 고민이시다구요? \n영상을 확인해 코디법을 한번 살펴보세요!",
                        "thumbnail": {
                            "imageUrl": 'https://post-phinf.pstatic.net/MjAyMDExMTBfMTg5/MDAxNjA0OTk1MjI0OTY3.zYTx-ndo3Cyp7PmTHLRTKwDCDwfR3koTN1XQ8P5raigg.vrjQqvqMJjZ7wx1_NkVtiLZGKXvc8QxHikEnUlMqdPcg.PNG/%EB%8C%80%EC%A7%80_1.png?type=w800_q75'
                        },
                        'buttons':[
                            {'action': "webLink",
                            'label': '남자 코디 하는 법',
                            "webLinkUrl": "https://www.youtube.com/watch?v=r9_rbkETWoM"
                            },
                            {'action': "webLink",
                             'label': '여자 코디 하는 법',
                             "webLinkUrl": "https://www.youtube.com/watch?v=Roj7Wi_flv4"
                             }
                        ]
                    }
                }
            ]
        }
    }

def create_answer_response(image_url):
    return {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "basicCard": {
                        'title': f"패션 캐스터를 보낼 준비 중 입니다!",
                        "description": f"현장에 있는 기자와 연결하기 위해 \n말씀 후, 5초만 기다려주세요!\n",
                        "thumbnail": {
                            "imageUrl": 'https://i.pinimg.com/736x/0f/60/92/0f609243f81410b663069d1633f93564.jpg'
                        },
                        'buttons':[
                            {'action': "message",
                            'label': '캐스터와 연결 하시겠습니까?',
                            "messageText": "연결해줘"
                            },
                        ]
                    }
                }
            ]
        }
    }
