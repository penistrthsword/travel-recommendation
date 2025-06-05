import streamlit as st
import random
import requests

# 위키백과 이미지 함수
def get_wikipedia_image(location_name):
    """위키백과에서 도시 대표 이미지를 가져오고 출처를 반환"""
    try:
        wiki_map = {
            "괌": "Guam",
            "아테네": "Athens",
            "산토리니": "Santorini",
            "프라하": "Prague",
            "싱가포르": "Singapore",
            "발리": "Bali",
            "이스탄불": "Istanbul",
            "보라카이": "Boracay",
            "방콕": "Bangkok",
            "푸꾸옥": "Phú Quốc",
            "스위스 인터라켄": "Interlaken",
            "태국 푸껫": "Phuket",
            "뉴질랜드 퀸스타운": "Queenstown",
            "일본 도쿄": "Tokyo",
            "베트남 다낭": "Da Nang",
            "이탈리아 로마": "Rome",
            "아이슬란드 레이캬비크": "Reykjavik",
            "미국 하와이 호놀룰루": "Honolulu",
            "캐나다 밴프": "Banff",
            "모로코 마라케시": "Marrakech",
            "미국 뉴욕": "New York",
            "프랑스 파리": "Paris"
        }
        title = wiki_map.get(location_name, location_name)
        url = f"https://en.wikipedia.org/api/rest_v1/page/summary/{title}"
        res = requests.get(url)
        data = res.json()
        img_url = data.get("thumbnail", {}).get("source")
        page_url = data.get("content_urls", {}).get("desktop", {}).get("page")
        return img_url, page_url
    except:
        return None, None

