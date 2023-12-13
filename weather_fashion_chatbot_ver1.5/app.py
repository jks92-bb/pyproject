# app.py

from flask import Flask, request, jsonify
import urllib.parse
from modules.weather import get_weather_info
from modules.utils import create_not_signal_response, create_weather_response, create_codi_response, create_HowToUse_response, create_UserInput_response, create_fallback_response, create_news_response, create_HowToCodi_response, create_answer_response
from modules.codi import get_codi_by_season
from modules.news_scraper import get_fashion_codi_news

application = Flask(__name__)

@application.route("/hellokakao", methods=["POST"])
def hello_kakao():
    req = request.get_json()
    my_req = req["userRequest"]["utterance"]
    print(req)

    response = None

    if "날씨" in my_req:
        city = my_req.split("날씨")[0].strip()
        if city:
            weather_info = get_weather_info(city)
            if weather_info['location'] == "VIEW":
                response = create_not_signal_response()
            else:
                response = create_weather_response(weather_info)
        else:
            response = create_not_signal_response()
    elif "코디" in my_req and ("남자" in my_req or "여자" in my_req):
        # Extract season keyword from the user's utterance
        gender_keywords = ["남자","여자"]
        season_keywords = ["따뜻한", "가벼운", "시원한", "따스한"]
        gender = next((g.strip() for g in gender_keywords if g in my_req), None)
        season = next((s.strip() for s in season_keywords if s in my_req), None)

        if gender and season:
            recommended_codi, image_url, item_link = get_codi_by_season(gender, season)
            response = create_codi_response(recommended_codi, image_url, item_link)
        else:
            response = response = create_fallback_response()
    elif "패션 예보 사용법" in my_req:
        response = create_HowToUse_response(my_req)
    elif "일기예보 알려줘" in my_req:
        response = create_UserInput_response(my_req)
    elif "패션 뉴스" in my_req:
        response = create_answer_response(my_req)
    elif "연결해줘" in my_req:
        news_data = get_fashion_codi_news()
        response = create_news_response(news_data)
    elif "코디 잘 하는 법" in my_req:
        response = create_HowToCodi_response(my_req)
    else:
        # 폴백 응답 사용
        response = create_fallback_response()
    return jsonify(response)

if __name__ == "__main__":
    application.run(host='0.0.0.0', port=5000)
