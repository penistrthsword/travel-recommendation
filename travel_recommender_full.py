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
            "푸꾸옥": "Phú Quốc"
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
         "budget_breakdown": {"항공편": "60만원", "숙박": "50만원", "식비": "20만원", "기타": "10만원"}, "hotel": {"name": "JW Marriott Phu Quoc", "rating": "4.8", "desc": "이국적 럭셔리"}}
    ]

# 점수 계산
def score_destination(dest, climate, activity, companion, budget):
    score = 0
    if dest["climate"] == climate: score += 3
    elif climate in ["추운", "시원한", "더운"] and dest["climate"] in ["추운", "시원한", "더운"]:
        if abs(["추운", "시원한", "더운"].index(climate) - ["추운", "시원한", "더운"].index(dest["climate"])) == 1:
            score += 1
    if dest["activity"] == activity: score += 3
    if companion in dest["companion"]: score += 3
    if budget >= dest["min_budget"]: score += 3
    elif budget >= dest["min_budget"] * 0.8: score += 1
    return score

# 여행 명언
def get_travel_quote():
    quotes = [
        ""여행은 당신을 말없이 만든 다음, 당신을 이야기꾼으로 만든다." – 이븐 바투타",
        ""세상은 한 권의 책이고, 여행하지 않는 사람은 그 책의 한 페이지만 읽는 것이다." – 성 아우구스티누스",
        ""가장 위대한 여행은 우리가 아직 가보지 않은 곳을 향한 것이다." – 알랭 드 보통"
    ]
    return random.choice(quotes)

# 메인 함수
def main():
    st.set_page_config(page_title="🌍 여름방학 해외여행 추천", page_icon="✈️", layout="wide")
    st.title("🌍 여름방학 해외여행 추천 프로그램")
    st.markdown("---")

    with st.sidebar:
        st.header("🔍 여행 취향 조사")
        climate = st.selectbox("원하는 기후:", ["더운", "시원한", "추운"])
        activity = st.selectbox("기대 활동:", ["휴양", "관광", "쇼핑", "모험"])
        companion = st.selectbox("동반자:", ["혼자", "커플", "친구들"])
        budget = st.number_input("예산 (만원):", 50, 1000, 200, 10)
        recommend_button = st.button("🎯 여행지 추천받기!")

    if recommend_button:
        dests = get_destinations_data()
        best = max(dests, key=lambda d: score_destination(d, climate, activity, companion, budget))
        score = score_destination(best, climate, activity, companion, budget)
        img_url, source_url = get_wikipedia_image(best["name"])

        st.markdown("---")
        st.balloons()
        if img_url:
            st.image(img_url, caption=f"📸 {best['name']} 여행지 전경", use_column_width=True)
            if source_url:
                st.markdown(f"📚 출처: [위키백과]({source_url})")
        else:
            st.info("🔍 이미지를 불러올 수 없습니다.")

        st.markdown(f"## 🎉 추천 여행지: {best['name']}")
        st.markdown(f"✈️ 비행시간: {best['flight_time']} | 🧭 현재 계절: {'북반구의 여름' if best['hemisphere']=='북' else '남반구의 겨울'}")
        st.metric("매칭 점수", f"{score}/12")

        with st.expander("🔍 상세 정보 보기"):
            st.subheader("🌡️ 기후 및 관광")
            st.write(best["description"]["기후"])
            st.write(f"평균기온: {best['description']['평균기온']}")
            st.write("관광지:", ", ".join(best["description"]["관광지"]))

            st.subheader("🍽️ 맛집 추천")
            st.write(", ".join(best["description"]["맛집"]))

            st.subheader("🏨 호텔 정보")
            st.write(f"{best['hotel']['name']} ({best['hotel']['rating']} ⭐): {best['hotel']['desc']}")

            st.subheader("💰 예산")
            for k, v in best["budget_breakdown"].items():
                st.write(f"{k}: {v}")

        st.markdown("---")
        st.markdown(f"> 📖 {get_travel_quote()}")
    else:
        st.markdown("👈 왼쪽 사이드바에서 조건을 선택해주세요!")

if __name__ == "__main__":
    main()