# 여행지 데이터베이스
def get_destinations_data():
    return [
        {"name": "괌", "climate": "더운", "activity": "휴양", "companion": ["커플", "친구들"], "min_budget": 180, "flight_time": "약 4시간", "hemisphere": "북",
         "description": {"기후": "열대 해양성 기후로 연중 따뜻합니다.", "평균기온": "27~32도", "관광지": ["투몬 해변", "사랑의 절벽"], "맛집": ["프로아", "투몬베이 카페"]},
         "budget_breakdown": {"항공편": "70만원", "숙박": "60만원", "식비": "30만원", "기타": "20만원"}, "hotel": {"name": "Dusit Thani Guam", "rating": "4.6", "desc": "럭셔리 오션뷰 리조트"}},
        {"name": "아테네", "climate": "더운", "activity": "관광", "companion": ["혼자", "커플"], "min_budget": 230, "flight_time": "약 12시간", "hemisphere": "북",
         "description": {"기후": "덥고 건조한 지중해성 여름입니다.", "평균기온": "28~35도", "관광지": ["아크로폴리스", "플라카 거리"], "맛집": ["O Thanasis", "Kuzina Athens"]},
         "budget_breakdown": {"항공편": "100만원", "숙박": "80만원", "식비": "30만원", "기타": "20만원"}, "hotel": {"name": "Electra Palace Athens", "rating": "4.5", "desc": "아크로폴리스 전망의 호텔"}},
        {"name": "산토리니", "climate": "더운", "activity": "휴양", "companion": ["커플"], "min_budget": 250, "flight_time": "약 13시간", "hemisphere": "북",
         "description": {"기후": "햇살 좋은 지중해성 기후", "평균기온": "27~33도", "관광지": ["이아 마을", "피라"], "맛집": ["Metaxi Mas", "Argo Restaurant"]},
         "budget_breakdown": {"항공편": "110만원", "숙박": "90만원", "식비": "30만원", "기타": "20만원"}, "hotel": {"name": "Canaves Oia Suites", "rating": "4.8", "desc": "절벽 위 인피니티 풀"}},
        {"name": "프라하", "climate": "시원한", "activity": "관광", "companion": ["혼자", "커플"], "min_budget": 200, "flight_time": "약 11시간", "hemisphere": "북",
         "description": {"기후": "여름엔 선선하고 쾌적합니다.", "평균기온": "20~26도", "관광지": ["카를 다리", "프라하성"], "맛집": ["Lokal", "Mlýnec"]},
         "budget_breakdown": {"항공편": "90만원", "숙박": "70만원", "식비": "20만원", "기타": "20만원"}, "hotel": {"name": "Hotel Kings Court", "rating": "4.5", "desc": "도심 중심의 고급 호텔"}},
        {"name": "싱가포르", "climate": "더운", "activity": "쇼핑", "companion": ["혼자", "커플", "친구들"], "min_budget": 220, "flight_time": "약 6시간 30분", "hemisphere": "북",
         "description": {"기후": "고온 다습한 열대 기후", "평균기온": "26~33도", "관광지": ["마리나 베이", "가든스 바이 더 베이"], "맛집": ["맥스웰 푸드센터", "Jumbo Seafood"]},
         "budget_breakdown": {"항공편": "90만원", "숙박": "80만원", "식비": "30만원", "기타": "20만원"}, "hotel": {"name": "Marina Bay Sands", "rating": "4.7", "desc": "인피니티 풀로 유명"}},
        {"name": "발리", "climate": "더운", "activity": "휴양", "companion": ["커플", "친구들"], "min_budget": 150, "flight_time": "약 7시간", "hemisphere": "남",
         "description": {"기후": "고온다습, 해변과 산을 모두 즐길 수 있어요.", "평균기온": "26~31도", "관광지": ["우붓", "쿠타 해변"], "맛집": ["Mamasan", "Bambu"]},
         "budget_breakdown": {"항공편": "60만원", "숙박": "50만원", "식비": "20만원", "기타": "20만원"}, "hotel": {"name": "Four Seasons Bali", "rating": "4.8", "desc": "전통미+럭셔리"}},
        {"name": "이스탄불", "climate": "시원한", "activity": "관광", "companion": ["혼자", "커플"], "min_budget": 230, "flight_time": "약 12시간", "hemisphere": "북",
         "description": {"기후": "초여름은 선선하고 건조함", "평균기온": "20~26도", "관광지": ["블루모스크", "아야 소피아"], "맛집": ["Ciya Sofrasi", "Nusr-Et"]},
         "budget_breakdown": {"항공편": "90만원", "숙박": "80만원", "식비": "30만원", "기타": "30만원"}, "hotel": {"name": "Sirkeci Mansion", "rating": "4.6", "desc": "역사 중심지 위치"}},
        {"name": "보라카이", "climate": "더운", "activity": "휴양", "companion": ["커플", "친구들"], "min_budget": 130, "flight_time": "약 5시간", "hemisphere": "북",
         "description": {"기후": "열대 기후, 바다가 아름다움", "평균기온": "28~32도", "관광지": ["화이트 비치", "윌리스 록"], "맛집": ["D’Talipapa", "The Sunny Side Cafe"]},
         "budget_breakdown": {"항공편": "50만원", "숙박": "50만원", "식비": "20만원", "기타": "10만원"}, "hotel": {"name": "Shangri-La Boracay", "rating": "4.7", "desc": "프라이빗 해변"}},
        {"name": "방콕", "climate": "더운", "activity": "쇼핑", "companion": ["혼자", "커플", "친구들"], "min_budget": 120, "flight_time": "약 6시간", "hemisphere": "북",
         "description": {"기후": "고온다습, 더위에 강한 분께 추천", "평균기온": "29~35도", "관광지": ["왓포", "카오산로드"], "맛집": ["Jay Fai", "Somtum Der"]},
         "budget_breakdown": {"항공편": "50만원", "숙박": "40만원", "식비": "20만원", "기타": "10만원"}, "hotel": {"name": "The Okura Prestige", "rating": "4.6", "desc": "도심 고급 호텔"}},
        {"name": "푸꾸옥", "climate": "더운", "activity": "휴양", "companion": ["커플"], "min_budget": 140, "flight_time": "약 5시간", "hemisphere": "북",
         "description": {"기후": "해양성 열대 기후, 해변 특화", "평균기온": "28~33도", "관광지": ["사오 비치", "빈펄랜드"], "맛집": ["Bún Quậy Kiến Xây", "Crab House"]},
         "budget_breakdown": {"항공편": "60만원", "숙박": "50만원", "식비": "20만원", "기타": "10만원"}, "hotel": {"name": "JW Marriott Phu Quoc", "rating": "4.8", "desc": "이국적 럭셔리"}},
        {"name": "스위스 인터라켄", "climate": "시원한", "activity": "휴양", "companion": ["혼자", "커플"], "min_budget": 300, "flight_time": "약 12시간", "hemisphere": "북",
         "description": {"기후": "알프스 산속에 위치해 여름에도 선선하고 상쾌합니다.", "평균기온": "약 15~22도", "관광지": ["융프라우요흐", "하더 쿨름", "툰 호수"], "맛집": ["Husi Bierhaus – 맥주와 전통식", "Schuh – 초콜릿 디저트 유명"]},
         "budget_breakdown": {"항공편": "120만원", "숙박": "100만원 (4성급 호텔 4박)", "식비": "30만원", "기타": "50만원 (기차, 케이블카 등)"}, "hotel": {"name": "Lindner Grand Hotel Beau Rivage", "rating": "4.4/5", "desc": "융프라우 강 전망이 멋진 클래식 호텔"}},
        {"name": "태국 푸껫", "climate": "더운", "activity": "휴양", "companion": ["혼자", "커플", "친구들"], "min_budget": 100, "flight_time": "약 6시간", "hemisphere": "북",
         "description": {"기후": "뜨거운 햇살과 바다, 스콜이 간혹 있지만 여행엔 큰 지장 없어요.", "평균기온": "약 28~32도", "관광지": ["빠통 해변", "섬 투어", "빅 부다"], "맛집": ["Ko Benz – 돼지고기 국수", "Blue Elephant – 전통 태국 요리"]},
         "budget_breakdown": {"항공편": "50만원", "숙박": "40만원 (리조트 4박)", "식비": "20만원", "기타": "10만원 (마사지, 교통 등)"}, "hotel": {"name": "The Shore at Katathani", "rating": "4.7/5", "desc": "바다 전망 풀빌라, 커플 여행에 딱!"}},
        {"name": "뉴질랜드 퀸스타운", "climate": "추운", "activity": "모험", "companion": ["혼자", "친구"], "min_budget": 300, "flight_time": "약 13시간", "hemisphere": "남",
         "description": {"기후": "겨울을 맞은 퀸스타운은 설경과 함께 다양한 액티비티로 가득해요.", "평균기온": "약 0~10도", "관광지": ["와카티푸 호수", "스키장", "번지점프"], "맛집": ["Fergburger – 전설의 버거", "The Cow – 벽난로 있는 피자집"]},
         "budget_breakdown": {"항공편": "140만원", "숙박": "90만원 (스키 리조트 4박)", "식비": "40만원", "기타": "30만원 (스키장, 액티비티)"}, "hotel": {"name": "QT Queenstown", "rating": "4.5/5", "desc": "스키어들을 위한 모던하고 감각적인 호텔"}},
        {"name": "일본 도쿄", "climate": "시원한", "activity": "쇼핑", "companion": ["혼자", "친구"], "min_budget": 150, "flight_time": "약 2시간 30분", "hemisphere": "북",
         "description": {"기후": "도쿄의 여름은 덥고 습하지만 도시 탐험에 적합해요.", "평균기온": "약 22~30도", "관광지": ["신주쿠", "시부야", "아키하바라"], "맛집": ["이치란 라멘", "스시 잔마이"]},
         "budget_breakdown": {"항공편": "40만원", "숙박": "60만원 (호텔 4박)", "식비": "30만원", "기타": "20만원 (교통, 입장료 등)"}, "hotel": {"name": "Shinjuku Granbell Hotel", "rating": "4.3/5", "desc": "도심 속 현대적 디자인 호텔"}},
        {"name": "베트남 다낭", "climate": "더운", "activity": "휴양", "companion": ["커플", "친구들"], "min_budget": 100, "flight_time": "약 4시간 30분", "hemisphere": "북",
         "description": {"기후": "더운 날씨와 아름다운 해변이 여행의 매력입니다.", "평균기온": "약 27~33도", "관광지": ["바나힐", "미케 해변", "호이안 구시가지"], "맛집": ["반미 포", "미꽝"]},
         "budget_breakdown": {"항공편": "40만원", "숙박": "30만원 (리조트 4박)", "식비": "20만원", "기타": "10만원 (교통, 액티비티)"}, "hotel": {"name": "InterContinental Danang Sun Peninsula Resort", "rating": "4.8/5", "desc": "호이안과 가까운 고급 리조트"}},
        {"name": "이탈리아 로마", "climate": "더운", "activity": "관광", "companion": ["혼자", "커플", "친구들"], "min_budget": 250, "flight_time": "약 12시간", "hemisphere": "북",
         "description": {"기후": "지중해성 기후로 여름엔 뜨겁지만 여행에는 적당합니다.", "평균기온": "약 26~34도", "관광지": ["콜로세움", "바티칸", "트레비 분수"], "맛집": ["Roscioli", "Da Enzo al 29"]},
         "budget_breakdown": {"항공편": "100만원", "숙박": "90만원 (호텔 4박)", "식비": "30만원", "기타": "30만원 (입장료, 교통 등)"}, "hotel": {"name": "Hotel Artemide", "rating": "4.6/5", "desc": "도심 중심 고급 호텔"}},
        {"name": "아이슬란드 레이캬비크", "climate": "추운", "activity": "관광", "companion": ["혼자", "커플"], "min_budget": 350, "flight_time": "약 14시간", "hemisphere": "북",
         "description": {"기후": "한여름에도 선선하거나 쌀쌀하며 맑은 날이 많아요.", "평균기온": "약 8~15도", "관광지": ["블루라군", "골든서클", "빙하호수"], "맛집": ["Icelandic Street Food", "Grillmarkadurinn"]},
         "budget_breakdown": {"항공편": "140만원", "숙박": "120만원 (호텔 4박)", "식비": "40만원", "기타": "50만원 (렌터카, 온천 등)"}, "hotel": {"name": "Fosshotel Reykjavik", "rating": "4.4/5", "desc": "도심과 가까우면서 바다 전망 고급 호텔"}},
        {"name": "미국 하와이 호놀룰루", "climate": "더운", "activity": "휴양", "companion": ["커플", "친구들"], "min_budget": 300, "flight_time": "약 9시간 30분", "hemisphere": "북",
         "description": {"기후": "연중 더운 날씨, 습도 비교적 낮음", "평균기온": "약 28~33도", "관광지": ["와이키키 해변", "다이아몬드 헤드", "하나우마 베이"], "맛집": ["Leonard's Bakery", "Marukame Udon"]},
         "budget_breakdown": {"항공편": "130만원", "숙박": "100만원 (리조트 4박)", "식비": "30만원", "기타": "40만원 (렌터카, 투어)"}, "hotel": {"name": "Hilton Hawaiian Village", "rating": "4.5/5", "desc": "와이키키 해변 앞 리조트"}},
        {"name": "캐나다 밴프", "climate": "시원한", "activity": "휴양", "companion": ["혼자", "커플"], "min_budget": 280, "flight_time": "약 11시간", "hemisphere": "북",
         "description": {"기후": "여름에도 시원하고 선선함", "평균기온": "약

# (코드 이어짐)