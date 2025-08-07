import streamlit as st

# MBTI 유형과 추천 직업, 취미
mbti_recommendations = {
    "ISTJ": {
        "job": ["회계사", "법률 전문가", "프로젝트 관리자"],
        "hobby": ["독서", "퍼즐", "정리정돈"]
    },
    "ISFJ": {
        "job": ["간호사", "교사", "사회복지사"],
        "hobby": ["자원봉사", "요리", "자기계발"]
    },
    "INFJ": {
        "job": ["심리학자", "상담가", "작가"],
        "hobby": ["명상", "창작 활동", "독서"]
    },
    "INTJ": {
        "job": ["엔지니어", "과학자", "전략 기획자"],
        "hobby": ["수학", "과학 실험", "추리 게임"]
    },
    "ISTP": {
        "job": ["기술자", "프로그램 개발자", "기계공"],
        "hobby": ["모터스포츠", "기계 조립", "비디오 게임"]
    },
    "ISFP": {
        "job": ["디자이너", "예술가", "음악가"],
        "hobby": ["미술", "음악", "여행"]
    },
    "INFP": {
        "job": ["작가", "예술가", "상담가"],
        "hobby": ["글쓰기", "자기성찰", "자연 탐방"]
    },
    "INTP": {
        "job": ["프로그램 개발자", "발명가", "철학자"],
        "hobby": ["수학 문제 풀기", "독서", "논리적 토론"]
    },
    "ESTP": {
        "job": ["판매 전문가", "마케팅", "운동선수"],
        "hobby": ["스포츠", "모험 여행", "사회적 활동"]
    },
    "ESFP": {
        "job": ["연예인", "이벤트 플래너", "사회복지사"],
        "hobby": ["무용", "음악", "파티"]
    },
    "ENFP": {
        "job": ["광고 기획자", "상담가", "마케팅 전문가"],
        "hobby": ["창작", "여행", "사교 활동"]
    },
    "ENTP": {
        "job": ["변호사", "기업가", "작가"],
        "hobby": ["논리적 토론", "스타트업 창업", "책 읽기"]
    },
    "ESTJ": {
        "job": ["관리자", "경영자", "군인"],
        "hobby": ["운동", "정리정돈", "독서"]
    },
    "ESFJ": {
        "job": ["교사", "간호사", "인사 담당자"],
        "hobby": ["자원봉사", "친목 모임", "요리"]
    },
    "ENFJ": {
        "job": ["리더", "상담가", "사회운동가"],
        "hobby": ["멘토링", "봉사 활동", "문화 활동"]
    },
    "ENTJ": {
        "job": ["CEO", "경영 전략가", "법률 전문가"],
        "hobby": ["비즈니스", "독서", "토론"]
    }
}

# 스트림릿 앱 제목
st.title("MBTI 직업 & 취미 추천")

# MBTI 유형 선택
mbti_type = st.selectbox("당신의 MBTI 유형을 선택하세요:", list(mbti_recommendations.keys()))

# 선택된 MBTI에 대한 직업과 취미 추천
job_suggestions = mbti_recommendations[mbti_type]["job"]
hobby_suggestions = mbti_recommendations[mbti_type]["hobby"]

# 직업 추천 출력
st.subheader(f"{mbti_type} 유형의 추천 직업:")
for job in job_suggestions:
    st.write(f"- {job}")

# 취미 추천 출력
st.subheader(f"{mbti_type} 유형의 추천 취미:")
for hobby in hobby_suggestions:
    st.write(f"- {hobby}")
