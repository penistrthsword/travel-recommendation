import streamlit as st
import random
import requests

def get_unsplash_image(location_name):
    """Unsplash에서 여행지 이미지를 가져오는 함수"""
    try:
        # 여행지 이름에서 국가 정보 제거하고 주요 도시명만 추출
        search_terms = {
            "스위스 인터라켄": "interlaken switzerland mountains",
            "태국 푸껫": "phuket thailand beach",
            "뉴질랜드 퀸스타운": "queenstown new zealand",
            "일본 도쿄": "tokyo japan city",
            "베트남 다낭": "danang vietnam beach",
            "이탈리아 로마": "rome italy colosseum",
            "아이슬란드 레이캬비크": "reykjavik iceland",
            "미국 하와이 호놀룰루": "honolulu hawaii beach",
            "캐나다 밴프": "banff canada mountains",
            "모로코 마라케시": "marrakech morocco",
            "미국 뉴욕": "new york city usa",
            "프랑스 파리": "paris france eiffel tower"
        }
        
        search_query = search_terms.get(location_name, location_name.split()[1] if len(location_name.split()) > 1 else location_name)
        
        # Unsplash Source API 사용 (무료, API 키 불필요)
        # 1280x720 크기의 랜덤 이미지
        image_url = f"https://source.unsplash.com/1280x720/?{search_query.replace(' ', ',')}"
        return image_url
    except:
        # 이미지 로드 실패 시 기본 여행 이미지
        return "https://source.unsplash.com/1280x720/?travel,vacation"

