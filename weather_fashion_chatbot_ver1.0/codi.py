import random


def get_codi_by_season(season):
    codi = None
    image_url = None
    item_links = None  # 추가된 부분

    if season == "겨울":
        codi = ["겨울 셋업", "러블리 겨울", "컬러 포인트 겨울", "파스텔 겨울", "스포츠 겨울"]
    elif season == "가을":
        codi = ["가을 니트", "완벽한 가을", "가을 데이트", "가을 아메카지 룩", "가을 무드 완성"]
    elif season == "여름":
        codi = ["여름엔 데님", "여름엔 이렇게", "여름에 딱이야", "심플한 여름", "쿨한 여름"]
    elif season == "봄":
        codi = ["봄 캐쥬얼 룩", "봄 데이트", "화사한 봄", "봄 맞이 스타일링", "봄 느낌 물씬"]
    else:
        codi = ["다양한 스타일"]

    selected_codi = random.choice(codi)

    # 이미지 URL 설정
    image_urls = {
        "겨울 셋업": "https://image.msscdn.net/images/codimap/detail/28463/detail_28463_1_500.jpg?202312051412",
        "러블리 겨울": "https://image.msscdn.net/images/codimap/detail/28376/detail_28376_2_500.jpg?202312051412",
        "컬러 포인트 겨울": "https://image.msscdn.net/images/codimap/detail/27681/detail_27681_1_500.jpg?202312051412",
        "파스텔 겨울": "https://image.msscdn.net/images/codimap/detail/27648/detail_27648_2_500.jpg?202312051412",
        "스포츠 겨울": "https://image.msscdn.net/images/codimap/detail/20556/detail_20556_1_500.jpg?202312051412",
        "가을 니트": "https://image.msscdn.net/images/codimap/detail/26535/detail_26535_1_500.jpg?202312051412",
        "완벽한 가을": "https://image.msscdn.net/images/codimap/detail/26257/detail_26257_1_500.jpg?202312051512",
        "가을 데이트": "https://image.msscdn.net/images/codimap/detail/25840/detail_25840_1_500.jpg?202312051512",
        "가을 아메카지 룩": "https://image.msscdn.net/images/codimap/detail/19344/detail_19344_1_500.jpg?202312051512",
        "가을 무드 완성": "https://image.msscdn.net/images/codimap/detail/8747/detail_8747_1_500.jpg?202312051512",
        "여름엔 데임": "https://image.msscdn.net/images/codimap/detail/23513/detail_23513_1_500.jpg?202312051512",
        "여름엔 이렇게": "https://image.msscdn.net/images/codimap/detail/23291/detail_23291_1_500.jpg?202312051512",
        "여름에 딱이야": "https://image.msscdn.net/images/codimap/detail/16682/detail_16682_1_500.jpg?202312051512",
        "심플한 여름": "https://image.msscdn.net/images/codimap/detail/4740/detail_4740_1_500.jpg?202312051512",
        "쿨한 여름": "https://image.msscdn.net/images/codimap/detail/3879/detail_3879_1_500.jpg?202312051512",
        "봄 캐쥬얼 룩": "https://image.msscdn.net/images/codimap/detail/22619/detail_22619_1_500.jpg?202312051512",
        "봄 데이트": "https://image.msscdn.net/images/codimap/detail/21845/detail_21845_1_500.jpg?202312051512",
        "화사한 봄": "https://image.msscdn.net/images/codimap/detail/14942/detail_14942_1_500.jpg?202312051512",
        "봄 맞이 스타일링": "https://image.msscdn.net/images/codimap/detail/14403/detail_14403_1_500.jpg?202312051512",
        "봄 느낌 물씬": "https://image.msscdn.net/images/codimap/detail/13955/detail_13955_1_500.jpg?202312051512"
    }
    
    item_links = {
        "겨울 셋업": "https://www.musinsa.com/app/codimap/views/28463",
        "러블리 겨울": "https://www.musinsa.com/app/codimap/views/28376",
        "컬러 포인트 겨울": "https://www.musinsa.com/app/codimap/views/27681",
        "파스텔 겨울": "https://www.musinsa.com/app/codimap/views/27648",
        "스포츠 겨울": "https://www.musinsa.com/app/codimap/views/20556",
        "가을 니트": "https://www.musinsa.com/app/codimap/views/26535",
        "완벽한 가을": "https://www.musinsa.com/app/codimap/views/26257",
        "가을 데이트": "https://www.musinsa.com/app/codimap/views/25840",
        "가을 아메카지 룩": "https://www.musinsa.com/app/codimap/views/18881",
        "가을 무드 완성": "https://www.musinsa.com/app/codimap/views/8747",
        "여름엔 데임": "https://www.musinsa.com/app/codimap/views/23513",
        "여름엔 이렇게": "https://www.musinsa.com/app/codimap/views/17598",
        "여름에 딱이야": "https://www.musinsa.com/app/codimap/views/16682",
        "심플한 여름": "https://www.musinsa.com/app/codimap/views/4740",
        "쿨한 여름": "https://www.musinsa.com/app/codimap/views/3879",
        "봄 캐쥬얼 룩": "https://www.musinsa.com/app/codimap/views/22619",
        "봄 데이트": "https://www.musinsa.com/app/codimap/views/14137",
        "화사한 봄": "https://www.musinsa.com/app/codimap/views/14841",
        "봄 맞이 스타일링": "https://www.musinsa.com/app/codimap/views/14403",
        "봄 느낌 물씬": "https://www.musinsa.com/app/codimap/views/14871"
    }

    image_url = image_urls.get(selected_codi, "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTx9cTPon4vY8hARZEH82VaeKY7K2ymGYeYoi89tnB_epPpLEKc84DUhaDnOR8OiHwn6-U&usqp=CAU")  # 선택된 코디에 대한 이미지 URL 가져오기
    item_link = item_links.get(selected_codi, "https://example.com/default_item_link")  # 선택된 코디에 대한 링크 가져오기
    
    return selected_codi, image_url, item_link