# codi.py

import random

def get_codi_by_season(gender,season):
    codi = None
    image_url = None
    item_links = None  # 추가된 부분

    if gender == "남자":
        if season == "따뜻한":
            codi = ["겨울 셋업", "러블리 겨울", "컬러 포인트 겨울", "파스텔 겨울", "스포츠 겨울"]
        elif season == "가벼운":
            codi = ["가을 니트", "완벽한 가을", "가을 데이트", "가을 아메카지 룩", "가을 무드 완성"]
        elif season == "시원한":
            codi = ["여름엔 데님", "여름엔 이렇게", "여름에 딱이야", "심플한 여름", "쿨한 여름", "데이트 룩"]
        elif season == "따스한":
            codi = ["봄 캐쥬얼 룩", "봄 데이트", "화사한 봄", "봄 맞이 스타일링", "봄 느낌 물씬", "봄 캠퍼스 코디", "봄을 닮은 코디"]
        else:
            codi = ["다양한 스타일"]
    if gender == "여자":
        if season == "따뜻한":
            codi = ["더플코트로 완성", "코듀로이 팬츠 활용법", "블랙 앤 화이트 룩",
                    "테일리 올드머니 룩", "뉴트럴 톤 아메카지", "추천, 캠퍼스 룩", "코트 포기 못 해", "한 끗 다른 컬러 믹스", "러블리 트위드 셋업", "데일리 스트릿 패션",
                    "한파 속 스트릿 룩", "유니크한 컬러 매치", "뉴트럴 톤 코디", "핑크로 기분UP", "루즈 핏 무스탕 연출법", "빈티지 느낌 물씬", "레드로 컬러 포인트",
                    "유니크한 포멀 룩", "톤온톤의 우아함", "올블랙 코디법", "걸리시 코디", "디테일에 시선 집중", "플리스 재킷 스타일링", "캐주얼도 시크하게", "트위드 셋업 코디",
                    "추울수록 힙하게", "일상의 포멀 룩", "손이 가는 컬러 매치", "추워도 치마 포기 못해", "원피스 레이어드하기", "포멀과 캐주얼 사이", "모노톤 출근 룩", "파스텔 컬러 포인트",
                    "주말 데이트 룩", "편안한 셋업 코디", "비즈니스 캐주얼 룩", "겨울철 숏 팬츠 코디법", "숏 패딩 연출법", "한겨울 원 마일 웨어", "은은한 컬러 포인트", "맥시스커트 활용법", "매력적인 아메카지 룩", "뉴트럴 톤 출근 룩"]
        elif season == "가벼운":
            codi = ["올 블랙 시크 코디", "니트 코디 여친 룩", "아이템 포인트 주기", "니트와 레더 조합", "커리어 우먼 무드", "유니크한 아우터", "카고 스타일링", "원피스 레이어링", "실루엣이 돋보여", "출근 룩 추천", "이렇게 입어봐",
                    "요즘 날씨에 딱이야", "걸리시 아우터 룩", "키치함 가득", "우아한 출근길", "편하지만 센스있게", "레더 코디 제안", "셔링 원피스 코디", "러블리한 조합", "차분한 룩"]
        elif season == "시원한":
            codi = ["셔링 캐주얼의 끝", "시크 포인트로 룩 완성", "출근 룩의 정석", "사랑스러운 룩", "로맨틱 모멘트", "데이트 가기 딱 좋아", "때론 섹시하게", "럭셔리한 디테일", "스포티 캠핑 룩 날 봐", "네온 온 미", "그레이 고프코어 룩",
                    "오늘의 룩", "귀여워 보이고 싶다면", "단정함이 베스트", "사랑스러워", "리본으로 완성", "러블리하게", "오늘의 주인공", "가방에 주목", "주말 룩으로 결정", "믹스 앤 매치", "서머 페스티벌", "블록코어의 인기", "대세는 고프코어",
                    "시크한 멋", "우산 챙기세요"]
        elif season == "따스한":
            codi = [ "매력적인 코디", "센스 넘쳐", "찰떡이야", "멋스러운 출근 룩", "워너비 스타일", "올 블랙 러버", "편한 게 최고", "트렌디한 걸리시룩", "무심하게 툭", "트렌디 아이템", "베스트 활용법", "스타일리시한 조합",
                     "인기 브랜드 픽", "로맨틱 무드", "센스 있는 매치", "카디건 스타일링", "추천 브랜드", "레더 재킷 연출 법"]
        else:
            codi = ["다양한 스타일"]


    selected_codi = random.choice(codi)

    # 이미지 URL 설정
    image_urls = {
        
        #여자 겨울
        "더플코트로 완성": "https://image.msscdn.net/images/codimap/detail/28663/detail_28663_1_500.jpg",
        "코듀로이 팬츠 활용법": "https://image.msscdn.net/images/codimap/detail/28662/detail_28662_1_500.jpg",
        "블랙 앤 화이트 룩": "https://image.msscdn.net/images/codimap/detail/28661/detail_28661_1_500.jpg",
        "테일리 올드머니 룩": "https://image.msscdn.net/images/codimap/detail/28660/detail_28660_1_500.jpg",
        "뉴트럴 톤 아메카지": "https://image.msscdn.net/images/codimap/detail/28659/detail_28659_1_500.jpg",
        "추천, 캠퍼스 룩": "https://image.msscdn.net/images/codimap/detail/28658/detail_28658_1_500.jpg",
        "코트 포기 못 해": "https://image.msscdn.net/images/codimap/detail/28657/detail_28657_1_500.jpg",
        "한 끗 다른 컬러 믹스": "https://image.msscdn.net/images/codimap/detail/28656/detail_28656_1_500.jpg",
        "러블리 트위드 셋업": "https://image.msscdn.net/images/codimap/detail/28655/detail_28655_1_500.jpg",
        "데일리 스트릿 패션": "https://image.msscdn.net/images/codimap/detail/28654/detail_28654_1_500.jpg",
        "한파 속 스트릿 룩": "https://image.msscdn.net/images/codimap/detail/28653/detail_28653_1_500.jpg",
        "유니크한 컬러 매치": "https://image.msscdn.net/images/codimap/detail/28652/detail_28652_1_500.jpg",
        "뉴트럴 톤 코디": "https://image.msscdn.net/images/codimap/detail/28651/detail_28651_1_500.jpg",
        "핑크로 기분UP": "https://image.msscdn.net/images/codimap/detail/28650/detail_28650_1_500.jpg",
        "루즈 핏 무스탕 연출법": "https://image.msscdn.net/images/codimap/detail/28649/detail_28649_1_500.jpg",
        "빈티지 느낌 물씬": "https://image.msscdn.net/images/codimap/detail/28648/detail_28648_1_500.jpg",
        "레드로 컬러 포인트": "https://image.msscdn.net/images/codimap/detail/28647/detail_28647_1_500.jpg",
        "유니크한 포멀 룩": "https://image.msscdn.net/images/codimap/detail/28646/detail_28646_1_500.jpg",
        "톤온톤의 우아함": "https://image.msscdn.net/images/codimap/detail/28645/detail_28645_1_500.jpg",
        "올블랙 코디법": "https://image.msscdn.net/images/codimap/detail/28644/detail_28644_1_500.jpg",
        "걸리시 코디" : "https://image.msscdn.net/images/codimap/detail/28600/detail_28600_1_500.jpg",
        "디테일에 시선 집중" : "https://image.msscdn.net/images/codimap/detail/28599/detail_28599_1_500.jpg",
        "플리스 재킷 스타일링" : "https://image.msscdn.net/images/codimap/detail/28598/detail_28598_1_500.jpg",
        "캐주얼도 시크하게": "https://image.msscdn.net/images/codimap/detail/28597/detail_28597_1_500.jpg",
        "트위드 셋업 코디": "https://image.msscdn.net/images/codimap/detail/28596/detail_28596_1_500.jpg",
        "추울수록 힙하게": "https://image.msscdn.net/images/codimap/detail/28595/detail_28595_1_500.jpg",
        "일상의 포멀 룩": "https://image.msscdn.net/images/codimap/detail/28594/detail_28594_1_500.jpg",
        "손이 가는 컬러 매치": "https://image.msscdn.net/images/codimap/detail/28593/detail_28593_1_500.jpg",
        "추워도 치마 포기 못해": "https://image.msscdn.net/images/codimap/detail/28592/detail_28592_1_500.jpg",
        "원피스 레이어드하기": "https://image.msscdn.net/images/codimap/detail/28591/detail_28591_1_500.jpg",
        "포멀과 캐주얼 사이": "https://image.msscdn.net/images/codimap/detail/28590/detail_28590_1_500.jpg",
        "모노톤 출근 룩": "https://image.msscdn.net/images/codimap/detail/28589/detail_28589_1_500.jpg",
        "파스텔 컬러 포인트": "https://image.msscdn.net/images/codimap/detail/28588/detail_28588_1_500.jpg",
        "주말 데이트 룩": "https://image.msscdn.net/images/codimap/detail/28587/detail_28587_1_500.jpg",
        "편안한 셋업 코디": "https://image.msscdn.net/images/codimap/detail/28586/detail_28586_1_500.jpg",
        "비즈니스 캐주얼 룩": "https://image.msscdn.net/images/codimap/detail/28585/detail_28585_1_500.jpg",
        "겨울철 숏 팬츠 코디법": "https://image.msscdn.net/images/codimap/detail/28584/detail_28584_1_500.jpg",
        "숏 패딩 연출법": "https://image.msscdn.net/images/codimap/detail/28583/detail_28583_1_500.jpg",
        "한겨울 원 마일 웨어": "https://image.msscdn.net/images/codimap/detail/28582/detail_28582_1_500.jpg",
        "은은한 컬러 포인트": "https://image.msscdn.net/images/codimap/detail/28551/detail_28551_1_500.jpg",
        "맥시스커트 활용법": "https://image.msscdn.net/images/codimap/detail/28550/detail_28550_1_500.jpg",
        "매력적인 아메카지 룩": "https://image.msscdn.net/images/codimap/detail/28549/detail_28549_1_500.jpg",
        "뉴트럴 톤 출근 룩": "https://image.msscdn.net/images/codimap/detail/28548/detail_28548_1_500.jpg",
        #여자 가을
        "올 블랙 시크 코디": "https://image.msscdn.net/images/codimap/detail/27029/detail_27029_1_500.jpg",
        "아이템 포인트 주기": "https://image.msscdn.net/images/codimap/detail/27027/detail_27027_1_500.jpg",
        "니트 코디 여친 룩": "https://image.msscdn.net/images/codimap/detail/27026/detail_27026_1_500.jpg",
        "니트와 레더 조합" : "https://image.msscdn.net/images/codimap/detail/27025/detail_27025_1_500.jpg",
        "커리어 우먼 무드": "https://image.msscdn.net/images/codimap/detail/27024/detail_27024_1_500.jpg",
        "유니크한 아우터": "https://image.msscdn.net/images/codimap/detail/27023/detail_27023_1_500.jpg",
        "카고 스타일링": "https://image.msscdn.net/images/codimap/detail/27022/detail_27022_1_500.jpg",
        "원피스 레이어링": "https://image.msscdn.net/images/codimap/detail/27021/detail_27021_1_500.jpg",
        "실루엣이 돋보여": "https://image.msscdn.net/images/codimap/detail/26981/detail_26981_1_500.jpg",
        "출근 룩 추천": "https://image.msscdn.net/images/codimap/detail/26980/detail_26980_1_500.jpg",
        "이렇게 입어봐": "https://image.msscdn.net/images/codimap/detail/26979/detail_26979_1_500.jpg",
        "요즘 날씨에 딱이야": "https://image.msscdn.net/images/codimap/detail/26978/detail_26978_1_500.jpg",
        "걸리시 아우터 룩" : "https://image.msscdn.net/images/codimap/detail/26977/detail_26977_1_500.jpg",
        "키치함 가득": "https://image.msscdn.net/images/codimap/detail/26976/detail_26976_1_500.jpg",
        "우아한 출근길": "https://image.msscdn.net/images/codimap/detail/26975/detail_26975_1_500.jpg",
        "편하지만 센스있게": "https://image.msscdn.net/images/codimap/detail/26974/detail_26974_1_500.jpg",
        "레더 코디 제안" : "https://image.msscdn.net/images/codimap/detail/26973/detail_26973_1_500.jpg",
        "셔링 원피스 코디": "https://image.msscdn.net/images/codimap/detail/26972/detail_26972_1_500.jpg",
        "러블리한 조합" : "https://image.msscdn.net/images/codimap/detail/26971/detail_26971_1_500.jpg",
        "차분한 룩" : "https://image.msscdn.net/images/codimap/detail/26970/detail_26970_1_500.jpg",
        #여자 여름
        "셔링 캐주얼의 끝" : "https://image.msscdn.net/images/codimap/detail/25337/detail_25337_1_500.jpg",
        "시크 포인트로 룩 완성": "https://image.msscdn.net/images/codimap/detail/25336/detail_25336_1_500.jpg",
        "출근 룩의 정석": "https://image.msscdn.net/images/codimap/detail/25335/detail_25335_1_500.jpg",
        "사랑스러운 룩": "https://image.msscdn.net/images/codimap/detail/25334/detail_25334_1_500.jpg",
        "로맨틱 모멘트": "https://image.msscdn.net/images/codimap/detail/25333/detail_25333_1_500.jpg",
        "데이트 가기 딱 좋아" : "https://image.msscdn.net/images/codimap/detail/25332/detail_25332_1_500.jpg",
        "때론 섹시하게": "https://image.msscdn.net/images/codimap/detail/25331/detail_25331_1_500.jpg",
        "럭셔리한 디테일": "https://image.msscdn.net/images/codimap/detail/25330/detail_25330_1_500.jpg",
        "스포티 캠핑 룩 날 봐" : "https://image.msscdn.net/images/codimap/detail/25312/detail_25312_1_500.jpg",
        "네온 온 미": "https://image.msscdn.net/images/codimap/detail/25311/detail_25311_1_500.jpg",
        "그레이 고프코어 룩": "https://image.msscdn.net/images/codimap/detail/25310/detail_25310_1_500.jpg",
        "오늘의 룩": "https://image.msscdn.net/images/codimap/detail/25309/detail_25309_1_500.jpg",
        "귀여워 보이고 싶다면": "https://image.msscdn.net/images/codimap/detail/25308/detail_25308_1_500.jpg",
        "단정함이 베스트": "https://image.msscdn.net/images/codimap/detail/25307/detail_25307_1_500.jpg",
        "사랑스러워" : "https://image.msscdn.net/images/codimap/detail/25204/detail_25204_1_500.jpg",
        "리본으로 완성": "https://image.msscdn.net/images/codimap/detail/25203/detail_25203_1_500.jpg",
        "러블리하게": "https://image.msscdn.net/images/codimap/detail/25202/detail_25202_1_500.jpg",
        "오늘의 주인공": "https://image.msscdn.net/images/codimap/detail/25201/detail_25201_1_500.jpg",
        "가방에 주목": "https://image.msscdn.net/images/codimap/detail/25184/detail_25184_1_500.jpg",
        "주말 룩으로 결정": "https://image.msscdn.net/images/codimap/detail/25183/detail_25183_1_500.jpg",
        "믹스 앤 매치": "https://image.msscdn.net/images/codimap/detail/25182/detail_25182_1_500.jpg",
        "서머 페스티벌": "https://image.msscdn.net/images/codimap/detail/25181/detail_25181_1_500.jpg",
        "블록코어의 인기": "https://image.msscdn.net/images/codimap/detail/25180/detail_25180_1_500.jpg",
        "대세는 고프코어": "https://image.msscdn.net/images/codimap/detail/25179/detail_25179_1_500.jpg",
        "시크한 멋": "https://image.msscdn.net/images/codimap/detail/25178/detail_25178_1_500.jpg",
        "우산 챙기세요": "https://image.msscdn.net/images/codimap/detail/25177/detail_25177_1_500.jpg",
        #여자 봄
        "매력적인 코디": "https://image.msscdn.net/images/codimap/detail/22757/detail_22757_1_500.jpg",
        "센스 넘쳐": "https://image.msscdn.net/images/codimap/detail/22756/detail_22756_1_500.jpg",
        "찰떡이야" "https://image.msscdn.net/images/codimap/detail/22755/detail_22755_1_500.jpg",
        "멋스러운 출근 룩": "https://image.msscdn.net/images/codimap/detail/22754/detail_22754_1_500.jpg",
        "워너비 스타일": "https://image.msscdn.net/images/codimap/detail/22753/detail_22753_1_500.jpg",
        "올 블랙 러버": "https://image.msscdn.net/images/codimap/detail/22752/detail_22752_1_500.jpg",
        "편한 게 최고" "https://image.msscdn.net/images/codimap/detail/22751/detail_22751_1_500.jpg",
        "트렌디한 걸리시룩": "https://image.msscdn.net/images/codimap/detail/22750/detail_22750_1_500.jpg",
        "무심하게 툭": "https://image.msscdn.net/images/codimap/detail/22749/detail_22749_1_500.jpg",
        "트렌디 아이템" : "https://image.msscdn.net/images/codimap/detail/22524/detail_22524_1_500.jpg",
        "베스트 활용법" : "https://image.msscdn.net/images/codimap/detail/22523/detail_22523_1_500.jpg",
        "스타일리시한 조합": "https://image.msscdn.net/images/codimap/detail/22522/detail_22522_1_500.jpg",
        "인기 브랜드 픽": "https://image.msscdn.net/images/codimap/detail/22521/detail_22521_1_500.jpg",
        "로맨틱 무드" : "https://image.msscdn.net/images/codimap/detail/22520/detail_22520_1_500.jpg",
        "센스 있는 매치": "https://image.msscdn.net/images/codimap/detail/22519/detail_22519_1_500.jpg",
        "카디건 스타일링": "https://image.msscdn.net/images/codimap/detail/22518/detail_22518_1_500.jpg",
        "추천 브랜드" : "https://image.msscdn.net/images/codimap/detail/22517/detail_22517_1_500.jpg",
        "레더 재킷 연출 법": "https://image.msscdn.net/images/codimap/detail/22516/detail_22516_1_500.jpg"




    }
    
    item_links = {

        "더플코트로 완성": "https://www.musinsa.com/app/codimap/views/28663",
        "코듀로이 팬츠 활용법":"https://www.musinsa.com/app/codimap/views/28662",
        "블랙 앤 화이트 룩": "https://www.musinsa.com/app/codimap/views/28661",
        "테일리 올드머니 룩": "https://www.musinsa.com/app/codimap/views/28660",
        "뉴트럴 톤 아메카지": "https://www.musinsa.com/app/codimap/views/28659",
        "추천, 캠퍼스 룩": "https://www.musinsa.com/app/codimap/views/28658",
        "코트 포기 못 해": "https://www.musinsa.com/app/codimap/views/28657",
        "한 끗 다른 컬러 믹스": "https://www.musinsa.com/app/codimap/views/28656",
        "러블리 트위드 셋업": "https://www.musinsa.com/app/codimap/views/28655",
        "데일리 스트릿 패션": "https://www.musinsa.com/app/codimap/views/28654",
        "한파 속 스트릿 룩": "https://www.musinsa.com/app/codimap/views/28653",
        "유니크한 컬러 매치": "https://www.musinsa.com/app/codimap/views/28652",
        "뉴트럴 톤 코디": "https://www.musinsa.com/app/codimap/views/28651",
        "핑크로 기분UP": "https://www.musinsa.com/app/codimap/views/28650g",
        "루즈 핏 무스탕 연출법": "https://www.musinsa.com/app/codimap/views/28649",
        "빈티지 느낌 물씬": "https://www.musinsa.com/app/codimap/views/28648",
        "레드로 컬러 포인트": "https://www.musinsa.com/app/codimap/views/28647",
        "유니크한 포멀 룩": "https://www.musinsa.com/app/codimap/views/28646",
        "톤온톤의 우아함": "https://www.musinsa.com/app/codimap/views/28645",
        "올블랙 코디법": "https://www.musinsa.com/app/codimap/views/28644",
        "걸리시 코디": "https://www.musinsa.com/app/codimap/views/28600",
        "디테일에 시선 집중": "https://www.musinsa.com/app/codimap/views/28599",
        "플리스 재킷 스타일링": "https://www.musinsa.com/app/codimap/views/28598",
        "캐주얼도 시크하게": "https://www.musinsa.com/app/codimap/views/28597",
        "트위드 셋업 코디": "https://www.musinsa.com/app/codimap/views/28596",
        "추울수록 힙하게": "https://www.musinsa.com/app/codimap/views/28595",
        "일상의 포멀 룩": "https://www.musinsa.com/app/codimap/views/28594",
        "손이 가는 컬러 매치": "https://www.musinsa.com/app/codimap/views/28593",
        "추워도 치마 포기 못해": "https://www.musinsa.com/app/codimap/views/28592",
        "원피스 레이어드하기": "https://www.musinsa.com/app/codimap/views/28591",
        "포멀과 캐주얼 사이": "https://www.musinsa.com/app/codimap/views/28590",
        "모노톤 출근 룩": "https://www.musinsa.com/app/codimap/views/28589",
        "파스텔 컬러 포인트": "https://www.musinsa.com/app/codimap/views/28588",
        "주말 데이트 룩": "https://www.musinsa.com/app/codimap/views/28587",
        "편안한 셋업 코디": "https://www.musinsa.com/app/codimap/views/28586",
        "비즈니스 캐주얼 룩": "https://www.musinsa.com/app/codimap/views/28585",
        "겨울철 숏 팬츠 코디법": "https://www.musinsa.com/app/codimap/views/28584",
        "숏 패딩 연출법": "https://www.musinsa.com/app/codimap/views/28583",
        "한겨울 원 마일 웨어": "https://www.musinsa.com/app/codimap/views/28582",
        "은은한 컬러 포인트": "https://www.musinsa.com/app/codimap/views/28551",
        "맥시스커트 활용법": "https://www.musinsa.com/app/codimap/views/28550",
        "매력적인 아메카지 룩": "https://www.musinsa.com/app/codimap/views/28549",
        "뉴트럴 톤 출근 룩": "https://www.musinsa.com/app/codimap/views/28548",
        # 여자 가을
        "올 블랙 시크 코디": "https://www.musinsa.com/app/codimap/views/27029",
        "아이템 포인트 주기": "https://www.musinsa.com/app/codimap/views/27027",
        "니트 코디 여친 룩": "https://www.musinsa.com/app/codimap/views/27026",
        "니트와 레더 조합": "https://www.musinsa.com/app/codimap/views/27025",
        "커리어 우먼 무드": "https://www.musinsa.com/app/codimap/views/27024",
        "유니크한 아우터": "https://www.musinsa.com/app/codimap/views/27023",
        "카고 스타일링": "https://www.musinsa.com/app/codimap/views/27022",
        "원피스 레이어링": "https://www.musinsa.com/app/codimap/views/27021",
        "실루엣이 돋보여": "https://www.musinsa.com/app/codimap/views/26981",
        "출근 룩 추천": "https://www.musinsa.com/app/codimap/views/26980",
        "이렇게 입어봐": "https://www.musinsa.com/app/codimap/views/26979",
        "요즘 날씨에 딱이야": "https://www.musinsa.com/app/codimap/views/26978",
        "걸리시 아우터 룩": "https://www.musinsa.com/app/codimap/views/26977",
        "키치함 가득": "https://www.musinsa.com/app/codimap/views/26976",
        "우아한 출근길": "https://www.musinsa.com/app/codimap/views/26975",
        "편하지만 센스있게": "https://www.musinsa.com/app/codimap/views/26974",
        "레더 코디 제안": "https://www.musinsa.com/app/codimap/views/26973",
        "셔링 원피스 코디": "https://www.musinsa.com/app/codimap/views/26972",
        "러블리한 조합": "https://www.musinsa.com/app/codimap/views/26971",
        "차분한 룩": "https://www.musinsa.com/app/codimap/views/26970",
        #여자 여름
        "셔링 캐주얼의 끝": "https://www.musinsa.com/app/codimap/views/25337",
        "시크 포인트로 룩 완성": "https://www.musinsa.com/app/codimap/views/25336",
        "출근 룩의 정석": "https://www.musinsa.com/app/codimap/views/25335",
        "사랑스러운 룩": "https://www.musinsa.com/app/codimap/views/25334",
        "로맨틱 모멘트": "https://www.musinsa.com/app/codimap/views/25333",
        "데이트 가기 딱 좋아": "https://www.musinsa.com/app/codimap/views/25332",
        "때론 섹시하게": "https://www.musinsa.com/app/codimap/views/25331",
        "럭셔리한 디테일": "https://www.musinsa.com/app/codimap/views/25330",
        "스포티 캠핑 룩 날 봐": "https://www.musinsa.com/app/codimap/views/25312",
        "네온 온 미": "https://www.musinsa.com/app/codimap/views/25311",
        "그레이 고프코어 룩": "https://www.musinsa.com/app/codimap/views/25310",
        "오늘의 룩": "https://www.musinsa.com/app/codimap/views/25309",
        "귀여워 보이고 싶다면": "https://www.musinsa.com/app/codimap/views/25308",
        "단정함이 베스트": "https://www.musinsa.com/app/codimap/views/25307",
        "사랑스러워": "https://www.musinsa.com/app/codimap/views/25204",
        "리본으로 완성": "https://www.musinsa.com/app/codimap/views/25203",
        "러블리하게": "https://www.musinsa.com/app/codimap/views/25202",
        "오늘의 주인공": "https://www.musinsa.com/app/codimap/views/25201",
        "가방에 주목": "https://www.musinsa.com/app/codimap/views/25184",
        "주말 룩으로 결정": "https://www.musinsa.com/app/codimap/views/25183",
        "믹스 앤 매치": "https://www.musinsa.com/app/codimap/views/25182",
        "서머 페스티벌": "https://www.musinsa.com/app/codimap/views/25181",
        "블록코어의 인기": "https://www.musinsa.com/app/codimap/views/25180",
        "대세는 고프코어": "https://www.musinsa.com/app/codimap/views/25179",
        "시크한 멋": "https://www.musinsa.com/app/codimap/views/25178",
        "우산 챙기세요": "https://www.musinsa.com/app/codimap/views/25177",
        #여자 봄
        "매력적인 코디": "https://www.musinsa.com/app/codimap/views/22757",
        "센스 넘쳐": "https://www.musinsa.com/app/codimap/views/22756",
        "찰떡이야" "https://www.musinsa.com/app/codimap/views/22755",
        "멋스러운 출근 룩": "https://www.musinsa.com/app/codimap/views/22754",
        "워너비 스타일": "https://www.musinsa.com/app/codimap/views/22753",
        "올 블랙 러버": "https://www.musinsa.com/app/codimap/views/22752",
        "편한 게 최고" "https://www.musinsa.com/app/codimap/views/22751",
        "트렌디한 걸리시룩": "https://www.musinsa.com/app/codimap/views/22750",
        "무심하게 툭": "https://www.musinsa.com/app/codimap/views/22749",
        "트렌디 아이템": "https://www.musinsa.com/app/codimap/views/22524",
        "베스트 활용법": "https://www.musinsa.com/app/codimap/views/22523",
        "스타일리시한 조합": "https://www.musinsa.com/app/codimap/views/22522",
        "인기 브랜드 픽": "https://www.musinsa.com/app/codimap/views/22521",
        "로맨틱 무드": "https://www.musinsa.com/app/codimap/views/22520",
        "센스 있는 매치": "https://www.musinsa.com/app/codimap/views/22519",
        "카디건 스타일링": "https://www.musinsa.com/app/codimap/views/22518",
        "추천 브랜드": "https://www.musinsa.com/app/codimap/views/22517",
        "레더 재킷 연출 법": "https://www.musinsa.com/app/codimap/views/22516"


    }

    image_url = image_urls.get(selected_codi, "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTx9cTPon4vY8hARZEH82VaeKY7K2ymGYeYoi89tnB_epPpLEKc84DUhaDnOR8OiHwn6-U&usqp=CAU")  # 선택된 코디에 대한 이미지 URL 가져오기
    item_link = item_links.get(selected_codi, "https://example.com/default_item_link")  # 선택된 코디에 대한 링크 가져오기
    
    return selected_codi, image_url, item_link