def get_destinations_data():
    """여행지 데이터를 반환하는 함수"""
    return [
        {
            "name": "스위스 인터라켄 🇨🇭",
            "climate": "시원한",
            "activity": "휴양",
            "companion": ["혼자", "커플"],
            "min_budget": 300,
            "flight_time": "약 12시간",
            "hemisphere": "북",
            "budget_breakdown": {
                "항공편": "120만원",
                "숙박": "100만원 (4성급 호텔 4박)",
                "식비": "30만원",
                "기타": "50만원 (기차, 케이블카 등)"
            },
            "hotel": {
                "name": "Lindner Grand Hotel Beau Rivage",
                "rating": "4.4/5",
                "desc": "융프라우 강 전망이 멋진 클래식 호텔"
            },
            "description": {
                "기후": "알프스 산속에 위치해 여름에도 선선하고 상쾌합니다.",
                "평균기온": "약 15~22도",
                "관광지": ["융프라우요흐", "하더 쿨름", "툰 호수"],
                "맛집": ["Husi Bierhaus – 맥주와 전통식", "Schuh – 초콜릿 디저트 유명"]
            }
        },
        {
            "name": "태국 푸껫 🇹🇭",
            "climate": "더운",
            "activity": "휴양",
            "companion": ["혼자", "커플", "친구들"],
            "min_budget": 100,
            "flight_time": "약 6시간",
            "hemisphere": "북",
            "budget_breakdown": {
                "항공편": "50만원",
                "숙박": "40만원 (리조트 4박)",
                "식비": "20만원",
                "기타": "10만원 (마사지, 교통 등)"
            },
            "hotel": {
                "name": "The Shore at Katathani",
                "rating": "4.7/5",
                "desc": "바다 전망 풀빌라, 커플 여행에 딱!"
            },
            "description": {
                "기후": "뜨거운 햇살과 바다, 스콜이 간혹 있지만 여행엔 큰 지장 없어요.",
                "평균기온": "약 28~32도",
                "관광지": ["빠통 해변", "섬 투어", "빅 부다"],
                "맛집": ["Ko Benz – 돼지고기 국수", "Blue Elephant – 전통 태국 요리"]
            }
        },
        {
            "name": "뉴질랜드 퀸스타운 🇳🇿",
            "climate": "추운",
            "activity": "모험",
            "companion": ["혼자", "친구들"],
            "min_budget": 300,
            "flight_time": "약 13시간",
            "hemisphere": "남",
            "budget_breakdown": {
                "항공편": "140만원",
                "숙박": "90만원 (스키 리조트 4박)",
                "식비": "40만원",
                "기타": "30만원 (스키장, 액티비티)"
            },
            "hotel": {
                "name": "QT Queenstown",
                "rating": "4.5/5",
                "desc": "스키어들을 위한 모던하고 감각적인 호텔"
            },
            "description": {
                "기후": "겨울을 맞은 퀸스타운은 설경과 함께 다양한 액티비티로 가득해요.",
                "평균기온": "약 0~10도",
                "관광지": ["와카티푸 호수", "스키장", "번지점프"],
                "맛집": ["Fergburger – 전설의 버거", "The Cow – 벽난로 있는 피자집"]
            }
        },
        {
            "name": "일본 도쿄 🇯🇵",
            "climate": "시원한",
            "activity": "쇼핑",
            "companion": ["혼자", "친구들"],
            "min_budget": 150,
            "flight_time": "약 2시간 30분",
            "hemisphere": "북",
            "budget_breakdown": {
                "항공편": "40만원",
                "숙박": "60만원 (호텔 4박)",
                "식비": "30만원",
                "기타": "20만원 (교통, 입장료 등)"
            },
            "hotel": {
                "name": "Shinjuku Granbell Hotel",
                "rating": "4.3/5",
                "desc": "도심 속 현대적 디자인 호텔"
            },
            "description": {
                "기후": "도쿄의 여름은 덥고 습하지만 도시 탐험에 적합해요.",
                "평균기온": "약 22~30도",
                "관광지": ["신주쿠", "시부야", "아키하바라"],
                "맛집": ["이치란 라멘", "스시 잔마이"]
            }
        },
        {
            "name": "베트남 다낭 🇻🇳",
            "climate": "더운",
            "activity": "휴양",
            "companion": ["커플", "친구들"],
            "min_budget": 100,
            "flight_time": "약 4시간 30분",
            "hemisphere": "북",
            "budget_breakdown": {
                "항공편": "40만원",
                "숙박": "30만원 (리조트 4박)",
                "식비": "20만원",
                "기타": "10만원 (교통, 액티비티)"
            },
            "hotel": {
                "name": "InterContinental Danang Sun Peninsula Resort",
                "rating": "4.8/5",
                "desc": "호이안과 가깝고 해변 뷰가 좋은 고급 리조트"
            },
            "description": {
                "기후": "더운 날씨와 아름다운 해변이 여행의 매력입니다.",
                "평균기온": "약 27~33도",
                "관광지": ["바나힐", "미케 해변", "호이안 구시가지"],
                "맛집": ["반미 포", "미꽝"]
            }
        },
        {
            "name": "이탈리아 로마 🇮🇹",
            "climate": "더운",
            "activity": "관광",
            "companion": ["혼자", "커플", "친구들"],
            "min_budget": 250,
            "flight_time": "약 12시간",
            "hemisphere": "북",
            "budget_breakdown": {
                "항공편": "100만원",
                "숙박": "90만원 (호텔 4박)",
                "식비": "30만원",
                "기타": "30만원 (입장료, 교통 등)"
            },
            "hotel": {
                "name": "Hotel Artemide",
                "rating": "4.6/5",
                "desc": "도심 중심에 위치한 고급 호텔"
            },
            "description": {
                "기후": "지중해성 기후로 여름엔 뜨겁지만 여행에는 적당합니다.",
                "평균기온": "약 26~34도",
                "관광지": ["콜로세움", "바티칸", "트레비 분수"],
                "맛집": ["Roscioli", "Da Enzo al 29"]
            }
        },
        {
            "name": "아이슬란드 레이캬비크 🇮🇸",
            "climate": "추운",
            "activity": "관광",
            "companion": ["혼자", "커플"],
            "min_budget": 350,
            "flight_time": "약 14시간",
            "hemisphere": "북",
            "budget_breakdown": {
                "항공편": "140만원",
                "숙박": "120만원 (호텔 4박)",
                "식비": "40만원",
                "기타": "50만원 (렌터카, 온천 등)"
            },
            "hotel": {
                "name": "Fosshotel Reykjavik",
                "rating": "4.4/5",
                "desc": "도심과 가까우면서 바다 전망도 좋은 호텔"
            },
            "description": {
                "기후": "한여름에도 선선하거나 쌀쌀하며 맑은 날이 많아요.",
                "평균기온": "약 8~15도",
                "관광지": ["블루라군", "골든서클", "빙하호수"],
                "맛집": ["Icelandic Street Food", "Grillmarkadurinn"]
            }
        },
        {
            "name": "미국 하와이 호놀룰루 🇺🇸",
            "climate": "더운",
            "activity": "휴양",
            "companion": ["커플", "친구들"],
            "min_budget": 300,
            "flight_time": "약 9시간 30분",
            "hemisphere": "북",
            "budget_breakdown": {
                "항공편": "130만원",
                "숙박": "100만원 (리조트 4박)",
                "식비": "30만원",
                "기타": "40만원 (렌터카, 투어)"
            },
            "hotel": {
                "name": "Hilton Hawaiian Village",
                "rating": "4.5/5",
                "desc": "와이키키 해변 바로 앞 리조트"
            },
            "description": {
                "기후": "연중 더운 날씨로 유명하며 습도는 비교적 낮습니다.",
                "평균기온": "약 28~33도",
                "관광지": ["와이키키 해변", "다이아몬드 헤드", "하나우마 베이"],
                "맛집": ["Leonard's Bakery", "Marukame Udon"]
            }
        },
        {
            "name": "캐나다 밴프 🇨🇦",
            "climate": "시원한",
            "activity": "휴양",
            "companion": ["혼자", "커플"],
            "min_budget": 280,
            "flight_time": "약 11시간",
            "hemisphere": "북",
            "budget_breakdown": {
                "항공편": "120만원",
                "숙박": "90만원 (호텔 4박)",
                "식비": "30만원",
                "기타": "40만원 (자연공원 입장료, 교통 등)"
            },
            "hotel": {
                "name": "Fairmont Banff Springs",
                "rating": "4.6/5",
                "desc": "산속에 있는 고성 같은 럭셔리 호텔"
            },
            "description": {
                "기후": "여름에도 시원하고 선선하며 쾌적한 날씨를 자랑합니다.",
                "평균기온": "약 12~20도",
                "관광지": ["레이크 루이스", "밴프 국립공원", "곤돌라"],
                "맛집": ["Three Ravens", "Eddie Burger"]
            }
        },
        {
            "name": "모로코 마라케시 🇲🇦",
            "climate": "더운",
            "activity": "관광",
            "companion": ["커플", "친구들"],
            "min_budget": 200,
            "flight_time": "약 16시간",
            "hemisphere": "북",
            "budget_breakdown": {
                "항공편": "90만원",
                "숙박": "60만원 (리야드 4박)",
                "식비": "20만원",
                "기타": "30만원 (시장, 교통 등)"
            },
            "hotel": {
                "name": "Riad Yasmine",
                "rating": "4.7/5",
                "desc": "전통 건축 양식의 인스타 명소"
            },
            "description": {
                "기후": "사막 근처로 매우 더운 날씨지만 건조합니다.",
                "평균기온": "약 30~38도",
                "관광지": ["제마 엘프나", "바히아 궁전", "수크 시장"],
                "맛집": ["Nomad", "Café des Épices"]
            }
        },
        {
            "name": "미국 뉴욕 🇺🇸",
            "climate": "더운",
            "activity": "쇼핑",
            "companion": ["혼자", "친구들"],
            "min_budget": 350,
            "flight_time": "약 14시간",
            "hemisphere": "북",
            "budget_breakdown": {
                "항공편": "150만원",
                "숙박": "120만원 (맨해튼 호텔 4박)",
                "식비": "40만원",
                "기타": "40만원 (브로드웨이, 입장료 등)"
            },
            "hotel": {
                "name": "The New Yorker",
                "rating": "4.3/5",
                "desc": "펜역 바로 앞의 인기 호텔"
            },
            "description": {
                "기후": "여름엔 덥고 습하지만 도시 탐험엔 완벽해요.",
                "평균기온": "약 26~34도",
                "관광지": ["센트럴 파크", "브루클린", "자유의 여신상"],
                "맛집": ["Shake Shack", "Katz's Delicatessen"]
            }
        },
        {
            "name": "프랑스 파리 🇫🇷",
            "climate": "시원한",
            "activity": "관광",
            "companion": ["혼자", "커플"],
            "min_budget": 270,
            "flight_time": "약 11시간",
            "hemisphere": "북",
            "budget_breakdown": {
                "항공편": "110만원",
                "숙박": "100만원 (호텔 4박)",
                "식비": "30만원",
                "기타": "30만원 (입장료, 교통 등)"
            },
            "hotel": {
                "name": "Hotel Le Six",
                "rating": "4.4/5",
                "desc": "몽파르나스 근처 부티크 호텔"
            },
            "description": {
                "기후": "7~8월엔 선선하거나 따뜻한 날씨가 대부분입니다.",
                "평균기온": "약 18~26도",
                "관광지": ["에펠탑", "루브르 박물관", "몽마르트 언덕"],
                "맛집": ["Le Relais de l'Entrecôte", "Ladurée"]
            }
        }
    ]

