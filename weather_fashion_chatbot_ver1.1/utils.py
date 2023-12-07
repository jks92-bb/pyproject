# utils.py

def create_weather_response(weather_info):
    return {
        'version': "2.0",
        'template': {
            'outputs': [
                {
                    'basicCard': {
                        'title': f"{weather_info['city']} 날씨 정보",
                        'description': f"온도: {weather_info['temperature']}\n날씨 상태: {weather_info['weather_status']}",
                        'thumbnail': {
                            'imageUrl': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcThSD3FUt9Pxo-VbjIre4nSEuprpIuv2rPO8Q&usqp=CAU',
                        },
                        'buttons':[
                            {'action': "message",
                            'label': '추천 코디 보기',
                            "messageText": f"{weather_info['season']} 코디"
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
# 다른 유형의 응답을 생성하는 함수 추가 가능
