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
                            'label': '열어보기',
                            "messageText": f"{weather_info['season']}코디"
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
                        "description": f"오늘 같은 날엔 {recommended_codi} 코디를 추천 드려요!\n",
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

# 다른 유형의 응답을 생성하는 함수 추가 가능