def score_destination(dest, climate, activity, companion, budget):
    """여행지 점수를 계산하는 함수"""
    score = 0
    
    # 기후 일치 3점, 인접 기후 1점
    if dest["climate"] == climate:
        score += 3
    else:
        climates = ["추운", "시원한", "더운"]
        if climate in climates and dest["climate"] in climates:
            diff = abs(climates.index(dest["climate"]) - climates.index(climate))
            if diff == 1:
                score += 1

    # 활동 일치 3점
    if dest["activity"] == activity:
        score += 3

    # 동반자 포함 3점
    if companion in dest["companion"]:
        score += 3

    # 예산: 충분하면 3점, 80% 이상이면 1점
    if budget >= dest["min_budget"]:
        score += 3
    elif budget >= dest["min_budget"] * 0.8:
        score += 1

    return score

def get_travel_quote():
    """랜덤 여행 명언을 반환하는 함수"""
    quotes = [
        "\"여행은 당신을 말없이 만든 다음, 당신을 이야기꾼으로 만든다.\" – 이븐 바투타",
        "\"세상은 한 권의 책이고, 여행하지 않는 사람은 그 책의 한 페이지만 읽는 것이다.\" – 성 아우구스티누스",
        "\"가장 위대한 여행은 우리가 아직 가보지 않은 곳을 향한 것이다.\" – 알랭 드 보통"
    ]
    return random.choice(quotes)

