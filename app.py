import streamlit as st
import pandas as pd

def get_category_words_by_age(age):
    age_category_data = {
        1: {'기본어': ['엄마', '아빠', '맘마', '물', '까까']},
        2: {'사물': ['자동차', '인형', '공'], '동물': ['멍멍이', '야옹이'], '음식': ['귤', '사과'], '형용사': ['크다', '작다']},
        3: {'색깔': ['빨강', '파랑', '노랑'], '모양': ['세모', '네모', '동그라미'], '숫자': ['하나', '둘', '셋'], '동물': ['고양이', '강아지'], '과일': ['딸기', '포도'], '탈것': ['버스', '자동차'], '감정': ['기쁨', '슬픔'], '수량': ['많다', '적다'], '높낮이': ['높다', '낮다']},
        4: {'직업': ['경찰', '소방관', '선생님'], '계절': ['봄', '여름', '가을', '겨울'], '시간': ['아침', '점심', '저녁'], '장소': ['학교', '병원', '놀이터'], '감정': ['행복', '화남'], '사회': ['친구', '가족']},
        5: {'가족': ['할머니', '할아버지'], '사회규칙': ['약속', '질서'], '협동': ['나눔', '도움'], '감정': ['용기', '인내'], '자연': ['지구', '우주']},
        6: {'학습': ['역사', '과학', '예술', '문화'], '활동': ['스포츠', '탐험'], '문제해결': ['추리', '창의'], '지식': ['나라', '세계']},
        7: {'가치': ['도덕', '윤리', '정의'], '환경': ['보호', '사랑'], '미래': ['계획', '실천'], '탐구': ['지식', '탐구', '발명']}
    }

    result_data_for_df = []

    if age in age_category_data:
        current_age_info = age_category_data[age]
        for category, words_list in current_age_info.items():
            for word in sorted(words_list):
                result_data_for_df.append({'연령': age, '범주어': category, '단어 예시': word})
    elif age < 1:
        return []
    else:
        all_categories_with_words = {}
        for i in range(1, age + 1):
            if i in age_category_data:
                for category, words_list in age_category_data[i].items():
                    if category not in all_categories_with_words:
                        all_categories_with_words[category] = set()
                    all_categories_with_words[category].update(words_list)

        for category in sorted(all_categories_with_words.keys()):
            for word in sorted(list(all_categories_with_words[category])):
                result_data_for_df.append({'연령': age, '범주어': category, '단어 예시': word})

    return result_data_for_df


# ✅ Streamlit UI 시작
st.title("아동 연령별 범주어 추천 프로그램")

child_age = st.number_input("아동의 연령을 입력하세요", min_value=1, max_value=10, step=1)

if st.button("결과 보기"):
    words_data = get_category_words_by_age(child_age)

    if words_data:
        df_temp = pd.DataFrame(words_data)
        df = df_temp.groupby(['연령', '범주어'])['단어 예시'].apply(lambda x: ', '.join(x)).reset_index()

        st.subheader(f"{child_age}세 아동 범주어 리스트")
        st.dataframe(df)
    else:
        st.warning("데이터가 없습니다.")
