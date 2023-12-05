# chatbot.py

from flask import Flask, request, jsonify
import urllib.parse
from weather import get_weather_info
from utils import create_weather_response, create_codi_response
from codi import get_codi_by_season


application = Flask(__name__)

@application.route("/")
def hello():
    return "Hello goorm!"

@application.route("/hellokakao", methods=["POST"])
def hello_kakao():
    req = request.get_json()
    my_req = req["userRequest"]["utterance"]
    print(req)

    response = None

    if "날씨" in my_req:
        city = my_req.split("날씨")[1].strip()
        weather_info = get_weather_info(city)
        response = create_weather_response(weather_info)
    elif "코디" in my_req:
        # Extract season keyword from the user's utterance
        season_keywords = ["겨울", "가을", "여름", "봄"]
        season = next((s.strip() for s in season_keywords if s in my_req), None)

        if season:
            recommended_codi, image_url, item_link = get_codi_by_season(season)
            response = create_codi_response(recommended_codi, image_url, item_link)
        else:
            response = {"error": "계절 키워드를 찾을 수 없습니다."}
            
    return jsonify(response)

if __name__ == "__main__":
    application.run(host='0.0.0.0', port=5000)