def main():
    # 페이지 설정
    st.set_page_config(
        page_title="🌍 여름방학 해외여행 추천",
        page_icon="✈️",
        layout="wide"
    )
    
    # 메인 타이틀
    st.title("🌍 여름방학 해외여행 추천 프로그램")
    st.markdown("---")
    
    # 인트로 메시지
    st.markdown("""
    ### 이제 곧 짜릿한 방학이 시작되겠네요! 🎒
    평소 꿈꿔왔던 여행지, 이번 여름에 다녀오는 건 어떨까요?
    
    **당신의 취향을 알려주시면, 딱 맞는 여행지를 추천해드릴게요!** ✨
    """)
    
    # 사이드바에 입력 폼 배치
    with st.sidebar:
        st.header("🔍 여행 취향 조사")
        
        # 기후 선택
        st.subheader("🌤️ 어떤 분위기를 원하시나요?")
        climate = st.selectbox(
            "원하는 기후를 선택해주세요:",
            ["더운", "시원한", "추운"],
            help="☀️ 따사로운 햇살 아래 / 🌬️ 선선한 바람 속에서 / ❄️ 차가운 공기 속에서"
        )
        
        # 활동 선택
        st.subheader("🎯 가장 기대되는 활동은?")
        activity = st.selectbox(
            "원하는 활동을 선택해주세요:",
            ["휴양", "관광", "쇼핑", "모험"],
            help="🏖️ 바다 보며 쉬는 휴양 / 🗺️ 유적지와 명소 투어 / 🛍️ 쇼핑 천국 / ⛰️ 짜릿한 모험"
        )
        
        # 동반자 선택
        st.subheader("👥 함께 여행하는 분은?")
        companion = st.selectbox(
            "동반자를 선택해주세요:",
            ["혼자", "커플", "친구들"]
        )
        
        # 예산 입력
        st.subheader("💰 여행 예산")
        budget = st.number_input(
            "1인당 전체 예산 (만원, 항공편 포함):",
            min_value=50,
            max_value=1000,
            value=200,
            step=10,
            help="예시: 150만원 → 150 입력"
        )
        
        # 추천 버튼
        recommend_button = st.button("🎯 여행지 추천받기!", type="primary", use_container_width=True)
    
    # 메인 영역에 결과 표시
    if recommend_button:
        with st.spinner("✈️ 완벽한 여행지를 찾는 중..."):
            destinations = get_destinations_data()
            
            # 최적 여행지 찾기
            best_dest = max(destinations, key=lambda dest: score_destination(dest, climate, activity, companion, budget))
            best_score = score_destination(best_dest, climate, activity, companion, budget)
            
            # 여행지 이미지 가져오기
            image_url = get_unsplash_image(best_dest['name'])
        
        # 결과 표시
        st.markdown("---")
        st.balloons()  # 축하 애니메이션
        
        # 여행지 대표 이미지 표시
        st.image(image_url, caption=f"📸 {best_dest['name']} 여행지 전경", use_column_width=True)
        
        # 메인 추천 결과
        col1, col2 = st.columns([2, 1])
        
        with col1:
            st.markdown(f"## 🎉 추천 여행지")
            st.markdown(f"# {best_dest['name']}")
            st.markdown(f"**✈️ 비행시간:** {best_dest['flight_time']}")
            hemisphere_text = "북반구의 여름" if best_dest['hemisphere'] == '북' else "남반구의 겨울"
            st.markdown(f"**🧭 현재 계절:** {hemisphere_text}")
        
        with col2:
            # 매칭 점수 표시
            st.metric("매칭 점수", f"{best_score}/12", help="선택한 조건과의 일치도")
            
            # 이미지 새로 고침 버튼
            if st.button("🖼️ 다른 사진 보기", help="같은 여행지의 다른 사진을 불러옵니다"):
                new_image_url = get_unsplash_image(best_dest['name'])
                st.image(new_image_url, caption=f"📸 {best_dest['name']} 또 다른 모습", width=300)
        
        # 상세 정보를 탭으로 구성
        tab1, tab2, tab3, tab4 = st.tabs(["🌡️ 기후 정보", "🏨 숙박 & 예산", "🏞️ 관광지", "🍽️ 맛집"])
        
        desc = best_dest["description"]
        hotel = best_dest["hotel"]
        breakdown = best_dest["budget_breakdown"]
        
        with tab1:
            st.markdown(f"### 🌤️ 기후 특성")
            st.info(desc['기후'])
            st.markdown(f"**🌡️ 평균 기온:** {desc['평균기온']}")
        
        with tab2:
            col1, col2 = st.columns(2)
            
            with col1:
                st.markdown("### 🏨 추천 숙소")
                st.markdown(f"**호텔명:** {hotel['name']}")
                st.markdown(f"**평점:** ⭐ {hotel['rating']}")
                st.markdown(f"**특징:** {hotel['desc']}")
            
            with col2:
                st.markdown("### 💸 예상 예산")
                for category, amount in breakdown.items():
                    st.markdown(f"• **{category}:** {amount}")
        
        with tab3:
            st.markdown("### 🏞️ 주요 관광지")
            for i, spot in enumerate(desc["관광지"], 1):
                st.markdown(f"{i}. {spot}")
        
        with tab4:
            st.markdown("### 🍽️ 현지 맛집")
            for i, restaurant in enumerate(desc["맛집"], 1):
                st.markdown(f"{i}. {restaurant}")
        
        # 여행 명언
        st.markdown("---")
        st.markdown("### 📖 여행 명언")
        quote = get_travel_quote()
        st.markdown(f"> {quote}")
        
        # 마무리 메시지
        st.success("🎒 멋진 여름 여행 되시길 바랍니다! 🌞🗺️")
    
    else:
        # 초기 상태에서 보여줄 내용
        st.markdown("### 👈 왼쪽 사이드바에서 여행 취향을 입력해주세요!")
        
        # 여행지 미리보기 (이미지 포함)
        st.markdown("---")
        st.markdown("### 🗺️ 추천 가능한 여행지들")
        
        destinations = get_destinations_data()
        
        # 여행지를 카드 형태로 표시 (2열 구성)
        for i in range(0, min(6, len(destinations)), 2):
            cols = st.columns(2)
            for j, col in enumerate(cols):
                if i + j < len(destinations):
                    dest = destinations[i + j]
                    with col:
                        # 미리보기 이미지 표시
                        preview_image = get_unsplash_image(dest['name'])
                        st.image(preview_image, use_column_width=True)
                        
                        with st.container():
                            st.markdown(f"**{dest['name']}**")
                            st.markdown(f"🌡️ {dest['climate']} | 🎯 {dest['activity']}")
                            st.markdown(f"💰 {dest['min_budget']}만원부터")
                            st.markdown("---")

if __name__ == "__main__":
    main()
